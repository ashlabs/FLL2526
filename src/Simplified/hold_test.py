from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Robot import Robot

HUB = PrimeHub()

robot : Robot | None = None

def run_test():
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	print("Running hold test")
	if robot.MainArm is not None:
		robot.MainArm.hold()
	if robot.SecondArm is not None:
		robot.SecondArm.hold()
	if robot.LeftDrive is not None:
		robot.LeftDrive.hold()
	if robot.RightDrive is not None:
		robot.RightDrive.hold()
	print("Hold the right button down to exit")
	robot.MissionDone()
	while Button.RIGHT not in HUB.buttons.pressed():
		wait(10)
	print("Exiting...")
	while Button.RIGHT in HUB.buttons.pressed():
		wait(10)
	wait(500)

if __name__ == "__main__":
	LeftDrive = Motor(Port.A)
	RightDrive = Motor(Port.B, Direction.COUNTERCLOCKWISE)
	robot = Robot(MainArm=Motor(Port.C), SecondArm=Motor(Port.D, Direction.COUNTERCLOCKWISE), Base=DriveBase(LeftDrive, RightDrive, wheel_diameter=56, axle_track=114), MatColorSensor=ColorSensor(Port.S1), LeftDrive=LeftDrive, RightDrive=RightDrive, DistSensor=UltrasonicSensor(Port.S2))
	run_test()