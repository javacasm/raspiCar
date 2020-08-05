#!/usr/bin/python3
"""
Ejemplo de lectura de temperatura, presión y humedad con el sensor bme280
Se requiere el módulo RPi.bme280

Instalación:

pip3 install RPi.bme280
"""

import smbus2
import bme280

import utils

port = 1
address = 0x76 # usaremos la dirección que hemos encontrado

bus = None
calibration_params = None

def init():
    global bus
    global calibration_params

    bus = smbus2.SMBus(port)

    calibration_params = bme280.load_calibration_params(bus, address) # parámetros de compensación

def getData():
    global bus
    global calibration_params

# leemos los datos
    data = bme280.sample(bus, address, calibration_params) 

# los mostramos en otro formato
    utils.myLog(str(data))
    return data.temperature, data.pressure, data.humidity, data.timestamp, data.id
