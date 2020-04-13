#!/usr/bin/python3

import scapy.all as scapy

# scapy.ls can be used to find what are the possible parameters available with the scapy class

#    scapy.ls(scapy.Ether())
#    scapy.ls(scapy.ARP())      # get the list of commands we have for a particular class
#    arp_quest.show()  can be used to see the packets
#    scapy.srp() gives list values, answered and unanswered, we need only answered hence [0] also answered gives list of two values, one is request and other is reply, we need only reply hence [1]


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast= broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMac Address\n-------------------------------------------------------------")
    for ele in answered_list:
        print(ele[1].psrc + "\t\t" + ele[1].hwsrc)

scan("192.168.0.1/24")

