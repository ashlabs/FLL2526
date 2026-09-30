from Robot import Robot
import Robot_config

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To make the robot move forward, you can use a.f(distance).
# To make the robot move backward, you can use a.b(distance).
# To make the robot turn left, you can use a.l(angle).
# To make the robot turn right, you can use a.r(angle).
# To run the arms, use a.lp(position) and a.rp(position) to turn each arm to a specific position (lp for left and rp for right). The positions will be relative to the position of the arms when the run started.
# To reset an arm to the starting position, use a.l0() for the left arm and a.r0() for the right arm.
# The arms can also be moved to preset positions using a.lu() (left arm to the position set as a.leftArmUpPos), a.ru() (right arm to the position set as a.rightArmUpPos), a.ld() (left arm to the position set as a.leftArmDownPos), and a.rd() (right arm to the position set as a.rightArmDownPos).
# To access the robot's peripherals directly, use a.robot or robot.
# Running this file will execute the run directly.
# To access all runs with a selector on the robot, run Main.py.
# To access robot functions while not in this function, pass a.robot, robot, or a into the other function.
# Call a.robot.Base.use_gyro(True) to turn the gyro on and a.robot.Base.use_g_gyro(False) to turn it off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def runMain(robot: Robot):
	a = robot.QuickFunctions

	a.f(500)

	dropAndPush(robot)

	a.f(-500)


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