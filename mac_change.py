#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="Mac to change")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please sepecify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify new mac, use --help for more info.")
    return options

def mac_change(interface, new_mac):
    print("[+1] changing mac address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):     
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("couldn't get mac address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))
mac_change(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("Mac sucessfully changed to " + current_mac)
else:
    print("cannot change mac")
