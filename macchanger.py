#!/usr/bin/env python3
import argparse
import subprocess
import re
from termcolor import colored

def get_aruments():
    parser = argparse.ArgumentParser(description="Tool to change MAC address of a Network Interface")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Network interface")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="New MAC address for the network interface")

    return parser.parse_args()

def input_validation(interface, mac_address):
    valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface)
    valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)

    return valid_interface and valid_mac_address

def change_mac_address(interface, mac_address):
    if input_validation(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])

        print(colored(f"\n[+] MAC address chenged successfully\n", 'cyan'))
    else:
        print(colored(f"\n[!] Values entered are invalid!\n", 'red'))

def run_scrip():
    args = get_aruments()
    change_mac_address(args.interface, args.mac_address)
    
if __name__ == "__main__":
    run_scrip()
