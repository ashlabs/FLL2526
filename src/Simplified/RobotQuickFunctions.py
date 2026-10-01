import Robot

class RobotQuickFunctions:
	robot : Robot.Robot
	leftArmUpPos : int = 90
	leftArmDownPos : int = -90
	rightArmUpPos : int = 90
	rightArmDownPos : int = -90

	def __init__(self, robot : Robot.Robot):
		self.robot = robot

	# Move forward by a specified amount
	def forward(self, distance : int):
		if self.robot.Base is not None:
			self.robot.Base.straight(distance)

	# Move backward by a specified amount
	def backward(self, distance : int):
		if self.robot.Base is not None:
			self.robot.Base.straight(-distance)

	# Turn left by a specified amount
	def left(self, angle : int):
		if self.robot.Base is not None:
			self.robot.Base.turn(-angle)

	# Turn right by a specified amount
	def right(self, angle : int):
		if self.robot.Base is not None:
			self.robot.Base.turn(angle)

	# Move the left arm to a specified position
	def SetLeftArm(self, pos: int):
		if self.robot.MainArm is not None:
			self.robot.MainArm.run_target(self.robot.ArmSpeed, pos)

	# Lift the left arm to the up position
	def LeftUp(self):
		self.SetLeftArm(self.leftArmUpPos)

	# Move the left arm to the default position
	def LeftDefault(self):
		self.SetLeftArm(0)
	
	# Lower the left arm to the down position
	def LeftDown(self):
		self.SetLeftArm(self.leftArmDownPos)

	# Move the right arm to a specified position
	def SetRightArm(self, pos: int):
		if self.robot.SecondArm is not None:
			self.robot.SecondArm.run_target(self.robot.ArmSpeed, pos)

	# Lift the right arm to the up position
	def RightUp(self):
		self.SetRightArm(self.rightArmUpPos)

	# Move the left arm to the default position
	def RightDefault(self):
		self.SetRightArm(0)

	# Lower the right arm to the down position
	def RightDown(self):
		self.SetRightArm(self.rightArmDownPos)