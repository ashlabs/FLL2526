from robot.drive import(
    drive_forward,
    drive_backward,
    turn_left,
    turn_right
)

from robot.arms import(
    raise_left_arm,
    lower_left_arm,
    raise_right_arm,
    lower_right_arm,
    move_left_arm_to,
    move_right_arm_to
)

def run():
    drive_forward(100)
    drive_backward(100)
    