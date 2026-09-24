from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

LeftMotor = Motor(Port.A, Direction.CLOCKWISE)
RightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

Base = DriveBase(LeftMotor, RightMotor, 56, 104)

Base.use_gyro(True)

Base.straight(150)

Base.turn(55)

Base.straight(880)

Base.turn(-55)

Base.straight(180)