from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait, Matrix

print("Basic selector ready")

class BasicSelector:
	options : list[str | int | float | bool | Matrix | None] = []
	hub = PrimeHub()
	currentIndex : int = 0
	selectedOption : str | int | float | bool | Matrix | None = None
	displayMultiplier : float = 1

	def __init__(self, options: list[str | int | float | bool | Matrix | None], defaultIndex: int = 0, displayMultiplier : float = 1):
		self.options = options
		self.currentIndex = defaultIndex
		self.displayMultiplier = displayMultiplier

	def showCurrentOption(self):
		selectedOption = self.options[self.currentIndex]
		if isinstance(selectedOption, str):
			if len(selectedOption) == 1:
				self.hub.display.char(selectedOption)
			else:
				self.hub.display.text(selectedOption)
		elif isinstance(selectedOption, bool):
			if selectedOption:
				self.hub.display.icon(Matrix([
						[0, 0, 0, 0, 255],
						[0, 0, 0, 255, 0],
						[255, 0, 255, 0, 0],
						[0, 255, 0, 0, 0],
						[128, 128, 128, 128, 128]]))
			else:
				self.hub.display.icon(Matrix([
						[255, 0, 0, 0, 255],
						[0, 255, 0, 255, 0],
						[0, 0, 255, 0, 0],
						[0, 255, 0, 255, 0],
						[255, 128, 128, 128, 255]]))
		elif isinstance(selectedOption, int):
			self.hub.display.number(selectedOption * self.displayMultiplier)
		elif isinstance(selectedOption, Matrix):
			self.hub.display.icon(selectedOption)
		elif selectedOption is None:
			self.hub.display.icon(Matrix([[255, 255, 255, 255, 255],[255, 255, 0, 255, 255],[255, 0, 255, 0, 255],[255, 255, 0, 255, 255],[255, 255, 255, 255, 255]]))
		else:
			print(f"Unknown option type: {type(selectedOption)}, content: {selectedOption}")
			self.hub.display.text(str(selectedOption))

	def selectNext(self):
		self.hub.system.set_stop_button(Button.BLUETOOTH)
		self.hub.light.on(Color.BLUE)
		if len(self.options) == 0:
			print("No options to select")
			return None
		if len(self.options) == 1:
			print(f"Only one option, selected {self.options[0]}")
			return self.options[0]
		self.showCurrentOption()
		while True:
			if Button.CENTER in self.hub.buttons.pressed():
				self.selectedOption = self.options[self.currentIndex]
				print(f"Selected {self.selectedOption}")
				self.hub.light.on(Color.CYAN)
				while Button.CENTER in self.hub.buttons.pressed():
					wait(10)
				wait(500)
				self.hub.display.off()
				self.hub.system.set_stop_button(Button.CENTER)
				return self.selectedOption
			elif Button.RIGHT in self.hub.buttons.pressed():
				self.currentIndex += 1
				if self.currentIndex >= len(self.options):
					self.currentIndex = 0
				self.showCurrentOption()
				while Button.RIGHT in self.hub.buttons.pressed():
					wait(10)
				wait(100)
			elif Button.LEFT in self.hub.buttons.pressed():
				self.currentIndex -= 1
				if self.currentIndex < 0:
					self.currentIndex = len(self.options) - 1
				self.showCurrentOption()
				while Button.LEFT in self.hub.buttons.pressed():
					wait(10)
				wait(100)