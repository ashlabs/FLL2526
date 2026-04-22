from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop
import umath as math
from pybricks.tools import wait
from pybricks.parameters import Direction


def gyro_turn(robot, hub, target_angle_deg, speed=50, tolerance=1):
    """
    Turns the robot to a relative angle using the hub's gyro (IMU).
    Positive target_angle_deg = clockwise, negative = counter-clockwise.
    speed = turning speed (deg/sec, affects motor power)
    tolerance = acceptable error in degrees
    """
    # Read current heading
    current_heading = hub.imu.heading()
    goal_heading = (current_heading + target_angle_deg) % 360

    while True:
        # Calculate shortest angular difference
        heading_error = (goal_heading - hub.imu.heading() + 180) % 360 - 180

        if abs(heading_error) <= tolerance:
            break  # reached target

        # Turn direction proportional to error
        turn_power = speed * (1 if heading_error > 0 else -1)

        # Send drive command: forward=0 (stay in place), turn rate = turn_power
        robot.drive(0, turn_power)

        hub.wait(10)

    # Stop precisely
    robot.stop(Stop.BRAKE)


hub = PrimeHub()
left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

WHEEL_DIAMETER = 49.5 # mm
# AXLE_TRACK = 79.375 # mm
AXLE_TRACK = 73.5 # mm


robot = DriveBase(left_motor=left, right_motor=right, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)

robot.settings(straight_speed=100,turn_rate=60)


# Reset IMU
hub.imu.reset_heading(0)

# hub.speaker.beep()

# hub.display.text("OK")

robot.turn(90)
gyro_turn(robot, hub, 90, 50, 1)
# wait(50)
# robot.turn(-90)
# wait(50)

# robot.straight(100)
# wait(50)

# hub.speaker.beep()
# wait(50)

hub.display.text("Done")
wait(50)


