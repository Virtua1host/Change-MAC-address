#!/usr/bin/env python3

import subprocess 
import optparse   
import re         

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Inteface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC addres")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser_error("Please specify an MAC, use --hepl for mere info")
    return options 

def change_mac(interface, new_mac):
	print("[+] Chaning MAC addres for " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC addres.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = ", str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC addres was successfully changed to " + current_mac)
else:
    print ("[-] MAC addres did not get change.")





 
