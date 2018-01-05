#!/usr/bin/python2.7

import sys, socket
sys.path.insert(0, '/usr/lib/python2.7/bridge')

from time import sleep
from bridgeclient import BridgeClient

# Init Arduino Bridge
bridgeClient = BridgeClient()

# Init IOT Server Socket Object
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect IOT Server
socketClient.connect(('10.154.197.144', 7280))

while True:
    # Get Server Data
    data = socketClient.recv(1024)
    if not data:
        print('Not data')
    elif 'LED_ON' == data:
        print('LED On')
        # Open LED
        bridgeClient.put('LED', '1')
    elif 'LED_OFF' == data:
        print('LED Off')
        # Close LED
        bridgeClient.put('LED', '2')