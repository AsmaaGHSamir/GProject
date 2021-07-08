from NetworkScan import NetworkScan
from Helper import *
import getopt
import sys

def get_network_interface(interface_to_scan=None):
    for network, netmask, gateway, interface, address, metric in conf.route.routes:
        if interface_to_scan and interface_to_scan != interface:
            continue

        # skip loopback network and default gw
        if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0':
            continue

        if netmask <= 0 or netmask == 0xFFFFFFFF:
            continue

        # skip docker interface
        if interface != interface_to_scan and interface.startswith('docker') or interface.startswith('br-'):
            print("Skipping interface '%s'" % interface)
            continue

        net = to_CIDR_notation(network, netmask)

        if net:
            return (net, interface)
    print("No interface found")
    sys.exit(1)


#if __name__ == "__main__":

def maincode():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:', ['help', 'interface='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    
    check_root()

    interface = None

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-i', '--interface'):
            interface = a
        else:
            assert False, 'unhandled option'

    network, interface = get_network_interface(interface_to_scan=interface)
    scanner = NetworkScan(network, interface)

    try:
        print("Scannig And Captureing packets from  {0} on {1}".format(network,interface))
        scanner.start_scan()
    except KeyboardInterrupt as e:
        scanner.stop_scan()
        print("Stopping Capture")
    except:
        scanner.stop_scan()
        print("Stopping Capture")


#maincode()