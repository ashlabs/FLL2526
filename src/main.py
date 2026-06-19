from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

# Mission imports
from missions.mission1 import run as mission1
from missions.mission2 import run as mission2


MENU_OPTIONS = [
    ("1",mission1),
    ("2", mission2),
    ("E", None)
]


hub = PrimeHub()

hub.system.set_stop_button(Button.BLUETOOTH)

def wait_for_center_button():
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)

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
    hub.display.text("GO?")
    wait_for_center_button()
    hub.speaker.beep()
    mission_function()

def main():
    hub.speaker.beep()

    while True:
        selected_index = choose_menu_option()
        label, mission_function = MENU_OPTIONS[selected_index]

        if mission_function is None:
            hub.display.text("BYE!")
            break

        run_selected_mission(mission_function)
        
        wait(500)

main()