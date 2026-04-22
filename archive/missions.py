"""
Missions module: define each mission function and map names to functions.
"""

from navigation import robot, hub

def mission_1():
    """SURFACE BRUSHING"""
    print("Mission 1 start")
    robot.straight(50)
    print("Mission 1 end")

def mission_2():
    """MAP REVEAL"""
    print("Mission 2 start")
    robot.straight(50)
    print("Mission 2 end")

def mission_3():
    """MINESHAFT EXPLORER"""
    print("Mission 3 start")
    robot.straight(50)
    print("Mission 3 end")

def mission_4():
    """CAREFUL RECOVERY"""
    print("Mission 4 start")
    robot.straight(50)
    print("Mission 4 end")

def mission_5():
    """WHO LIVED HERE"""
    print("Mission 5 start")
    robot.straight(50)
    print("Mission 5 end")

def mission_6():
    """FORGE"""
    print("Mission 6 start")
    robot.straight(50)
    print("Mission 6 end")

def mission_7():
    """HEAVY LIFTING"""
    print("Mission 7 start")
    robot.straight(50)
    print("Mission 7 end")

def mission_8():
    """SILO"""
    print("Mission 8 start")
    robot.straight(50)
    print("Mission 8 end")

def mission_9():
    """WHATS ON SALE"""
    print("Mission 9 start")
    robot.straight(50)
    print("Mission 9 end")

# Map mission names to functions
MISSIONS = {
    "SURFACE BRUSHING": mission_1,
    "MAP REVEAL": mission_2,
    "MINESHAFT EXPLORER": mission_3,
    "CAREFUL RECOVERY": mission_4,
    "WHO LIVED HERE": mission_5,
    "FORGE": mission_6,
    "HEAVY LIFTING": mission_7,
    "SILO": mission_8,
    "WHATS ON SALE": mission_9
}
