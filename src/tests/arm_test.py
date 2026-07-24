from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()

Arm1 = Motor(Port.C)
Arm2 = Motor(Port.D, Direction.COUNTERCLOCKWISE)

def runCountdown(length : int = 5, warning : int = 3):
	HUB.light.on(Color.YELLOW)
	for i in range(length, 0, -1):
		HUB.display.number(i)
		print(f"Running in {i} (Total {length}, Warning {warning})")
		if i == warning:
			HUB.light.on(Color.ORANGE)
		wait(1000)
	HUB.light.on(Color.GREEN)
		
while True:
	Arm1.run_target(500, 0, then=Stop.HOLD)
	Arm2.run_target(500, 0, then=Stop.HOLD)
	runCountdown(5, 3)
	Arm1.run_target(500, 90, then=Stop.HOLD)
	Arm2.run_target(500, 90, then=Stop.HOLD)
	runCountdown(5, 3)