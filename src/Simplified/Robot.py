from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Color
from pybricks.tools import wait, StopWatch, Matrix

from RobotQuickFunctions import RobotQuickFunctions

print("Robot class ready")

class Robot:
	MainArm : Motor | None = None
	SecondArm : Motor | None = None
	ArmSpeed : int = 50
	LeftDrive : Motor | None = None
	RightDrive : Motor | None = None
	Base : DriveBase | None = None
	DriveSpeed : int = 100
	DriveAcceleration : int = 150
	TurnSpeed : int = 100
	TurnAcceleration : int = 300
	DriveGyroEnabled : bool = False
	MatColorSensor : ColorSensor | None = None
	DistSensor : UltrasonicSensor | None = None
	MissionTimer : StopWatch = StopWatch()
	hub = PrimeHub()
	QuickFunctions : RobotQuickFunctions

	def __init__(self, MainArm:Motor | None, SecondArm:Motor | None, Base:DriveBase | None, MatColorSensor:ColorSensor | None, LeftDrive:Motor | None, RightDrive:Motor | None, DistSensor: UltrasonicSensor | None):
		self.MainArm = MainArm
		self.SecondArm = SecondArm
		self.Base = Base
		self.LeftDrive = LeftDrive
		self.RightDrive = RightDrive
		self.MatColorSensor = MatColorSensor
		self.DistSensor = DistSensor
		self.QuickFunctions = RobotQuickFunctions(self)

	def reset(self):
		if self.MainArm is not None:
			self.MainArm.reset_angle(0)
		if self.SecondArm is not None:
			self.SecondArm.reset_angle(0)
		if self.Base is not None:
			self.Base.use_gyro(False)
			self.Base.reset()
		else:
			if self.LeftDrive is not None:
				self.LeftDrive.reset_angle(0)
			if self.RightDrive is not None:
				self.RightDrive.reset_angle(0)
		self.hub.imu.reset_heading(0)
		if self.MatColorSensor is not None:
			self.MatColorSensor.lights.off()
		if self.DistSensor is not None:
			self.DistSensor.lights.off()
		self.hub.light.off()
		self.hub.display.off()
		self.hub.system.set_stop_button(Button.CENTER)
		self.setSpeed(100)
		self.setArmSpeed(50)
		self.setAcceleration(150)

	def MissionDone(self):
		self.hub.display.icon(Matrix([
				[0, 0, 0, 0, 255],
				[0, 0, 0, 255, 0],
				[255, 0, 255, 0, 0],
				[0, 255, 0, 0, 0],
				[0, 0, 0, 0, 0]]))
		self.hub.light.on(Color.GREEN)
		self.MissionTimer.pause()

	def runCountdown(self, length : int = 5, warning : int = 3):
		self.hub.light.on(Color.YELLOW)
		for i in range(length, 0, -1):
			self.hub.display.number(i)
			print(f"Running in {i} (Total {length}, Warning {warning})")
			if i == warning:
				self.hub.light.on(Color.ORANGE)
			wait(1000)
		self.hub.light.on(Color.GREEN)

	def getSpeed(self) -> int:
		return self.DriveSpeed

	def setSpeed(self, speed: int):
		self.DriveSpeed = speed
		if self.Base is not None:
			self.Base.settings(straight_speed=speed, straight_acceleration=self.DriveAcceleration, turn_rate=self.TurnSpeed, turn_acceleration=self.TurnAcceleration)

	def getArmSpeed(self) -> int:
		return self.ArmSpeed

	def setArmSpeed(self, speed: int):
		self.ArmSpeed = speed

	def getAcceleration(self) -> int:
		return self.DriveAcceleration

	def setAcceleration(self, acc: int):
		self.DriveAcceleration = acc
		if self.Base is not None:
			self.Base.settings(straight_speed=self.DriveSpeed, straight_acceleration=acc, turn_rate=self.TurnSpeed, turn_acceleration=self.TurnAcceleration)