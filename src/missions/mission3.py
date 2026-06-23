from robot.drive import(
    drive_forward,
    drive_backward,
    turn_left,
    turn_right,
    enable_gyro,
    disable_gyro
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
    play_handoff_to_nav_code_ding_dong,
    play_robot_moving_ding_dong,
    play_robot_about_to_move_ding_dong
)

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait, Matrix

STRAIGHT_AMOUNT = 900
TURN_AMOUNT = 195
SMALL_MOVE = 100
NUM_RUNS = 3

HUB = PrimeHub()

def run():
    play_robot_moving_ding_dong()
    enable_gyro()
    collect()
    disable_gyro()
    waitForButton(Button.CENTER)
    runCountdown(10, 3)
    play_delivery_animation(300)
    enable_gyro()
    deliver()
    disable_gyro()
    wait(300)
    HUB.display.icon(Matrix([
            [0, 0, 0, 0, 255],
            [0, 0, 0, 255, 0],
            [255, 0, 255, 0, 0],
            [0, 255, 0, 0, 0],
            [0, 0, 0, 0, 0]]))
    waitForButton(Button.CENTER)

def collect():
    for i in range(NUM_RUNS):
        HUB.display.number(i + 1)
        print(f"Run {i + 1} start")
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
        print(f"Run {i + 1} done")
    turn_left(TURN_AMOUNT/2)
    drive_forward(SMALL_MOVE*NUM_RUNS)
    turn_right(TURN_AMOUNT/2)

def deliver():
    play_handoff_to_mission_code_ding_dong()
    drive_backward(STRAIGHT_AMOUNT)
    play_handoff_to_nav_code_ding_dong()
    drive_forward(STRAIGHT_AMOUNT)

def waitForButton(button : Button = Button.CENTER):
    if button == Button.CENTER:
        HUB.display.icon(Matrix([
                [0, 0, 0, 0, 0],
                [0, 255, 255, 255, 0],
                [0, 255, 255, 255, 0],
                [0, 255, 255, 255, 0],
                [0, 0, 0, 0, 0]]))
    elif button == Button.LEFT:
        HUB.display.icon(Matrix([
                [0, 0, 0, 0, 0],
                [255, 255, 255, 0, 0],
                [255, 255, 255, 0, 0],
                [255, 255, 255, 0, 0],
                [0, 0, 0, 0, 0]]))
    elif button == Button.RIGHT:
        HUB.display.icon(Matrix([
                [0, 0, 0, 0, 0],
                [0, 0, 255, 255, 255],
                [0, 0, 255, 255, 255],
                [0, 0, 255, 255, 255],
                [0, 0, 0, 0, 0]]))
    elif button == Button.BLUETOOTH:
        HUB.display.icon(Matrix([
                [0, 0, 255, 255, 255],
                [0, 0, 255, 255, 255],
                [0, 0, 255, 255, 255],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]))
    else:
        HUB.display.icon(Matrix([
                [0, 0, 0, 0, 0],
                [255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255],
                [0, 0, 0, 0, 0]]))
    HUB.light.on(Color.RED)
    while button not in HUB.buttons.pressed():
        wait(10)
    HUB.light.on(Color.GREEN)
    while button in HUB.buttons.pressed():
        wait(10)
    wait(250)

def runCountdown(length : int = 10, warning : int = 3):
    HUB.light.on(Color.YELLOW)
    for i in range(length, 0):
        HUB.display.number(i)
        if i == warning:
            HUB.light.on(Color.ORANGE)
            play_robot_about_to_move_ding_dong()
        wait(1000)
    HUB.light.on(Color.GREEN)
    play_robot_moving_ding_dong()

def play_delivery_animation(speed : int = 300):
    HUB.display.animate([
        Matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]),
        Matrix([
            [0, 255, 255, 255, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]),
        Matrix([
            [0, 0, 0, 0, 0],
            [0, 255, 255, 255, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]),
        Matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 255, 255, 255, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]),
        Matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 255, 255, 255, 0],
            [0, 0, 0, 0, 0]]),
        Matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 255, 255, 255, 0]]),
        ], speed)