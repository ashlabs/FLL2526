from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import Matrix, wait, StopWatch

HUB = PrimeHub()

Arm1 : Motor | None = None
Arm2 : Motor | None = None

def runCountdown(length : int = 5, warning : int = 3):
	HUB.light.on(Color.YELLOW)
	for i in range(length, 0, -1):
		HUB.display.number(i)
		print(f"Running in {i} (Total {length}, Warning {warning})")
		if i == warning:
			HUB.light.on(Color.ORANGE)
		wait(1000)
	HUB.light.on(Color.GREEN)

def run_test(armSpeed : int = 500):
	if Arm1 is None or Arm2 is None:
		print("Arm motors not initialized, exiting...")
		return
	print(f"Running arm test with speed {armSpeed}")
	print("Hold the right button down to exit")
	while Button.RIGHT not in HUB.buttons.pressed():
		Arm1.run_target(armSpeed, 0, then=Stop.HOLD)
		if Button.RIGHT in HUB.buttons.pressed():
			break
		Arm2.run_target(armSpeed, 0, then=Stop.HOLD)
		if Button.RIGHT in HUB.buttons.pressed():
			break
		runCountdown(5, 3)
		if Button.RIGHT in HUB.buttons.pressed():
			break
		Arm1.run_target(armSpeed, 90, then=Stop.HOLD)
		if Button.RIGHT in HUB.buttons.pressed():
			break
		Arm2.run_target(armSpeed, 90, then=Stop.HOLD)
		if Button.RIGHT in HUB.buttons.pressed():
			break
		runCountdown(5, 3)
	print("Exiting...")
	HUB.display.icon(Matrix([
			[0, 0, 0, 0, 255],
			[0, 0, 0, 255, 0],
			[255, 0, 255, 0, 0],
			[0, 255, 0, 0, 0],
			[0, 0, 0, 0, 0]]))
	while Button.RIGHT in HUB.buttons.pressed():
		wait(10)
	wait(500)

if __name__ == "__main__":
	Arm1 = Motor(Port.C)
	Arm2 = Motor(Port.D, Direction.COUNTERCLOCKWISE)
	run_test(500)