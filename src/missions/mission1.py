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

from robot.Sounds import(
    play_handoff_to_mission_code_ding_dong,
    play_handoff_to_nav_code_ding_dong
)

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

STRAIGHT_AMOUNT = 900
TURN_AMOUNT = 200
SMALL_MOVE = 100
NUM_RUNS = 3

def run():
    for i in range(NUM_RUNS):
        print(f"Run {i} start")
        play_handoff_to_mission_code_ding_dong()
        drive_backward(STRAIGHT_AMOUNT)
        play_handoff_to_nav_code_ding_dong()
        turn_left(TURN_AMOUNT/2)
        drive_backward(SMALL_MOVE)
        turn_left(TURN_AMOUNT/2)
        play_handoff_to_mission_code_ding_dong()
        drive_backward(STRAIGHT_AMOUNT)
        play_handoff_to_nav_code_ding_dong()
        turn_right(TURN_AMOUNT/2)
        drive_backward(SMALL_MOVE)
        turn_right(TURN_AMOUNT/2)
        print(f"Run {i} done")
    turn_left(TURN_AMOUNT/2)
    drive_forward(SMALL_MOVE*NUM_RUNS)