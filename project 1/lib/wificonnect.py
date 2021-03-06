# ---- Imports ----

import pycom
from network import WLAN
import machine
import time


def connect():

    wlan = WLAN(mode=WLAN.STA)
    pycom.heartbeat(False)
    wlan.connect(ssid='wifinaam', auth=(WLAN.WPA2, 'wachtwoord'))



    while not wlan.isconnected():
        time.sleep(5)
        pycom.rgbled(0xFF0000)          # Red
        print("no connection")
        machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)              # Green
