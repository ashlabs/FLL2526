from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import Matrix, wait, StopWatch
from Robot import Robot

HUB = PrimeHub()

robot : Robot | None = None

def run_test():
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	print("Running motor alignment test")
	if robot.MainArm is not None:
		robot.MainArm.reset_angle(None)
		robot.MainArm.run_target(robot.ArmSpeed, 0, then=Stop.HOLD)
	if robot.SecondArm is not None:
		robot.SecondArm.reset_angle(None)
		robot.SecondArm.run_target(robot.ArmSpeed, 0, then=Stop.HOLD)
	if robot.Base is not None:
		robot.Base.use_gyro(False) # Prevent gyro from affecting independent motor movement
		robot.Base.reset()
	if robot.LeftDrive is not None:
		robot.LeftDrive.reset_angle(None)
		robot.LeftDrive.run_target(robot.DriveSpeed, 0, then=Stop.HOLD)
	if robot.RightDrive is not None:
		robot.RightDrive.reset_angle(None)
		robot.RightDrive.run_target(robot.DriveSpeed, 0, then=Stop.HOLD)
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