from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Robot import Robot
from BasicSelector import BasicSelector as Selector
import arm_up_down_test, hold_test, motor_alignment_test, drive_test_forward, drive_test_backward, drive_test_left, drive_test_right, Robot_config, TestsMain

def run(robot : Robot):
	selector = Selector(["~", "F", "B", "L", "R", "A", "H", "M", "+"])
	while True:
		robot.reset()
		selectedTest = selector.selectNext()
		if selectedTest == "~":
			print("Exiting...")
			return
		elif selectedTest == "F":
			print("Drive forward test selected")
			drive_test_forward.robot = robot
			drive_test_forward.run_test(100)
		elif selectedTest == "B":
			print("Drive backward test selected")
			drive_test_backward.robot = robot
			drive_test_backward.run_test(100)
		elif selectedTest == "L":
			print("Drive left test selected")
			drive_test_left.robot = robot
			drive_test_left.run_test(90)
		elif selectedTest == "R":
			print("Drive right test selected")
			drive_test_right.robot = robot
			drive_test_right.run_test(90)
		elif selectedTest == "A":
			print("Arm up and down test selected")
			arm_up_down_test.Arm1 = Robot.MainArm
			arm_up_down_test.Arm2 = Robot.SecondArm
			arm_up_down_test.run_test(100)
		elif selectedTest == "H":
			print("Hold test selected")
			hold_test.robot = robot
			hold_test.run_test()
		elif selectedTest == "M":
			print("Motor alignment test selected")
			motor_alignment_test.robot = robot
			motor_alignment_test.run_test()
		elif selectedTest == "+":
			print("Full tests menu selected")
			TestsMain.robot = robot
			TestsMain.main()