import robot
import time

espera = 2 

robot.init()
for i in range(0,4):
    robot.forward(robot.throttle_max)
    time.sleep(espera)
    robot.right(robot.throttle_max)
    time.sleep(espera/2)
robot.stop()


