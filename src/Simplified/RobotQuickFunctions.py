from Robot import Robot

class RobotQuickFunctions:
	robot : Robot
	leftArmUpPos : int = 90
	leftArmDownPos : int = -90
	rightArmUpPos : int = 90
	rightArmDownPos : int = -90

	def __init__(self, robot : Robot):
		self.robot = robot

	# Move forwaqrd by a specified amount
	def f(self, distance : int):
		if self.robot.Base is not None:
			self.robot.Base.straight(distance)

	# Move backward by a specified amount
	def b(self, distance : int):
		if self.robot.Base is not None:
			self.robot.Base.straight(-distance)

	# Turn left by a specified amount
	def l(self, angle : int):
		if self.robot.Base is not None:
			self.robot.Base.turn(-angle)

	# Turn right by a specified amount
	def r(self, angle : int):
		if self.robot.Base is not None:
			self.robot.Base.turn(angle)

	# Move the left arm to a specified position
	def lp(self, pos: int):
		if self.robot.MainArm is not None:
			self.robot.MainArm.run_target(self.robot.ArmSpeed, pos)

	# Lift the left arm to the up position
	def lu(self):
		self.lp(self.leftArmUpPos)

	# Move the left arm to the default position
	def l0(self):
		self.lp(0)
	
	# Lower the left arm to the down position
	def ld(self):
		self.lp(self.leftArmDownPos)

	# Move the right arm to a specified position
	def rp(self, pos: int):
		if self.robot.SecondArm is not None:
			self.robot.SecondArm.run_target(self.robot.ArmSpeed, pos)

	# Lift the right arm to the up position
	def ru(self):
		self.rp(self.rightArmUpPos)

	# Move the left arm to the default position
	def r0(self):
		self.rp(0)

	# Lower the right arm to the down position
	def rd(self):
		self.rp(self.rightArmDownPos)