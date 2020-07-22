from flask import Flask, render_template, request, Response

import robot

import time

app = Flask('Robot control')
state_msg = 'Hola desde raspiCar '
robot.init()

@app.route('/')
def index():
   return render_template('./index.html', state_msg=state_msg)

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
