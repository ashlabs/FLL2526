
"""
Purpose:
- Run a standard set of repeatable tests while making changes only to the hub position.
- Record results in the assessment sheet.

Notes:
- Tune wheel_diameter, axle_track, and drive speeds to match your robot.
- Keep EVERYTHING else constant between hub-position trials.
- Run the same test set for each hub configuration.
- If you use attachments, either keep the same attachment installed for all tests
  or use a dummy weight.

Suggested test order:
1. Forward straight repeatability
2. Reverse straight repeatability
3. 90-degree point turn
4. 180-degree point turn
5. Curve test
6. Start-stop stability test
7. Push/traction test
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# ----------------------------
# Robot configuration
# ----------------------------
hub = PrimeHub()

# Change ports if needed.
left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

# Tune these to match your base robot.
WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 120

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)

# Conservative defaults for preseason testing.
robot.settings(
    straight_speed=250,      # mm/s
    straight_acceleration=450,
    turn_rate=120,           # deg/s
    turn_acceleration=240
)

# ----------------------------
# Test parameters
# ----------------------------
STRAIGHT_DISTANCE_MM = 800      # 80 cm
CURVE_RADIUS_MM = 350
CURVE_ANGLE_DEG = 90

SLOW_SPEED = 180
MEDIUM_SPEED = 250
FAST_SPEED = 350

START_STOP_DISTANCE_MM = 500
PUSH_DISTANCE_MM = 250

REPEAT_RUNS = 5

# ----------------------------
# Utility helpers
# ----------------------------
def wait_for_center_button(message=None):
    """Pause so team can reset robot and launch next run."""
    if message:
        print("")
        print(message)
    print("Press CENTER button to begin...")
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)
    while Button.CENTER in hub.buttons.pressed():
        wait(10)
    wait(250)

def reset_robot_state():
    """Reset encoders, gyro heading, and stop motion before a run."""
    robot.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    hub.imu.reset_heading(0)
    wait(100)

def beep_ok():
    hub.speaker.beep(800, 100)

def beep_done():
    hub.speaker.beep(1000, 100)
    wait(50)
    hub.speaker.beep(1200, 150)

def announce_test(title):
    print("")
    print("=" * 42)
    print(title)
    print("=" * 42)
    hub.display.text("GO")

def run_straight(distance_mm, speed_mm_s):
    robot.settings(
        straight_speed=speed_mm_s,
        straight_acceleration=450,
        turn_rate=120,
        turn_acceleration=240
    )
    robot.straight(distance_mm)
    robot.stop()

def run_turn(angle_deg, turn_rate_deg_s=120):
    robot.settings(
        straight_speed=250,
        straight_acceleration=450,
        turn_rate=turn_rate_deg_s,
        turn_acceleration=240
    )
    robot.turn(angle_deg)
    robot.stop()

def run_curve(radius_mm, angle_deg):
    robot.settings(
        straight_speed=220,
        straight_acceleration=350,
        turn_rate=100,
        turn_acceleration=200
    )
    robot.curve(radius_mm, angle_deg)
    robot.stop()

# ----------------------------
# Individual tests
# ----------------------------
def forward_repeatability_test():
    announce_test("Forward Straight Repeatability")
    print("Goal: Check drift and stopping consistency while driving forward.")
    print("Run count:", REPEAT_RUNS)
    print("Distance:", STRAIGHT_DISTANCE_MM, "mm")

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot at launch line for FORWARD run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running forward test:", run)
        run_straight(STRAIGHT_DISTANCE_MM, MEDIUM_SPEED)
        beep_ok()
        print("Record:")
        print("- stop position error")
        print("- left/right drift")
        print("- wobble or snaking")
        wait(1000)

    beep_done()

def reverse_repeatability_test():
    announce_test("Reverse Straight Repeatability")
    print("Goal: Check drift and stopping consistency while driving backward.")
    print("Run count:", REPEAT_RUNS)
    print("Distance:", STRAIGHT_DISTANCE_MM, "mm")

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot at launch line for REVERSE run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running reverse test:", run)
        run_straight(-STRAIGHT_DISTANCE_MM, MEDIUM_SPEED)
        beep_ok()
        print("Record:")
        print("- stop position error")
        print("- left/right drift")
        print("- reverse stability")
        wait(1000)

    beep_done()

def turn_90_test():
    announce_test("90 Degree Point Turn Test")
    print("Goal: Check heading accuracy and repeatability for 90-degree turns.")
    print("Run count:", REPEAT_RUNS)

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot at launch line for 90-degree turn run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running 90-degree turn test:", run)
        run_turn(90, 120)
        beep_ok()
        print("Record:")
        print("- overshoot / undershoot")
        print("- final heading")
        print("- skid or rocking")
        wait(1000)

    beep_done()

def turn_180_test():
    announce_test("180 Degree Point Turn Test")
    print("Goal: Check repeatability for larger in-place turns.")
    print("Run count:", REPEAT_RUNS)

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot at launch line for 180-degree turn run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running 180-degree turn test:", run)
        run_turn(180, 120)
        beep_ok()
        print("Record:")
        print("- overshoot / undershoot")
        print("- heading consistency")
        print("- wheel slip")
        wait(1000)

    beep_done()

def curve_test():
    announce_test("Curve Tracking Test")
    print("Goal: See whether robot follows a smooth arc consistently.")
    print("Run count:", REPEAT_RUNS)
    print("Radius:", CURVE_RADIUS_MM, "mm")
    print("Angle:", CURVE_ANGLE_DEG, "deg")

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot at launch line for CURVE run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running curve test:", run)
        run_curve(CURVE_RADIUS_MM, CURVE_ANGLE_DEG)
        beep_ok()
        print("Record:")
        print("- inside/outside drift")
        print("- smoothness")
        print("- stop consistency")
        wait(1000)

    beep_done()

def start_stop_stability_test():
    announce_test("Start-Stop Stability Test")
    print("Goal: Watch pitching, rocking, and attachment shake.")
    print("This test runs at 3 speeds: slow, medium, fast.")

    speeds = [("slow", SLOW_SPEED), ("medium", MEDIUM_SPEED), ("fast", FAST_SPEED)]

    for label, speed in speeds:
        wait_for_center_button(
            "Place robot for START-STOP test at {} speed.".format(label.upper())
        )
        reset_robot_state()
        print("Running start-stop test at", label, "speed")
        run_straight(START_STOP_DISTANCE_MM, speed)
        wait(300)
        run_straight(-START_STOP_DISTANCE_MM, speed)
        beep_ok()
        print("Record:")
        print("- front/rear rocking")
        print("- wheel slip on launch")
        print("- attachment shake")
        wait(1000)

    beep_done()

def push_traction_test():
    announce_test("Push / Traction Test")
    print("Goal: Compare grip while pushing a constant object.")
    print("Use the SAME object every time.")
    print("Suggested object: light test block or weighted sled.")
    print("Run count:", REPEAT_RUNS)

    for run in range(1, REPEAT_RUNS + 1):
        wait_for_center_button(
            "Place robot against test object for PUSH run {} of {}.".format(run, REPEAT_RUNS)
        )
        reset_robot_state()
        print("Running push test:", run)
        run_straight(PUSH_DISTANCE_MM, SLOW_SPEED)
        beep_ok()
        print("Record:")
        print("- did robot slip?")
        print("- did object move fully?")
        print("- did robot veer?")
        wait(1000)

    beep_done()

# ----------------------------
# Menus
# ----------------------------
def run_all_tests():
    forward_repeatability_test()
    reverse_repeatability_test()
    turn_90_test()
    turn_180_test()
    curve_test()
    start_stop_stability_test()
    push_traction_test()

def print_menu():
    print("")
    print("Hub Position Test Menu")
    print("1 - Forward straight repeatability")
    print("2 - Reverse straight repeatability")
    print("3 - 90-degree point turn")
    print("4 - 180-degree point turn")
    print("5 - Curve test")
    print("6 - Start-stop stability")
    print("7 - Push / traction")
    print("8 - Run all tests")
    print("9 - Exit")
    print("Use LEFT/RIGHT buttons to choose. Press CENTER to run.")

def choose_menu_option():
    option = 1
    while True:
        hub.display.number(option)
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            option -= 1
            if option < 1:
                option = 9
            wait(250)

        elif Button.RIGHT in pressed:
            option += 1
            if option > 9:
                option = 1
            wait(250)

        elif Button.CENTER in pressed:
            while Button.CENTER in hub.buttons.pressed():
                wait(10)
            return option

        wait(10)

def main():
    print("Hub Position Test Harness Ready.")
    print("Keep robot configuration constant except for HUB POSITION.")
    hub.speaker.beep()

    while True:
        print_menu()
        option = choose_menu_option()

        if option == 1:
            forward_repeatability_test()
        elif option == 2:
            reverse_repeatability_test()
        elif option == 3:
            turn_90_test()
        elif option == 4:
            turn_180_test()
        elif option == 5:
            curve_test()
        elif option == 6:
            start_stop_stability_test()
        elif option == 7:
            push_traction_test()
        elif option == 8:
            run_all_tests()
        elif option == 9:
            print("Exiting.")
            hub.display.text("BYE")
            break

        wait(500)

main()
