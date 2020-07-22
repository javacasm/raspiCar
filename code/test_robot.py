import robot
import time

espera = 5 

robot.init()
for i in range(0,4):
    robot.forward(robot.throttle_med)
    time.sleep(espera)
    robot.right(robot.throttle_med)
    time.sleep(espera)
robot.stop()


