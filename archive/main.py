"""
Main program for FLL robot. Handles initialization, mission sequence selection, and sequence execution.
"""

from pybricks.tools import wait
from map import MISSIONS_GRID, FIELD_MAP
from navigation import navigate_grid, robot_init, robot, hub, drive_to_point
from missions import MISSIONS
from util import play_ding_dong
from pybricks.parameters import Button

# Initialize robot and hub
robot, hub = robot_init()

# Mission execution sequences
MISSION_SEQUENCES = {
    # "A": ["BASE","SURFACE BRUSHING", "MAP REVEAL", "MINESHAFT EXPLORER"],
    "A": ["BASE","SURFACE BRUSHING", "BASE"],
    "B": ["BASE","CAREFUL RECOVERY", "WHO LIVED HERE", "FORGE"],
    "C": ["BASE","HEAVY LIFTING", "SILO", "WHATS ON SALE"]
}

def select_program():
    """
    Allow user to switch programs using left/right buttons on the hub.
    Center button confirms selection.
    """
    mission_keys = list(MISSION_SEQUENCES.keys())
    index = 0
    while True:
        # hub.display.text(f"Program: {mission_keys[index]}")
        hub.display.text(mission_keys[index])
        pressed = []
        while not any(pressed):
            pressed = hub.buttons.pressed()
            wait(10)
        while any(hub.buttons.pressed()):
            wait(10)
        
        # if hub.left_button.pressed():
        if Button.LEFT in pressed:
            print("Left pressed")
            index = (index - 1) % len(mission_keys)
            wait(300)
        # if hub.right_button.pressed():
        if Button.RIGHT in pressed:
            print("Right pressed")
            index = (index + 1) % len(mission_keys)
            wait(300)
        # if hub.center_button.pressed():
        if Button.CENTER in pressed:
            print("Center pressed")
            wait(300)
            return mission_keys[index]
        wait(50)

def run_sequence(sequence):
    """
    Run a sequence of missions from the current position.
    The robot navigates to each mission, orients itself, and executes mission logic.
    Returns to base after completing the sequence.
    """
    current_position = MISSIONS_GRID[sequence[0]]

    for mission_name in sequence[1:]:
        target_position = MISSIONS_GRID[mission_name]
        # Navigate to mission
        navigate_grid(current_position, target_position)
        # drive_to_point
        play_ding_dong()
        # Orient and execute mission
        MISSIONS[mission_name]()
        current_position = target_position
    # Return to base
    # navigate_grid(current_position, MISSIONS_GRID["BASE"])
    

def main():
    """
    Main loop: select program, run sequence, repeat.
    """

    hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))
    while True:
        selected_sequence = select_program()
        print(selected_sequence)
        hub.display.text(selected_sequence)
        wait(2000)
        run_sequence(MISSION_SEQUENCES[selected_sequence])
        hub.display.text("Sequence Complete")
        wait(2000)

if __name__ == "__main__":
    main()
