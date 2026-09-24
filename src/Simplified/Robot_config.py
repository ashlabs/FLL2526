from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Robot import Robot
from BasicSelector import BasicSelector as Selector

config_selector : Selector = Selector([
	1,
	2,
	3,
	4,
	"p"
])

def prepare_robot_object() -> Robot:
	selected_config = config_selector.selectNext()
	if (selected_config == 1):
		return config_1()
	elif (selected_config == 2):
		return config_2()
	elif (selected_config == 3):
		return config_3()
	elif (selected_config == 4):
		return config_4()
	elif (selected_config == "p"):
		import Ports as _
		return BlankRobot()
	else:
		raise RuntimeError("Couldn't find specified config")

def config_1() -> Robot:
	# Used by:
	# 	Rishi/Raj pre-season V2 (Calibrated to this design on 7/29/2026)
	LeftDrive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
	RightDrive = Motor(Port.B)
	return Robot(MainArm=Motor(Port.C), SecondArm=Motor(Port.D, Direction.COUNTERCLOCKWISE), Base=DriveBase(LeftDrive, RightDrive, wheel_diameter=56, axle_track=128), MatColorSensor=ColorSensor(Port.E), LeftDrive=LeftDrive, RightDrive=RightDrive, DistSensor=UltrasonicSensor(Port.F))

def config_2() -> Robot:
	# Used by:
	# 	Elephant main (post merge 1) - V2 (Not calibrated)
	return config_basic(leftPort = Port.A, leftDir = Direction.CLOCKWISE, rightPort = Port.B, rightDir = Direction.COUNTERCLOCKWISE, wheelDiam = 56, AxTrack = 128, MainArmPort = Port.C, MainArmDir = Direction.CLOCKWISE, SecondArmPort = Port.D, SecondArmDir = Direction.COUNTERCLOCKWISE)

def config_3() -> Robot:
	# Used by:
	# 	Dinosaur main (post merge 1) - V2 (Not calibrated)
	return config_basic(leftPort = Port.A, leftDir = Direction.CLOCKWISE, rightPort = Port.B, rightDir = Direction.COUNTERCLOCKWISE, wheelDiam = 56, AxTrack = 128, MainArmPort = Port.C, MainArmDir = Direction.CLOCKWISE, SecondArmPort = Port.D, SecondArmDir = Direction.COUNTERCLOCKWISE)

def config_4() -> Robot:
	# Used by:
	# 	Egg main (post merge 1) - V2 (Not calibrated)
	return config_basic(leftPort = Port.A, leftDir = Direction.CLOCKWISE, rightPort = Port.B, rightDir = Direction.COUNTERCLOCKWISE, wheelDiam = 56, AxTrack = 128, MainArmPort = Port.C, MainArmDir = Direction.CLOCKWISE, SecondArmPort = Port.D, SecondArmDir = Direction.COUNTERCLOCKWISE)

def config_basic(leftPort : Port | None = None, leftDir : Direction | None = None, rightPort : Port | None = None, rightDir : Direction | None = None, wheelDiam : int | None = None, AxTrack : int | None = None, MainArmPort : Port | None = None, MainArmDir : Direction | None = None, SecondArmPort : Port | None = None, SecondArmDir : Direction | None = None, MatColorSensorPort : Port | None = None, DistSensorPort : Port | None = None) -> Robot:
	if type(leftPort) is Port and type(leftDir) is Direction:
		try:
			LeftDrive = Motor(leftPort, leftDir)
			print(f"Left drive motor found on {leftPort} (direction: {leftDir}")
		except OSError as e:
			print(f"Left drive motor not found on Port {leftPort}, skipping motor creation")
			print(f"Check connections and make sure the motor is attached to Port {leftPort} (error: {e})")
			LeftDrive = None
		except Exception as e:
			print(f"Unexpected error while creating left drive motor on Port {leftPort}: {e}")
			LeftDrive = None
	else:
		print("Not setting up the left drive motor because the port or direction is not provided")
		LeftDrive = None

	if type(rightPort) is Port and type(rightDir) is Direction:
		try:
			RightDrive = Motor(rightPort, rightDir)
			print(f"Right drive motor found on Port {rightPort} (direction: {rightDir})")
		except OSError as e:
			print(f"Right drive motor not found on Port {rightPort}, skipping motor creation")
			print(f"Check connections and make sure the motor is attached to Port {rightPort} (error: {e})")
			RightDrive = None
		except Exception as e:
			print(f"Unexpected error while creating right drive motor on Port {rightPort}: {e}")
			RightDrive = None
	else:
		print("Not setting up the right drive motor because the port or direction is not provided")
		RightDrive = None

	if (type(LeftDrive) is Motor and type(RightDrive) is Motor and type(wheelDiam) is int and type(AxTrack) is int):
		print("Drive motors found, creating drive base")
		try:
			Base = DriveBase(LeftDrive, RightDrive, wheel_diameter=wheelDiam, axle_track=AxTrack)
			print(f"Drive base created successfully (wd = {wheelDiam}, at = {AxTrack})")
		except Exception as e:
			print(f"Failed to create drive base (Error: {e})")
			Base = None
	else:
		print("Drive motors or base settings not found, not creating drive base")
		Base = None

	if type(MainArmPort) is Port and type(MainArmDir) is Direction:
		try:
			MainArm = Motor(MainArmPort, MainArmDir)
			print(f"Main arm motor found on Port {MainArmPort} (direction: {MainArmDir})")
		except OSError as e:
			print(f"Main arm motor not found on Port {MainArmPort}, skipping motor creation")
			print(f"Check connections and make sure the motor is attached to Port {MainArmPort} (error: {e})")
			MainArm = None
		except Exception as e:
			print(f"Unexpected error while creating the main arm on Port {MainArmPort}: {e}")
			MainArm = None
	else:
		print("Not setting up the main arm motor because the port or direction is not provided")
		MainArm = None

	if type(SecondArmPort) is Port and type(SecondArmDir) is Direction:
		try:
			SecondArm = Motor(SecondArmPort, SecondArmDir)
			print(f"Second arm motor found on Port {SecondArmPort} (direction: {SecondArmDir})")
		except OSError as e:
			print(f"Second arm motor not found on Port {SecondArmPort}, skipping motor creation")
			print(f"Check connections and make sure the motor is attached to Port {SecondArmPort} (error: {e})")
			SecondArm = None
		except Exception as e:
			print(f"Unexpected error while creating the secondary arm on Port {SecondArmPort}: {e}")
			SecondArm = None
	else:
		print("Not setting up the second arm motor because the port or direction is not provided")
		SecondArm = None

	if type(MatColorSensorPort) is Port:
		try:
			MatColorSensor = ColorSensor(MatColorSensorPort)
			print(f"Mat-facing color sensor found on {MatColorSensorPort}")
		except OSError as e:
			print(f"Mat-facing color sensor not found on Port {MatColorSensorPort} (error: {e})")
			print(f"Check connections and make sure the sensor is attached to Port {MatColorSensorPort}")
			MatColorSensor = None
		except Exception as e:
			print(f"Unexpected error while creating the mat-facing color sensor on Port {MatColorSensorPort}: {e}")
			MatColorSensor = None
	else:
		print("Not setting up the mat-facing color sensor because the port is not provided")
		MatColorSensor = None

	if type(DistSensorPort) is Port:
		try:
			DistSensor = UltrasonicSensor(DistSensorPort)
			print(f"Ultrasonic distance sensor found on Port {DistSensorPort}")
		except OSError as e:
			print(f"Ultrasonic distance sensor not found on Port {Port.F} (error: {e})")
			print(f"Check connections and make sure the sensor is attached to Port {Port.F}")
			DistSensor = None
		except Exception as e:
			print(f"Unexpected error while creating the distance sensor on Port {DistSensorPort}: {e}")
			DistSensor = None
	else:
		print("Not setting up the distance sensor because the port is not provided")
		DistSensor = None

	return Robot(MainArm=MainArm, SecondArm=SecondArm, Base=Base, MatColorSensor=MatColorSensor, LeftDrive=LeftDrive, RightDrive=RightDrive, DistSensor=DistSensor)

def BlankRobot() -> Robot:
	return Robot(MainArm=None, SecondArm=None, Base=None, MatColorSensor=None, LeftDrive=None, RightDrive=None, DistSensor=None)