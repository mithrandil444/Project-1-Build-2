from network import LoRa
import socket
import time
import ubinascii
import ustruct

Europe = LoRa.EU868

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('70B3D57ED003E4C9')
app_key = ubinascii.unhexlify('20EDF2610F5F451607EA87E50CFC1C40')
dev_eui = ubinascii.unhexlify('00C517882FED489A')

def setup_lora():
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')
    print('Joined')

def send_to_lora(float):

    packet=ustruct.pack('f',float)
    print(packet)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    s.send(packet)
    s.setblocking(False)
    #data = s.recv(64)
