from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

hub = PrimeHub()

left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

WHEEL_DIAMETER = 49.5   # mm (typical for SPIKE Prime large wheels)
AXLE_TRACK = 73.5     # your current guess

robot = DriveBase(left, right, WHEEL_DIAMETER, AXLE_TRACK)

# hub.speaker.beep()
# robot.turn(90)
robot.straight(1000)
# hub.speaker.beep()