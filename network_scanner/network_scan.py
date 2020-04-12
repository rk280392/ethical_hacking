#!/usr/bin/python3

import scapy.all as scapy

# scapy.ls can be used to find what are the possible parameters available with the scapy class

#    scapy.ls(scapy.Ether())
#    scapy.ls(scapy.ARP())      # get the list of commands we have for a particular class


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast= broadcast/arp_request
    arp_request_broadcast.show()
   
scan("192.168.0.1/24")
