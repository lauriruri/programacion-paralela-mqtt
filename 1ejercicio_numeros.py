# -*- coding: utf-8 -*-

from paho.mqtt.client import Client
import math

def on_message(mqttc, userdata, msg):
    d = float(msg.payload)
    n = int(round(d))
    print("Número",msg.payload,'int',n,'float',d, 'entero' if d==n else 'real')
    print("¿Es primo ", n, "?",  'si' if es_primo(n) else 'no')
    
def es_primo(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i)==0:
            return False
    return True

def main():
    mqttc = Client()
    mqttc.on_message = on_message
    mqttc.connect("simba.fdi.ucm.es")
    mqttc.subscribe('clients/laura/numbers')
    mqttc.loop_forever()


if __name__ == '__main__':
    main()