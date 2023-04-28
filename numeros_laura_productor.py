# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:22:26 2023

"""

from paho.mqtt.client import Client
from multiprocessing import Lock
import time
from random import randint,random

def on_publish(mqttc, userdata, mid, message, topic):
    print(f"MESSAGE PUBLISHED: {message}")
    print(f"TOPIC: {topic}")
    

def main(hostname):
    client = Client()
    client.connect(hostname)
    #client.on_publish = on_publish
    client.on_publish = lambda client, userdata, mid: on_publish(client, userdata, mid, message, topic)
    topic = "clients/laura/numbers"
    #topic2 = "clients/laura/numbers/reales"
    while True:
        message = randint(0,99)
        #topic = topic1
        client.publish(topic, message)
        time.sleep(2)
        message = random()
        #topic = topic2
        client.publish(topic, message)
        time.sleep(2)

if __name__ == "__main__":
    hostname = "simba.fdi.ucm.es"
    main(hostname)