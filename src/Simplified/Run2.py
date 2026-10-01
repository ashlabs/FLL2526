from Robot import Robot
import Robot_config

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To make the robot move forward, you can use Actions.forward(distance).
# To make the robot move backward, you can use Actions.backward(distance).
# To make the robot turn left, you can use Actions.left(angle).
# To make the robot turn right, you can use Actions.right(angle).
# To run the arms, use Actions.SetLeftArm(position) and Actions.SetRightArm(position).
# To reset an arm to the starting position, use Actions.LeftDefault() for the left arm and Actions.RightDefault() for the right arm.
# The arms can also be moved to preset positions using Actions.LeftUp() (left arm to the position set as Actions.leftArmUpPos), Actions.RightUp() (right arm to the position set as Actions.rightArmUpPos), Actions.LeftDown() (left arm to the position set as Actions.leftArmDownPos), and Actions.RightDown() (right arm to the position set as Actions.rightArmDownPos).
# To access the robot's peripherals directly, use Actions.robot or robot.
# Running this file will execute the run directly.
# To access all runs with Actions selector on the robot, run Main.py.
# To access robot functions while not in this function, pass Actions.robot, robot, or Actions into the other function.
# Call Actions.robot.Base.use_gyro(True) to turn the gyro on and Actions.robot.Base.use_gyro(False) to turn it off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def runMain(robot: Robot):
	Actions = robot.QuickFunctions

	# Put your code here
	Actions.forward(1000)
	Actions.backward(350)
	Actions.left(90)
	Actions.backward(200)
	Actions.right(90)
	#Actions.forward(400)
	#Actions.right(50)
if __name__ == "__main__":
	runMain(Robot_config.prepare_robot_object())