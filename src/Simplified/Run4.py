from Robot import Robot
import Robot_config

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