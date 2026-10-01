from Robot import Robot
import Robot_config

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To make the robot move forward, you can use Actions.forward(distance).
# To make the robot move backward, you can use Actions.backward(distance).
# To make the robot turn left, you can use Actions.l(angle).
# To make the robot turn right, you can use Actions.r(angle).
# To run the arms, use Actions.lp(position) and Actions.rp(position) to turn each arm to Actions specific position (lp for left and rp for right). The positions will be relative to the position of the arms when the run started.
# To reset an arm to the starting position, use Actions.l0() for the left arm and Actions.r0() for the right arm.
# The arms can also be moved to preset positions using Actions.lu() (left arm to the position set as Actions.leftArmUpPos), Actions.ru() (right arm to the position set as Actions.rightArmUpPos), Actions.ld() (left arm to the position set as Actions.leftArmDownPos), and Actions.rd() (right arm to the position set as Actions.rightArmDownPos).
# To access the robot's peripherals directly, use Actions.robot or robot.
# Running this file will execute the run directly.
# To access all runs with Actions selector on the robot, run Main.py.
# To access robot functions while not in this function, pass Actions.robot, robot, or Actions into the other function.
# Call Actions.robot.Base.use_gyro(True) to turn the gyro on and Actions.robot.Base.use_gyro(False) to turn it off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def runMain(robot: Robot):
	Actions = robot.QuickFunctions

	Actions.forward(500)

	dropAndPush(robot)

	Actions.forward(-500)


def dropAndPush(robot : Robot):
	if robot.SecondArm is not None:
		robot.SecondArm.reset_angle(0)
		robot.SecondArm.run_target(500, -120)
		if robot.MainArm is not None:
			robot.MainArm.run_angle(200, -360)
			robot.MainArm.run_angle(200, 360)
		robot.SecondArm.run_target(100, 0)

if __name__ == "__main__":
	runMain(Robot_config.prepare_robot_object())