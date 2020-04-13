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

    client_list = []
    for ele in answered_list:
        client_dict = {"ip":ele[1].psrc, "mac": ele[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(client_list):
    print("IP\t\t\tMac Address\n-------------------------------------------------------------")
    for client in client_list:
        print(client["ip"] + "\t\t" + client["mac"])
        

scan_result = scan("192.168.0.1/24")
print_result(scan_result)

