#!usr/bin/env python3
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)

    print("IP\t\t\tMAC Address\n-------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

    ##     TO GET ABOUT THE VARIABLE YOU DONT'T KNOW
    #              scapy.ls(scapy.ARP)

scan("10.0.2.1/24")

def argument():
    parser = argparse.ArgumentParser(description="A simple Network scanner tool !")
    parser.add_argument('-t','--target',dest='target',help='Specify the IP address or range for scanning.')
    return parser.parse_args()
def checker(x):
    if not x:
        print("Use -h or --help for more info on usage.")
        exit()
def scan(ip):
    a = scapy.ARP(pdst=ip)
    b = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    c = b/a
    result = scapy.srp(c,timeout=1)[0]
    print("------------Network Scanner--------------")
    print("-----------------------------------------")
    print("------IP-----------------MAC-------------")
    print("-----------------------------------------")
    for i in result:
        print(i[1].psrc+"------"+i[1].hwsrc+"---")
