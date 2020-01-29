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

