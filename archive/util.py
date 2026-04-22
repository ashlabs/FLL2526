"""
Utility functions.
"""

from navigation import hub
from pybricks.tools import wait

def play_ding_dong():
    """Play a two-tone sound."""
    speaker = hub.speaker
    speaker.beep(880,150)
    wait(200)
    speaker.beep(660,300)
