# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:22:26 2023

"""

from paho.mqtt.client import Client
from multiprocessing import Lock
import time
from random import uniform

def on_publish(mqttc, userdata, mid, message, topic):
    print(f"MESSAGE PUBLISHED: {message}")
    print(f"TOPIC: {topic}")
    

def main(hostname):
    client = Client()
    client.connect(hostname)
    #client.on_publish = on_publish
    client.on_publish = lambda client, userdata, mid: on_publish(client, userdata, mid, message, topic)
    topic1 = "clients/laura/temperature/t1"
    topic2 = "clients/laura/temperature/t2"
    while True:
        message = uniform(-10.0, 5.0)
        topic = topic1
        client.publish(topic, message)
        time.sleep(2)
        message = uniform(10.0, 18.0)
        topic = topic2
        client.publish(topic, message)
        time.sleep(2)

if __name__ == "__main__":
    hostname = "simba.fdi.ucm.es"
    main(hostname)