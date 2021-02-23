# ---- Imports ----

import pycom
from network import WLAN
import machine
import time

# ---- Config ----

wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)
wlan.connect(ssid='telenet-C9C22', auth=(WLAN.WPA2, 'k0T3bU6R0EyA'))

# ---- Loop ----

while not wlan.isconnected():
    time.sleep(2)
    pycom.rgbled(0xFF0000)          # Red
    print("no connection")
    machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)              # Green