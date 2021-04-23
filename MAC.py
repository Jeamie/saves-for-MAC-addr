#!/usr/bin/env python3
#reject humanity become an anonymous crab
#LINUX GANG ON TOP
import subprocess
import optparse
import re

def get_arguments():  
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC, use --help for more info")
    return options
def change_mac(interface, new_mac):
    print("[+] Changing MAC for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def regex ():
    # ifoutput = subprocess.check_call(["ifconfig"])
    ifoutput = "jhdasjfsdfhkj 12:34:56:78:90:12 asdklfogdasdsgm kjdhghd"
    ifoutput = re.search(["\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifoutput])
    print(ifoutput)
# options = get_arguments()
# change_mac(options.interface, options.new_mac)
regex()
