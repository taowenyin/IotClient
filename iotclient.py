#!/usr/bin/python2.7

import sys, socket
sys.path.insert(0, '/usr/lib/python2.7/bridge')

from time import sleep
from bridgeclient import BridgeClient

# Init Arduino Bridge
bridgeClient = BridgeClient()

# Init IOT Server Socket Object
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        # Connect IOT Server
        socketClient.connect(('39.104.87.214', 7280))
        socketClient.settimeout(15)
        # No Error
        bridgeClient.put('ERROR', '2')
        break
    except socket.error, e:
        print "Can't connect to Server as ", e.errno
        sleep(1)
        # Has Error
        bridgeClient.put('ERROR', '1')
        continue

while True:
    # Get Server Data
    try:
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
    except socket.error, e:
        print "Can't connect to Server as ", e.errno
        socketClient.close()
        socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                # Connect IOT Server
                socketClient.connect(('39.104.87.214', 7280))
                socketClient.settimeout(15)
                # No Error
                bridgeClient.put('ERROR', '2')
                break
            except socket.error, e:
                print "Can't connect to Server as ", e.errno
                sleep(1)
                # Has Error
                bridgeClient.put('ERROR', '1')
                continue