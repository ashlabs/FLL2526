from Robot import Robot
import Robot_config
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
 
def run_arm_angle(arm, speed: int, delta_degrees: int, wait: bool = True):
    """Move an arm by a relative angle with a reliable fallback implementation."""
    if arm is None:
        raise ValueError("Cannot move a missing arm.")

    # Prefer the native API when it exists.
    if hasattr(arm, "run_angle"):
        try:
            arm.run_angle(speed, delta_degrees, wait=wait)
            return
        except TypeError:
            pass

    # Fallback for mock/abstract implementations without a real run_angle method.
    if hasattr(arm, "angle"):
        current_angle = arm.angle()
        target_angle = current_angle + delta_degrees
        arm.run_target(speed, target_angle, wait=wait)
        return

    raise AttributeError("The arm does not support relative angle movements.")


def runMain(robot: Robot):
    Actions = robot.QuickFunctions
   
    # Configure the robot to go slower (Adjust numbers as needed)
    # settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    # Pybricks default straight_speed is usually around 400-500 mm/s.
    #Change the straigth_speed

    
    # robot.MainArm.run_angle(500, -50)
    
    # Your movement actions will now run at the new slower speed
    # if robot.SecondArm is not None:
    #     robot.SecondArm.run_target(50, 45, wait=True)

 
    Actions.forward(880)
    robot.MainArm.run_angle(800, 200)

    # assert robot.SecondArm is not None
    # run_arm_angle(robot.SecondArm, 50, 45, wait=True)
    #Actions.right(45)
    #Actions.forward(490)
    #Actions.left(5)
    #Actions.forward(20)
    #Actions.left(65)
    #robot.Base.settings(
        # straight_speed=150,         # Slower linear speed (mm/s)
        # straight_acceleration=70,  # Slower acceleration (mm/s²)
        # turn_rate=150,              # Slower turning speed (deg/s)
    #     turn_acceleration=125       # Slower turning acceleration (deg/s²)
    # )
    #Actions.backward(300)
    #Actions.forward(20)
    #Actions.forward(75)
    #Actions.left(90)
    #robot.Base.settings(
    #     straight_speed=560,         # Slower linear speed (mm/s)
    #     straight_acceleration=120,  # Slower acceleration (mm/s²)
    #     turn_rate=150,              # Slower turning speed (deg/s)
    #     turn_acceleration=125       # Slower turning acceleration (deg/s²)
    # )
    #Actions.forward(620)
    #Actions.left(170)
    #Actions.forward(250)
    #Actions.right(45)
    #Actions.SetRightArm(20)
   
if __name__ == "__main__":
    runMain(Robot_config.prepare_robot_object())
 
 
