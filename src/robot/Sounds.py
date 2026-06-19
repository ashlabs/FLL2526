from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub : PrimeHub = PrimeHub()
speaker = hub.speaker

print("Sounds ready")

def play_default_ding_dong():
    speaker.beep(880, 150)
    wait(200)
    speaker.beep(660, 300)

def play_program_start_ding_dong():
    speaker.beep(880, 150)
    wait(200)
    speaker.beep(950, 400)

def play_program_end_ding_dong():
    speaker.beep(950, 400)
    wait(200)
    speaker.beep(880, 150)

def play_robot_ready_ding_dong():
    speaker.beep(950, 150)
    wait(200)
    speaker.beep(650, 400)
    
def play_default_double_ding_dong():
    speaker.beep(880, 150)
    wait(50)
    speaker.beep(880, 150)
    wait(200)
    speaker.beep(660, 300)
    wait(50)
    speaker.beep(660, 300)

def play_default_fast_ding_dong():
    speaker.beep(880, 50)
    wait(50)
    speaker.beep(660, 100)
    
def play_waypoint_ding_dong():
    speaker.beep(800, 100)
    wait(200)
    speaker.beep(700,600)
    
def play_handoff_to_mission_code_ding_dong():
    speaker.beep(720, 50)
    wait(100)
    speaker.beep(800, 600)
    
def play_handoff_to_nav_code_ding_dong():
    speaker.beep(720, 600)
    wait(100)
    speaker.beep(800, 50)

def play_default_error_ding_dong():
    speaker.beep(880, 300)
    wait(200)
    speaker.beep(660, 432)
    wait(200)
    speaker.beep(660, 236)

def play_note_array(, note_array : list[tuple[int, int]] = [(0, 0)]):
    for note in note_array:
        speaker.beep(note[0], note[1])