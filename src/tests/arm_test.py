from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Arm1 = Motor(Port.C)
Arm2 = Motor(Port.D)

Arm1.run_angle(100,-45)
# while True:
#     Arm1.run_angle(500, 360)
#     Arm2.run_angle(500,360)