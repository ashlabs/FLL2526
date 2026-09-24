import Robot_config
from Robot import Robot
from BasicSelector import BasicSelector
import Run1, Run2, Run3, Run4

def main(robot : Robot):
	RunSelector = BasicSelector([1, 2, 3, 4])
	while True:
		RunSelector.selectNext()
		if RunSelector.selectedOption ==  1:
			Run1.runMain(robot)
		elif RunSelector.selectedOption == 2:
			Run2.runMain(robot)
		elif RunSelector.selectedOption == 3:
			Run3.runMain(robot)
		elif RunSelector.selectedOption == 4:
			Run4.runMain(robot)

if __name__ == "__main__":
	robot = Robot_config.config_2()
	main(robot)