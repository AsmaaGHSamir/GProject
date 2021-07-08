#this files contains all list of pure helper functions
from scapy.config import conf
from scapy.sendrecv import SndRcvHandler
from scapy.data import ETH_P_ALL
from scapy.utils import ltoa
import math
import os
import sys


def long2net(arg):
    if (arg <= 0 or arg >= 0xFFFFFFFF):
        raise ValueError("illegal netmask value", hex(arg))
    return 32 - int(round(math.log(0xFFFFFFFF - arg, 2)))

def get_L3socket(iface,promisc=None, s_filter=None, nofilter=0):
    return conf.L3socket(promisc=promisc, filter=s_filter, nofilter=nofilter, iface=iface)

def get_l2socket(iface, promisc=None, s_filter=None, nofilter=0, s_type=ETH_P_ALL):
    return conf.L2socket(promisc=promisc, iface=iface,filter=s_filter, nofilter=nofilter, type=s_type)


def srp(s, x,*args,**kwargs):
    """Send and receive packets at layer 2 if given layer 2 socket
    nofilter: put 1 to avoid use of bpf filters
    retry:    if positive, how many times to resend unanswered packets
            if negative, how many times to retry when no more packets are answered
    timeout:  how much time to wait after the last packet has been sent
    verbose:  set verbosity level
    multi:    whether to accept multiple answers for the same stimulus
    """
    sndrcver = SndRcvHandler(s, x, *args, **kwargs)
    return sndrcver.results()

def srp1(s, x, *args, **kwargs):
    # type: (*Packet, **Any) -> Optional[Packet]
    """
    Send and receive packets at layer 2 if given layer 2 socket and return only the first answer
    """
    ans, _ = srp(s, x, *args, **kwargs)
    if len(ans) > 0:
        pkt = ans[0][1]  # type: Packet
        return pkt
    else:
        return None


def to_CIDR_notation(bytes_network, bytes_netmask):
    network = ltoa(bytes_network)
    netmask = long2net(bytes_netmask)
    net = "%s/%s" % (network, netmask)
    if netmask < 16:
        print("%s is too big. skipping" % net)
        return None
    return net

def check_root():
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
        except:
             print('You need to run this script with administrator privileges try run as administrator', file=sys.stderr)
             sys.exit(1)
    else:
        if os.geteuid() != 0:
            print('You need to be root to run this script', file=sys.stderr)
            sys.exit(1)

def usage():
    print("Usage: %s [-i <interface>]" % sys.argv[0])