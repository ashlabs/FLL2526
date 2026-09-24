from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

LeftMotor = Motor(Port.A, Direction.CLOCKWISE)
RightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

Base = DriveBase(LeftMotor, RightMotor, 56, 104)

SecondArm = Motor(Port.D, Direction.COUNTERCLOCKWISE)

Base.straight(500)

SecondArm.reset_angle(0)
SecondArm.run_target(500, -120)
SecondArm.run_target(100, 0)

Base.straight(-500)