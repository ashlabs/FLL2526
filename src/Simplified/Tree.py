from Robot import Robot
import Robot_config
import Sounds
from pybricks.tools import wait

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
	robot.reset()
	Actions = robot.QuickFunctions

	if robot.Base is not None:
		robot.Base.use_gyro(True)

	# Launched with: 45 degree jig

	# Drive to mission
	Sounds.play_waypoint_ding_dong()
	Actions.forward(100)
	Sounds.play_waypoint_ding_dong()
	Actions.left(14)
	Sounds.play_waypoint_ding_dong()
	Actions.forward(750)
	Sounds.play_waypoint_ding_dong()
	Actions.left(28)
	Sounds.play_waypoint_ding_dong()
	Actions.forward(108)
	Sounds.play_waypoint_ding_dong()

	# Do mission

	Sounds.play_waypoint_ding_dong()
	if robot.MainArm is not None and robot.SecondArm is not None:
		robot.MainArm.run_target(50, 75, wait=False)
		robot.SecondArm.run_target(50, 75, wait=True)

	# Sounds.play_waypoint_ding_dong()
	# robot.runCountdown(length=1, warning=1)

	# Sounds.play_waypoint_ding_dong()
	# Actions.backward(160)
	
	# Sounds.play_waypoint_ding_dong()
	# if robot.MainArm is not None and robot.SecondArm is not None:
	# 	robot.MainArm.run_target(50, 0, wait=False)
	# 	robot.SecondArm.run_target(50, 0, wait=True)

	robot.reset()
	wait(100)

	# Go back
	
	# Sounds.play_waypoint_ding_dong()
	# Actions.right(30)
	# Sounds.play_waypoint_ding_dong()
	# Actions.backward(700)
	# Sounds.play_waypoint_ding_dong()
	

if __name__ == "__main__":
	runMain(Robot_config.prepare_robot_object())