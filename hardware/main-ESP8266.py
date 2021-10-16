from machine import Pin
from time import sleep
import urequests
import dht

# Script para ESP8266

wlan_ssid = ''
wlan_password = ''
node_red_post_url =''

led = Pin(2, Pin.OUT)
adc = machine.ADC(0)
d = dht.DHT11(Pin(2))

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wlan_ssid, wlan_password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()

while True:
    try:
        d.measure()
        valorLido = {"valor": adc.read(), "temperatura":d.temperature(), "umidade":d.humidity()}
        
        led.value(0)
        response = urequests.post(node_red_post_url, json=valorLido)
        response.close()
        led.value(1)
        
        print(valorLido)
        sleep(5)
    except:
        machine.reset()
