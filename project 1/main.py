import sonarsensor
import loraconnect2
from time import sleep
import wificonnect
import urequests as requests

# adafruit config
aio_key = "aio_SWaA65ahbUNaL8Qd3D6o28GMq4Uy"
username = "mithrandil444"
feed_name = "houthakken"

#Lora
loraconnect2.setup_lora()
distance= sonarsensor.send_distance()
loraconnect2.send_to_lora(distance)
#Wifi
wificonnect.connect()

while True:

    distance= sonarsensor.send_distance()
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': distance}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        r.close()
    except Exception as e:
        print(e)
    sleep(10)
