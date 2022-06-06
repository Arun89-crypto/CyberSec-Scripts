#!/usr/bin/env python
import sys
import socket
import time
from sty import fg, bg
import nmap

scanner = nmap.PortScanner()


def main():
    def printBanner():
        print('''
-------------Welcome-------------
_____  ____  ____   ____   __  _ 
| ()_)(_ (_`/ (__` / () \ |  \| |
|_|  .__)__)\____)/__/\__\|_|\__|
-------------Welcome-------------

Faster than NMAP :) but uses NMAP :]

--help : For Help Center
        ''')

    def printHelp():
        print('''
-------------Welcome-------------
_____  ____  ____   ____   __  _ 
| ()_)(_ (_`/ (__` / () \ |  \| |
|_|  .__)__)\____)/__/\__\|_|\__|
-------------Welcome-------------

Faster than NMAP :) but uses NMAP :]


--------------------------
HELP SECTION
--------------------------

Basic PORT Scanning :
python3 PortScanner.py [Target_IP]

Basic PORT Scanning with verbose :
python3 PortScanner.py [Target_IP] -v

--------------------------
NMAP SCANNING SECTION
--------------------------

Services you can add to your nmap scan :

[1] -> Stealth Scan (-sS)
[2] -> TCP Scan (-sT)
[3] -> UDP Scan (-sU)
[4] -> Services Scan (-sV)
[5] -> Basic Script Scan (-sC)
[6] -> Aggressive (-A)
[7] -> Operating System Version (-O)
        ''')

    # Inputs and arguments
    arg1 = sys.argv[1]
    try:
        arg2 = sys.argv[2]
    except:
        arg2 = ""

    if(arg1 == "--help"):
        printHelp()
        return
    else:
        printBanner()

    arg1 = socket.gethostbyname(arg1)

    # -------------
    # PORT SCANNING
    # -------------
    ports = []

    print(f"Starting Scan on {arg1}")
    count = 0
    start = time.time()
    for i in range(1, 1000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((arg1, i))
                print(fg.li_green+f"[+] PORT {i} is OPEN"+fg.rs)
                ports.append(i)
        except:
            if(arg2 == "-v"):
                print(fg.red+f"[-] PORT {i} is CLOSED"+fg.rs)

    end = time.time()
    print("-----------------RESULT-----------------")
    print("Total Ports open : ", count)
    print(ports)
    print(f"Total time taken : {end - start} seconds")
    print("-----------------RESULT-----------------")

    decision = input(
        "Do you want to run a NMAP scan on open ports(Y/N) ? ")

    if(decision == 'Y'):
        print("Select options for scan :")
        print('''
    [1] -> Stealth Scan (-sS)
    [2] -> TCP Scan (-sT)
    [3] -> UDP Scan (-sU)
    [4] -> Services Scan (-sV -sC)
    [5] -> Compehensive Scan (-sC -sS -sV -A -O)
    [6] -> OS Detection (-O)
        ''')

        nmap_option = int(input("Enter option : "))
        port_string = "-P"
        for port in ports:
            port_string += str(port) + ","

        if(nmap_option == 1):
            scanner.scan(hosts=arg1, arguments=f'-v -sS {port_string}')
        else:
            print("Some other option scanned")
    else:
        exit(1)


if __name__ == "__main__":
    main()
