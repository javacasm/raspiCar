from flask import Flask, render_template, request, Response

import robot

import time
import smbus2
import bme280

port = 1
address = 0x76 # usaremos la dirección que hemos encontrado
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address) # parámetros de compensación

app = Flask('Robot control')
temperature  = 0
presion = 0
humedad = 0
fechaDatos = ''
state_msg = 'Hola desde raspiCar '
robot.init()

@app.route('/')
def index():
   data = bme280.sample(bus, address, calibration_params) 

   fechaDatos = data.timestamp
   temperatura = int(data.temperature)
   presion = int(data.pressure)
   humedad = int(data.humidity)
   return render_template('./index.html', state_msg=state_msg, presion = presion, humedad = humedad, temperatura = temperatura, fechaDatos = fechaDatos)

@app.route('/move/<direction>')
def move(direction):
    if direction == 'forward':
       robot.forward(0.5)
    if direction == 'backward':
       robot.backward(0.5)
    if direction == 'left':
       robot.left(0.5)
    if direction == 'right':
       robot.right(0.5)
    return '{}'

@app.route('/stop')
def stop():
    robot.stop()
    return '{}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
