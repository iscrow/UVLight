#!/usr/bin/env python3.7 

import time
import RPi.GPIO as GPIO  
import logging

hvac = 7
relay = 11
sleep = 1
logfile = '/tmp/uvlight.log'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(hvac, GPIO.IN)  
GPIO.setup(relay, GPIO.OUT)  

logging.basicConfig(filename=logfile, filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

while True:
    result = GPIO.wait_for_edge(hvac, GPIO.RISING, timeout=sleep*1000)

    if result is None:
        if GPIO.input(relay) == GPIO.HIGH:
            logging.info('Off')
        GPIO.output(relay, GPIO.LOW)
    else:
        if GPIO.input(relay) == GPIO.LOW:
            logging.info('On')
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(sleep)

GPIO.cleanup() 
