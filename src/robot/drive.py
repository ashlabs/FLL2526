from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from robot.config import (
    LEFT_DRIVE_PORT,
    RIGHT_DRIVE_PORT,
    LEFT_DRIVE_DIRECTION,
    RIGHT_DRIVE_DIRECTION,
    WHEEL_DIAMETER_MM,
    AXLE_TRACK_MM,
    DEFAULT_STRAIGHT_SPEED,
    DEFAULT_STRAIGHT_ACCELERATION,
    DEFAULT_TURN_RATE,
    DEFAULT_TURN_ACCELERATION,
)

hub = PrimeHub()

left_drive_motor = Motor(LEFT_DRIVE_PORT, LEFT_DRIVE_DIRECTION)

right_drive_motor = Motor(RIGHT_DRIVE_PORT, RIGHT_DRIVE_DIRECTION)

drive_base = DriveBase(left_drive_motor, right_drive_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)

def apply_default_drive_settings():
    drive_base.settings(
        straight_speed= DEFAULT_STRAIGHT_SPEED,
        straight_acceleration=DEFAULT_STRAIGHT_ACCELERATION,
        turn_rate=DEFAULT_TURN_RATE,
        turn_acceleration=DEFAULT_TURN_ACCELERATION,
    )

def reset_drive_state():
    drive_base.stop()
    left_drive_motor.reset_angle(0)
    right_drive_motor.reset_angle(0)
    hub.imu.reset_heading(0)
    wait(100)

def drive_forward(distance_mm):
    apply_default_drive_settings()
    drive_base.straight(distance_mm)
    drive_base.stop()

def drive_backward(distance_mm):
    apply_default_drive_settings()
    drive_base.straight(-distance_mm)
    drive_base.stop()

def turn_right(angle_deg):
    apply_default_drive_settings()
    drive_base.turn(angle_deg)
    drive_base.stop()

def turn_left(angle_deg):
    apply_default_drive_settings()
    drive_base.turn(-angle_deg)
    drive_base.stop()

def enable_gyro():
    drive_base.use_gyro(True)

def disable_gyro():
    drive_base.use_gyro(False)