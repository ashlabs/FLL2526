from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait, Matrix

from Config import(Robot_config, Robot, BasicSelector)

def drop(robot : Robot.Robot):
	if robot.SecondArm is not None:
		robot.SecondArm.reset_angle(0)
		robot.SecondArm.run_target(500, -120)
		robot.SecondArm.run_target(100, 0)

def main(robot: Robot.Robot):
	drop(robot)

if __name__ == "__main__":
	main(Robot_config.prepare_robot_object())