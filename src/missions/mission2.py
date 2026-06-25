from robot.drive import(
    drive_forward,
    drive_backward,
    turn_left,
    turn_right,
    enable_gyro,
    disable_gyro,
    reset_drive_state,
    apply_default_drive_settings,
    apply_fast_drive_settings
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
TURN_AMOUNT = 200
SMALL_MOVE = 350
MED_MOVE = 500
DIAG_MOVE = 700
NUM_RUNS = 3

HUB = PrimeHub()

HANDOFF_SOUND = False
ROBOT_MOVING_WARNINGS = False
ROBOT_ABOUT_TO_MOVE_WARNINGS = False

DEFAULT_COUNTDOWN = 5
DEFAULT_WARNING = 2

def run():
    # Prep
    apply_fast_drive_settings(4, 1, 1, 1)
    reset_drive_state()
    # Part 1
    runCountdown(DEFAULT_COUNTDOWN, DEFAULT_WARNING)
    if ROBOT_MOVING_WARNINGS:
        play_robot_moving_ding_dong()
    enable_gyro()
    collect1()
    disable_gyro()
    waitForButton(Button.CENTER)
    # Part 2
    runCountdown(DEFAULT_COUNTDOWN, DEFAULT_WARNING)
    if ROBOT_MOVING_WARNINGS:
        play_robot_moving_ding_dong()
    enable_gyro()
    collect2()
    disable_gyro()
    waitForButton(Button.CENTER)
    # Part 3
    runCountdown(DEFAULT_COUNTDOWN, DEFAULT_WARNING)
    if ROBOT_MOVING_WARNINGS:
        play_robot_moving_ding_dong()
    enable_gyro()
    collect3()
    disable_gyro()
    waitForButton(Button.CENTER)
    # Delivery
    runCountdown(10, 3)
    play_delivery_animation(300)
    enable_gyro()
    deliver()
    disable_gyro()
    # End
    HUB.display.icon(Matrix([
            [0, 0, 0, 0, 255],
            [0, 0, 0, 255, 0],
            [255, 0, 255, 0, 0],
            [0, 255, 0, 0, 0],
            [0, 0, 0, 0, 0]]))
    waitForButton(Button.CENTER)
    apply_default_drive_settings()
    reset_drive_state()

def collect1():
    HUB.display.number(1)
    if HANDOFF_SOUND:
        play_handoff_to_mission_code_ding_dong()
    drive_backward(MED_MOVE)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    drive_forward(MED_MOVE)

def collect2():
    HUB.display.number(2)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    turn_left(TURN_AMOUNT/2)
    if HANDOFF_SOUND:
        play_handoff_to_mission_code_ding_dong()
    drive_backward(SMALL_MOVE)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    drive_forward(SMALL_MOVE)
    turn_right(TURN_AMOUNT/3)

def collect3():
    HUB.display.number(2)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    turn_left(TURN_AMOUNT/3.5)
    if HANDOFF_SOUND:
        play_handoff_to_mission_code_ding_dong()
    drive_backward(DIAG_MOVE)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    drive_forward(DIAG_MOVE)
    turn_right(TURN_AMOUNT/3)

def deliver():
    if HANDOFF_SOUND:
        play_handoff_to_mission_code_ding_dong()
    drive_backward(STRAIGHT_AMOUNT)
    if HANDOFF_SOUND:
        play_handoff_to_nav_code_ding_dong()
    drive_forward(STRAIGHT_AMOUNT)

def waitForButton(button : Button = Button.CENTER):
    if button == Button.CENTER:
        HUB.display.icon(Matrix([
                [0, 0, 0, 0, 0],
                [0, 255, 255, 255, 0],
                [0, 255, 0, 255, 0],
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

def runCountdown(length : int = DEFAULT_COUNTDOWN, warning : int = DEFAULT_WARNING):
    HUB.light.on(Color.YELLOW)
    for i in range(length, 0, -1):
        HUB.display.number(i)
        print(f"Running in {i} (Total {length}, Warning {warning})")
        if i == warning:
            HUB.light.on(Color.ORANGE)
            if ROBOT_ABOUT_TO_MOVE_WARNINGS:
                play_robot_about_to_move_ding_dong()
        wait(1000)
    HUB.light.on(Color.GREEN)
    
    if ROBOT_MOVING_WARNINGS:
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