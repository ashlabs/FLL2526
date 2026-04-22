"""
Telemetry module: display robot state on hub and console.
"""

from navigation import hub, robot
from pybricks.tools import wait

def telemetry_task(state, sample_ms=500):
    """Continuously display robot position, heading, and speed."""
    x, y, theta = state.get("position", (0,0,0))
    speed = state.get("speed", 0)
    heading = hub.imu.heading()
    try:
        print(f"[TELEMETRY] x={x:.1f} cm, y={y:.1f} cm, theta={theta:.1f}, heading={heading:.1f}, speed={speed}")
    except Exception: pass
    try:
        hub.display.text(f"{int(heading)}")
    except Exception: pass
    wait(sample_ms)
