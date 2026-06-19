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

from robot import Sounds

STRAIGHT_AMOUNT = 1000
TURN_AMOUNT = 100

def run():
    for i in range(100):
        Sounds.play_handoff_to_mission_code_ding_dong()
        drive_backward(STRAIGHT_AMOUNT)
        Sounds.play_handoff_to_nav_code_ding_dong()
        turn_left(TURN_AMOUNT)
        Sounds.play_handoff_to_mission_code_ding_dong()
        drive_backward(STRAIGHT_AMOUNT)
        Sounds.play_handoff_to_nav_code_ding_dong()
        turn_right(TURN_AMOUNT)
    
if __name__ == "__main__":
    import main
    main.main()