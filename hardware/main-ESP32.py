from machine import Pin
from machine import ADC
import urequests
import machine
import time
import dht

# script para ESP32

wlan_ssid = ''
wlan_password = ''
node_red_post_url =''

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wlan_ssid, wlan_password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

print("comecou")
led = Pin(2, Pin.OUT)
d = dht.DHT11(machine.Pin(15))
solo = ADC(Pin(32))
solo.atten(ADC.ATTN_11DB)

do_connect()

while True:
    try:
        d.measure()
        umidadeAr = d.humidity()
        temperatura = d.temperature()
        umidadeSolo = solo.read()
        dados = {"umidade-ar": umidadeAr, "umidade-solo": umidadeSolo, "temperatura": temperatura}
        
        led.value(0)
        response = urequests.post(node_red_post_url, json=dados)
        response.close()
        led.value(1)
        
        time.sleep(1)
    except:
        machine.reset()
