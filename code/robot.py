#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uso básico de movimiento de motores con Adafruit Motor Hat

https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all

CC by SA @javacasm
Julio 2020
"""

import time
from adafruit_motorkit import MotorKit
import utils

"""
Posición de los motores en el robot. 
Las flechas indican el sentido de giro con el cableado actual
   -------
^4|       |3^
  |       |
  |       |
v1|       |2v
   -------

"""

v = '0.3'

# niveles de movimiento, la velocidad depende del voltaje
throttle_max = 1
throttle_med = 0.5
throttle_min = 0.3
throttle_stop = 0

def backward(speed):
    global kit
    utils.myDebug('backward ' + str(speed))
    kit.motor4.throttle = -1 * speed
    kit.motor3.throttle = -1 * speed
    kit.motor2.throttle = speed
    kit.motor1.throttle = speed

def forward(speed):
    global kit
    utils.myDebug('forward ' + str(speed))
    kit.motor4.throttle = speed
    kit.motor3.throttle = speed
    kit.motor2.throttle = -1 * speed
    kit.motor1.throttle = -1 * speed 

def stop():
    global kit
    utils.myDebug('stop')
    kit.motor4.throttle = 0
    kit.motor3.throttle = 0
    kit.motor2.throttle = 0
    kit.motor1.throttle = 0

def right(speed):
    global kit
    utils.myDebug('right ' + str(speed))
    kit.motor4.throttle = -1 * speed
    kit.motor3.throttle = speed
    kit.motor2.throttle = -1 * speed
    kit.motor1.throttle = speed

def left(speed):
    global kit
    utils.myDebug('left ' + str(speed))
    kit.motor4.throttle =  speed
    kit.motor3.throttle = -1 * speed
    kit.motor2.throttle =  speed
    kit.motor1.throttle = -1 * speed

kit = None

def init():
    global kit
    utils.myDebug('Robot.py ' + v)
    kit  = MotorKit()
