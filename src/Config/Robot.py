from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait, StopWatch, Matrix

print("Robot class ready")

class Robot:
	MainArm : Motor | None = None
	SecondArm : Motor | None = None
	ArmSpeed : int = 0
	LeftDrive : Motor | None = None
	RightDrive : Motor | None = None
	Base : DriveBase | None = None
	DriveSpeed : int = 0
	DriveAcceleration : int = 0
	TurnSpeed : int = 0
	TurnAcceleration : int = 0
	DriveGyroEnabled : bool = False
	MatColorSensor : ColorSensor | None = None
	DistSensor : UltrasonicSensor | None = None
	MissionTimer : StopWatch = StopWatch()
	hub = PrimeHub()

	def __init__(self, MainArm:Motor | None, SecondArm:Motor | None, Base:DriveBase | None, MatColorSensor:ColorSensor | None, LeftDrive:Motor | None, RightDrive:Motor | None, DistSensor: UltrasonicSensor | None):
		self.MainArm = MainArm
		self.SecondArm = SecondArm
		self.Base = Base
		self.LeftDrive = LeftDrive
		self.RightDrive = RightDrive
		self.MatColorSensor = MatColorSensor
		self.DistSensor = DistSensor

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

	def MissionDone(self):
		self.hub.display.icon(Matrix([
				[0, 0, 0, 0, 255],
				[0, 0, 0, 255, 0],
				[255, 0, 255, 0, 0],
				[0, 255, 0, 0, 0],
				[0, 0, 0, 0, 0]]))
		self.hub.light.on(Color.GREEN)
		self.MissionTimer.pause()