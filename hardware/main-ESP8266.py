from machine import Pin
from time import sleep
import urequests
import dht

# Script para ESP8266

wlan_ssid = ''
wlan_password = ''
node_red_post_url =''

led = Pin(2, Pin.OUT)
adc = machine.ADC(0) # ADC = Abnalod to Digital Converter (nosso sensor de umidade), conectado no pino 0 da nossa placa de desenvolvimento
d = dht.DHT11(Pin(2)) # sensor de umidade DHT modelo 11, conectado no pino 2 da placa de desenvolvimento

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
        d.measure() # le o sensor de umidade e temperatura
        valorLido = {"valor": adc.read(), "temperatura":d.temperature(), "umidade":d.humidity()} # forma um dicionário com os valores lidos pelos sensores
        
        led.value(0)
        response = urequests.post(node_red_post_url, json=valorLido) # manda um POST com os dados formados para a URL do Node-RED
        response.close()
        led.value(1)
        
        print(valorLido)
        sleep(5)
    except:
        machine.reset()
