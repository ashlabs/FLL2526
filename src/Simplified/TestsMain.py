from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Robot import Robot
from BasicSelector import BasicSelector as Selector
import arm_up_down_test, hold_test, motor_alignment_test, drive_test_forward, drive_test_backward, drive_test_left, drive_test_right, Robot_config

robot : Robot | None = None

hub = PrimeHub()

selector : Selector = Selector([
	"~", # Exit
	"S", # Settings menu
	"A", # Arm up-down test
	"H", # Hold all motors test
	"M", # Motor alignment test
	"D", # Drive test (variant selector)
	"P", # Preset tests menu
])

settingsSelector : Selector = Selector([
	"~", # Exit
	"A", # Arm speed selection
	"D", # Drive speed selection
	"d", # Drive acceleration selection
	"T", # Turn speed selection
	"t", # Turn acceleration selection
	"G", # Use gyro for driving
	"L", # Drive distance selection
])

driveTestSelector : Selector = Selector([
	"~", # Exit
	"d", # Distance selection
	"F", # Drive forward test
	"B", # Drive backward test
	"L", # Drive left test
	"R", # Drive right test
])

PresetTestSelector : Selector = Selector([
	"~", # Exit
	"F50-200", # Drive forward 50cm at a speed of 200
	"F50-500", # Drive forward 50cm at a speed of 500
	"B50-200", # Drive backward 50cm at a speed of 200
	"B50-500", # Drive backward 50cm at a speed of 500
	"F50-200G", # Drive forward 50cm at a speed of 200 (with gyro)
	"F50-500G", # Drive forward 50cm at a speed of 500 (with gyro)
	"B50-200G", # Drive backward 50cm at a speed of 200 (with gyro)
	"B50-500G", # Drive backward 50cm at a speed of 500 (with gyro)
])

driveLengthSelector : Selector = Selector([
	0, # 0 cm / 0 deg
	5, # 5 cm / 45 deg
	10, # 10 cm / 90 deg
	50, # 50 cm / 180 deg
	"m", # 1 m / 360 deg
	"i", # infinite
], defaultIndex=3)

armspeedselector = Selector([0, 50, 200, 500, 700, 1000], defaultIndex=3, displayMultiplier=0.1) # Put options in here for arm speeds here
drivespeedselector = Selector([0, 50, 100, 200, 300, 400, 500], defaultIndex=3, displayMultiplier=0.1) # Put options in here for drive speeds here
driveaccelerationselector = Selector([0, 200, 400, 700, 1000, 2000], defaultIndex=3, displayMultiplier=0.05) # Put options in here for drive accelerations here
turnspeedselector = Selector([0, 50, 100, 150, 200, 250], defaultIndex=3, displayMultiplier=0.1) # Put options in here for turn speeds here
turnaccelerationselector = Selector([0, 100, 300, 700, 1000, 1500], defaultIndex=3, displayMultiplier=0.05) # Put options in here for turn accelerations here
gyroselector = Selector([False, True], defaultIndex=0)

def main():
	global robot, selector
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	else:
		while True:
			postRunReset()
			selectedTest = selector.selectNext()
			if selectedTest == "~":
				print("Exiting...")
				return
			elif selectedTest == "S":
				print("Settings selected")
				startSettingsMenu()
			elif selectedTest == "A":
				print("Arm test selected")
				preRunSetup()
				arm_up_down_test.Arm1 = robot.MainArm
				arm_up_down_test.Arm2 = robot.SecondArm
				arm_up_down_test.run_test()
			elif selectedTest == "H":
				print("Hold test selected")
				preRunSetup()
				hold_test.robot = robot
				hold_test.run_test()
			elif selectedTest == "M":
				print("Motor alignment test selected")
				preRunSetup()
				motor_alignment_test.robot = robot
				motor_alignment_test.run_test()
			elif selectedTest == "D":
				print("Drive test selected")
				driveTestMenu()
			elif selectedTest == "P":
				print("Preset tests selected")
				presetTestMenu()


def driveTestMenu():
	global robot, driveTestSelector
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	else:
		while True:
			postRunReset()
			selectedDriveTest = driveTestSelector.selectNext()
			if selectedDriveTest == "~":
				print("Exiting drive test menu...")
				return
			elif selectedDriveTest == "F":
				print("Drive forward test selected")
				preRunSetup()
				drive_test_forward.robot = robot
				if isinstance(driveLengthSelector.selectedOption, int):
					drive_test_forward.run_test(100)
				elif driveLengthSelector.selectedOption == "m":
					drive_test_forward.run_test(100)
				else:
					drive_test_forward.run_test(None)
			elif selectedDriveTest == "B":
				print("Drive backward test selected")
				preRunSetup()
				drive_test_backward.robot = robot
				if isinstance(driveLengthSelector.selectedOption, int):
					drive_test_backward.run_test(100)
				elif driveLengthSelector.selectedOption == "m":
					drive_test_backward.run_test(100)
				else:
					drive_test_backward.run_test(None)
			elif selectedDriveTest == "L":
				print("Drive left test selected")
				preRunSetup()
				drive_test_left.robot = robot
				if driveLengthSelector.selectedOption == 0:
					drive_test_left.run_test(0)
				elif driveLengthSelector.selectedOption == 5:
					drive_test_left.run_test(45)
				elif driveLengthSelector.selectedOption == 10:
					drive_test_left.run_test(90)
				elif driveLengthSelector.selectedOption == 50:
					drive_test_left.run_test(180)
				elif driveLengthSelector.selectedOption == "m":
					drive_test_left.run_test(360)
				else:
					drive_test_left.run_test(None)
			elif selectedDriveTest == "R":
				print("Drive right test selected")
				preRunSetup()
				drive_test_right.robot = robot
				if driveLengthSelector.selectedOption == 0:
					drive_test_right.run_test(0)
				elif driveLengthSelector.selectedOption == 5:
					drive_test_right.run_test(45)
				elif driveLengthSelector.selectedOption == 10:
					drive_test_right.run_test(90)
				elif driveLengthSelector.selectedOption == 50:
					drive_test_right.run_test(180)
				elif driveLengthSelector.selectedOption == "m":
					drive_test_right.run_test(360)
				else:
					drive_test_right.run_test(None)
			elif selectedDriveTest == "d":
				print("Drive distance selected")
				driveDistanceMenu()


def presetTestMenu():
	global robot, PresetTestSelector
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	else:
		while True:
			postRunReset()
			selectedPresetTest = PresetTestSelector.selectNext()
			if selectedPresetTest == "~":
				print("Exiting preset test menu...")
				return
			elif selectedPresetTest == "F50-200":
				print("Drive forward 50 cm at speed 200 test selected")
				preRunSetup()
				robot.DriveSpeed = 200
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = False
				drive_test_forward.robot = robot
				drive_test_forward.run_test(50)
			elif selectedPresetTest == "F50-500":
				print("Drive forward 50 cm at speed 500 test selected")
				preRunSetup()
				robot.DriveSpeed = 500
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = False
				drive_test_forward.robot = robot
				drive_test_forward.run_test(50)
			elif selectedPresetTest == "B50-200":
				print("Drive backward 50 cm at speed 200 test selected")
				preRunSetup()
				robot.DriveSpeed = 200
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = False
				drive_test_backward.robot = robot
				drive_test_backward.run_test(50)
			elif selectedPresetTest == "B50-500":
				print("Drive backward 50 cm at speed 500 test selected")
				preRunSetup()
				robot.DriveSpeed = 500
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = False
				drive_test_backward.robot = robot
				drive_test_backward.run_test(50)
			elif selectedPresetTest == "F50-200G":
				print("Drive forward 50 cm at speed 200 (gyro on) test selected")
				preRunSetup()
				robot.DriveSpeed = 200
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = True
				drive_test_forward.robot = robot
				drive_test_forward.run_test(50)
			elif selectedPresetTest == "F50-500G":
				print("Drive forward 50 cm at speed 500 (gyro on) test selected")
				preRunSetup()
				robot.DriveSpeed = 500
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = True
				drive_test_forward.robot = robot
				drive_test_forward.run_test(50)
			elif selectedPresetTest == "B50-200G":
				print("Drive backward 50 cm at speed 200 (gyro on) test selected")
				preRunSetup()
				robot.DriveSpeed = 200
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = True
				drive_test_backward.robot = robot
				drive_test_backward.run_test(50)
			elif selectedPresetTest == "B50-500G":
				print("Drive backward 50 cm at speed 500 (gyro on) test selected")
				preRunSetup()
				robot.DriveSpeed = 500
				robot.DriveAcceleration = 700
				robot.TurnSpeed = 150
				robot.TurnAcceleration = 700
				robot.DriveGyroEnabled = True
				drive_test_backward.robot = robot
				drive_test_backward.run_test(50)


def driveDistanceMenu():
	print("Drive distance selection")
	DriveLength = driveLengthSelector.selectNext()
	print(f"Selected drive length: {DriveLength}")


def preRunSetup():
	global robot
	print("Setting up robot")
	try:
		if robot is None:
			raise Exception("Robot not initialized")
		else:
			# runCountdown(3, 1)
			robot.reset()
			print("Robot reset complete")
			if robot.Base is not None:
				print(f"Setting up drivetrain. Speed: {robot.DriveSpeed}, Acceleration: {robot.DriveAcceleration}, Turn Speed: {robot.TurnSpeed}, Turn Acceleration: {robot.TurnAcceleration}, Gyro Enabled: {robot.DriveGyroEnabled}")
				if drivespeedselector.selectedOption is int:
					robot.DriveSpeed = drivespeedselector.selectedOption
				if driveaccelerationselector.selectedOption is int:
					robot.DriveAcceleration = driveaccelerationselector.selectedOption
				if turnspeedselector.selectedOption is int:
					robot.TurnSpeed = turnspeedselector.selectedOption
				if turnaccelerationselector.selectedOption is int:
					robot.TurnAcceleration = turnaccelerationselector.selectedOption
				if gyroselector.selectedOption is bool:
					robot.DriveGyroEnabled = gyroselector.selectedOption
				robot.Base.settings(robot.DriveSpeed, robot.DriveAcceleration, robot.TurnSpeed, robot.TurnAcceleration)
				robot.Base.use_gyro(robot.DriveGyroEnabled)
				print(f"Drivetrain setup complete. Speed: {robot.DriveSpeed}, Acceleration: {robot.DriveAcceleration}, Turn Speed: {robot.TurnSpeed}, Turn Acceleration: {robot.TurnAcceleration}, Gyro Enabled: {robot.DriveGyroEnabled}")
				robot.MissionTimer.reset()
				robot.MissionTimer.resume()
				print("Test timer started")
	except Exception as e:
		print(f"Error occurred: {e}")


def runCountdown(length : int = 5, warning : int = 3):
	hub.light.on(Color.YELLOW)
	for i in range(length, 0, -1):
		hub.display.number(i)
		print(f"Running in {i} (Total {length}, Warning {warning})")
		if i == warning:
			hub.light.on(Color.ORANGE)
		wait(1000)
	hub.light.on(Color.WHITE)


def postRunReset():
	global robot
	try:
		if robot is None:
			raise Exception("Robot not initialized")
		else:
			robot.MissionTimer.pause()
			print(f"Test took {robot.MissionTimer.time()} ms. This may include time to exit the test.")
			Robot.MissionTimer.reset()
			robot.reset()
			print("Robot reset complete")
	except Exception as e:
		print(f"Error occurred: {e}")

def startSettingsMenu():
	global robot, settingsSelector, armspeedselector, drivespeedselector, driveaccelerationselector, turnspeedselector, turnaccelerationselector, gyroselector
	if robot is None:
		print("Robot not initialized, exiting...")
		return
	else:
		while True:
			selectedItem = settingsSelector.selectNext()
			if selectedItem == "~":
				print("Exiting settings...")
				return
			elif selectedItem == "A":
				print("Arm speed selection")
				ArmSpeed = armspeedselector.selectNext()
				if ArmSpeed is int:
					robot.ArmSpeed = ArmSpeed
				print(f"Selected arm speed: {ArmSpeed}")
			elif selectedItem == "D":
				print("Drive speed selection")
				DriveSpeed = drivespeedselector.selectNext()
				if DriveSpeed is int:
					robot.DriveSpeed = DriveSpeed
				print(f"Selected drive speed: {DriveSpeed}")
			elif selectedItem == "d":
				print("Drive acceleration selection")
				DriveAcceleration = driveaccelerationselector.selectNext()
				if DriveAcceleration is int:
					robot.DriveAcceleration = DriveAcceleration
				print(f"Selected drive acceleration: {DriveAcceleration}")
			elif selectedItem == "T":
				print("Turn speed selection")
				TurnSpeed = turnspeedselector.selectNext()
				if TurnSpeed is int:
					robot.TurnSpeed = TurnSpeed
				print(f"Selected turn speed: {TurnSpeed}")
			elif selectedItem == "t":
				print("Turn acceleration selection")
				TurnAcceleration = turnaccelerationselector.selectNext()
				if TurnAcceleration is int:
					robot.TurnAcceleration = TurnAcceleration
				print(f"Selected turn acceleration: {TurnAcceleration}")
			elif selectedItem == "G":
				print("Gyro selection")
				DriveGyroEnabled = gyroselector.selectNext()
				if DriveGyroEnabled is bool:
					robot.DriveGyroEnabled = DriveGyroEnabled
				print(f"Gyro enabled: {DriveGyroEnabled}")
			elif selectedItem == "L":
				print("Drive distance selected")
				driveDistanceMenu()
			

if __name__ == "__main__":
	robot = Robot_config.prepare_robot_object()
	main()