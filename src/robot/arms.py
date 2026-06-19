from pybricks.pupdevices import Motor

from robot.config import (
    LEFT_ARM_PORT,
    RIGHT_ARM_PORT,
    LEFT_ARM_DIRECTION,
    RIGHT_ARM_DIRECTION,
    ARM_SPEED,
    LEFT_ARM_UP_ANGLE,
    LEFT_ARM_DOWN_ANGLE,
    RIGHT_ARM_UP_ANGLE,
    RIGHT_ARM_DOWN_ANGLE
)

left_arm = Motor(LEFT_ARM_PORT, LEFT_ARM_DIRECTION)

right_arm = Motor(RIGHT_ARM_PORT, RIGHT_ARM_DIRECTION)

def reset_arms():
    left_arm.reset_angle(0)
    right_arm.reset_angle(0)

def move_left_arm_to(angle):
    left_arm.run_target(
        ARM_SPEED,
        angle
    )

def move_right_arm_to(angle):
    right_arm.run_target(
        ARM_SPEED,
        angle
    )

def raise_left_arm():
    move_left_arm_to(LEFT_ARM_UP_ANGLE)

def lower_left_arm():
    move_left_arm_to(LEFT_ARM_DOWN_ANGLE)

def raise_right_arm():
    move_right_arm_to(RIGHT_ARM_UP_ANGLE)

def lower_right_arm():
    move_right_arm_to(RIGHT_ARM_DOWN_ANGLE)

def stop_arms():
    left_arm.stop()
    right_arm.stop()

