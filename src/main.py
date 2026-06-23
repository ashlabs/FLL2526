from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

# Mission imports
from missions.mission1 import run as mission1
from missions.mission2 import run as mission2

from robot.Sounds import(
    play_program_start_ding_dong,
    play_program_end_ding_dong,
    play_robot_ready_ding_dong
)


MENU_OPTIONS = [
    ("1",mission1),
    ("2", mission2),
    ("E", None)
]


hub = PrimeHub()

hub.system.set_stop_button(Button.BLUETOOTH)

def wait_for_center_button():
    hub.light.on(Color.RED)
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)

    hub.light.on(Color.GREEN)
    while Button.CENTER in hub.buttons.pressed():
        wait(10)

    wait(250)

def wait_for_button_release(button):
    while button in hub.buttons.pressed():
        wait(10)

def choose_menu_option():
    option_index = 0

    while True:
        label, _ = MENU_OPTIONS[option_index]

        if label == "EXIT":
            hub.display.text("X")
        else:
            hub.display.text(label)

        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            option_index -= 1
            if option_index < 0:
                option_index = len(MENU_OPTIONS) - 1
            wait_for_button_release(Button.LEFT)
            wait(150)

        elif Button.RIGHT in pressed:
            option_index += 1
            if option_index >= len(MENU_OPTIONS):
                option_index = 0
            wait_for_button_release(Button.RIGHT)
            wait(150)

        elif Button.CENTER in pressed:
            wait_for_button_release(Button.CENTER)
            wait(250)
            return option_index

        wait(10)

def run_selected_mission(mission_function):
    hub.light.on(Color.RED)
    hub.display.text("GO?")
    wait_for_center_button()
    hub.light.on(Color.GREEN)
    play_program_start_ding_dong()
    wait(10)
    mission_function()
    wait(10)
    play_program_end_ding_dong()
    hub.light.on(Color.BLUE)

def main():
    play_robot_ready_ding_dong()
    hub.light.on(Color.BLUE)
    print("Robot is Ready")

    while True:
        selected_index = choose_menu_option()
        label, mission_function = MENU_OPTIONS[selected_index]

        if mission_function is None:
            hub.display.text("BYE!")
            break

        run_selected_mission(mission_function)
        
        wait(500)

if __name__ == "__main__":
    main()