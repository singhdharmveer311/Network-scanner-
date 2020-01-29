import os
import argparse
try:
    import scapy.all as scapy
except:
    os.system('pip3 install scapy')
    import scapy.all as scapy
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
ip = argument()
checker(ip.target)
scan(ip.target)
