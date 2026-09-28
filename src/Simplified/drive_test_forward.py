from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import Matrix, wait, StopWatch
from Robot import Robot

HUB = PrimeHub()

robot : Robot | None = None

def run_test(cm : float | None = 10): # None = infinite
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	print("Running drive test")
	if robot.Base is not None:
		if cm is None:
			robot.Base.drive(robot.DriveSpeed, 0)
		else:
			robot.Base.straight(10 * cm, wait=False)
	print("Hold the right button down to exit")
	while Button.RIGHT not in HUB.buttons.pressed():
		wait(10)
	print("Exiting...")
	robot.MissionDone()
	while Button.RIGHT in HUB.buttons.pressed():
		wait(10)
	wait(500)

if __name__ == "__main__":
	LeftDrive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
	RightDrive = Motor(Port.B)
	robot = Robot(MainArm=Motor(Port.C), SecondArm=Motor(Port.D, Direction.COUNTERCLOCKWISE), Base=DriveBase(LeftDrive, RightDrive, wheel_diameter=56, axle_track=114), MatColorSensor=ColorSensor(Port.S1), LeftDrive=LeftDrive, RightDrive=RightDrive, DistSensor=UltrasonicSensor(Port.S2))
	run_test()