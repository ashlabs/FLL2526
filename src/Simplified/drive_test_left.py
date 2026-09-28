from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import Matrix, wait, StopWatch
from Robot import Robot

HUB = PrimeHub()

robot : Robot | None = None

def run_test(degrees : float | None = 90): # None is infinite
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	print("Running drive test")
	if robot.Base is not None:
		if degrees is None:
			robot.Base.drive(0, -robot.TurnSpeed)
		else:
			robot.Base.turn(-degrees, wait=False)
	print("Hold the right button down to exit")
	robot.MissionDone()
	while Button.RIGHT not in HUB.buttons.pressed():
		wait(10)
	print("Exiting...")
	while Button.RIGHT in HUB.buttons.pressed():
		wait(10)
	wait(500)

if __name__ == "__main__":
	LeftDrive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
	RightDrive = Motor(Port.B)
	robot = Robot(MainArm=Motor(Port.C), SecondArm=Motor(Port.D, Direction.COUNTERCLOCKWISE), Base=DriveBase(LeftDrive, RightDrive, wheel_diameter=56, axle_track=114), MatColorSensor=ColorSensor(Port.S1), LeftDrive=LeftDrive, RightDrive=RightDrive, DistSensor=UltrasonicSensor(Port.S2))
	run_test()