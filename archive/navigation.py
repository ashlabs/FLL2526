from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import umath
from map import GRID_CELL_SIZE, FIELD_MAP, ROBOT_WIDTH, ROBOT_LENGTH

# -------------------------
# Field dimensions
# -------------------------
NUM_ROWS = len(FIELD_MAP)    # expected 22
NUM_COLS = len(FIELD_MAP[0]) # expected 40

# -------------------------
# Safe buffer around obstacles (in grid cells)
# -------------------------
SAFE_CELLS_X = max(0, int((ROBOT_WIDTH + GRID_CELL_SIZE - 1) // GRID_CELL_SIZE) // 2 + 1)
SAFE_CELLS_Y = max(0, int((ROBOT_LENGTH + GRID_CELL_SIZE - 1) // GRID_CELL_SIZE) // 2 + 1)

# -------------------------
# Shared robot and state
# -------------------------
robot: DriveBase = None
hub: PrimeHub = None

state = {
    "position": (0.0, 0.0, 0.0),  # x_mm, y_mm, heading_deg
    "speed": 0
}

# -------------------------
# Coordinate conversion helpers
# -------------------------
def robot_to_fieldmap(x_r, y_r):
    x_f = int(x_r)
    y_f = (NUM_ROWS - 1) - int(y_r)
    return x_f, y_f

def fieldmap_to_robot(x_f, y_f):
    x_r = int(x_f)
    y_r = (NUM_ROWS - 1) - int(y_f)
    return x_r, y_r

def grid_cell_center_mm_from_robot_grid(x_r, y_r):
    x_mm = x_r * GRID_CELL_SIZE + GRID_CELL_SIZE / 2.0
    y_mm = y_r * GRID_CELL_SIZE + GRID_CELL_SIZE / 2.0
    return x_mm, y_mm

# -------------------------
# Gyro-based turn with proportional control
# -------------------------
def gyro_turn(relative_deg, speed=60, tolerance=1.0, Kp=1.2):
    if hub is None or robot is None:
        raise RuntimeError("robot and hub must be initialized before using gyro_turn()")
    start = hub.imu.heading()
    goal = (start + relative_deg) % 360

    while True:
        current = hub.imu.heading()
        error = (goal - current + 180) % 360 - 180
        if abs(error) <= tolerance:
            break
        turn_rate = max(min(Kp * error, speed), -speed)
        robot.drive(0, turn_rate)
        wait(10)
        x, y, _ = state["position"]
        state["position"] = (x, y, current)

    robot.stop(Stop.BRAKE)
    wait(50)
    x, y, _ = state["position"]
    state["position"] = (x, y, hub.imu.heading())

# -------------------------
# Drive to a point
# -------------------------
# def drive_to_point(x1_mm, y1_mm, x2_mm, y2_mm, base_speed=150, step_mm=100, Kp=1.2):
#     if hub is None or robot is None:
#         raise RuntimeError("robot and hub must be initialized before using drive_to_point()")

#     dx = x2_mm - x1_mm
#     dy = y2_mm - y1_mm
#     distance = umath.sqrt(dx * dx + dy * dy)
#     if distance == 0:
#         return

#     target_angle = umath.degrees(umath.atan2(dy, dx)) % 360
#     current_heading = hub.imu.heading() % 360
#     angle_diff = (target_angle - current_heading + 180) % 360 - 180

#     drive_backward = False
#     if abs(angle_diff) > 90:
#         drive_backward = True
#         if angle_diff > 0:
#             relative_turn = angle_diff - 180
#         else:
#             relative_turn = angle_diff + 180
#     else:
#         relative_turn = angle_diff

#     gyro_turn(relative_turn, Kp=Kp)

#     remaining = float(distance)
#     while remaining > 0.5:
#         move = float(step_mm) if remaining > step_mm else remaining
#         move_speed = base_speed if remaining > 150 else max(80, int(base_speed * (remaining / 150.0)))
#         robot.straight(-move if drive_backward else move)
#         heading_deg = hub.imu.heading()
#         heading_rad = umath.radians(heading_deg)
#         dx_mm = umath.cos(heading_rad) * (-move if drive_backward else move)
#         dy_mm = umath.sin(heading_rad) * (-move if drive_backward else move)
#         x_mm, y_mm, _ = state["position"]
#         x_mm += dx_mm
#         y_mm += dy_mm
#         state["position"] = (x_mm, y_mm, heading_deg)
#         state["speed"] = move_speed
#         remaining -= move
#         wait(20)

#     robot.stop(Stop.BRAKE)
#     state["speed"] = 0

def drive_to_point(x1_mm, y1_mm, x2_mm, y2_mm, base_speed=150, step_mm=100, Kp=1.2):
    """
    Drive the robot from (x1_mm, y1_mm) to (x2_mm, y2_mm) always moving forward.
    Turns to face the target using gyro_turn(), then moves in small steps while
    updating the robot's odometry.
    """
    if hub is None or robot is None:
        raise RuntimeError("robot and hub must be initialized before using drive_to_point()")

    dx = x2_mm - x1_mm
    dy = y2_mm - y1_mm
    distance = umath.sqrt(dx * dx + dy * dy)
    if distance == 0:
        return

    # Always face the target
    target_angle = umath.degrees(umath.atan2(dy, dx)) % 360
    current_heading = hub.imu.heading() % 360
    angle_diff = (target_angle - current_heading + 180) % 360 - 180

    # Always drive forward
    drive_backward = False
    relative_turn = angle_diff
    gyro_turn(relative_turn, Kp=Kp)

    # Drive in steps towards the target
    remaining = float(distance)
    while remaining > 0.5:
        move = float(step_mm) if remaining > step_mm else remaining
        move_speed = base_speed if remaining > 150 else max(80, int(base_speed * (remaining / 150.0)))
        robot.straight(move)
        
        # Update odometry
        heading_deg = hub.imu.heading()
        heading_rad = umath.radians(heading_deg)
        dx_mm = umath.cos(heading_rad) * move
        dy_mm = umath.sin(heading_rad) * move
        x_mm, y_mm, _ = state["position"]
        x_mm += dx_mm
        y_mm += dy_mm
        state["position"] = (x_mm, y_mm, heading_deg)
        state["speed"] = move_speed
        remaining -= move
        wait(20)

    robot.stop(Stop.BRAKE)
    state["speed"] = 0


# -------------------------
# BFS without collections.deque
# -------------------------
# def bfs_path(field_map, start_robot_grid, goal_robot_grid):
#     start_f = robot_to_fieldmap(*start_robot_grid)
#     goal_f = robot_to_fieldmap(*goal_robot_grid)
#     rows = len(field_map)
#     cols = len(field_map[0])

#     # Expand obstacles for robot safety
#     safe_map = [row[:] for row in field_map]
#     for fy in range(rows):
#         for fx in range(cols):
#             if field_map[fy][fx] == 1:
#                 for dy in range(-SAFE_CELLS_Y, SAFE_CELLS_Y + 1):
#                     for dx in range(-SAFE_CELLS_X, SAFE_CELLS_X + 1):
#                         nx = fx + dx
#                         ny = fy + dy
#                         if 0 <= nx < cols and 0 <= ny < rows:
#                             safe_map[ny][nx] = 1

#     sx, sy = start_f
#     gx, gy = goal_f

#     if not (0 <= sx < cols and 0 <= sy < rows) or not (0 <= gx < cols and 0 <= gy < rows):
#         return []
#     if safe_map[sy][sx] == 1 or safe_map[gy][gx] == 1:
#         return []

#     queue = [(sx, sy)]
#     visited = [[False] * cols for _ in range(rows)]
#     prev = [[None] * cols for _ in range(rows)]
#     visited[sy][sx] = True
#     directions = [(1,0), (-1,0), (0,1), (0,-1)]
#     found = False

#     while queue:
#         cx, cy = queue.pop(0)
#         if (cx, cy) == (gx, gy):
#             found = True
#             break
#         for dx, dy in directions:
#             nx = cx + dx
#             ny = cy + dy
#             if 0 <= nx < cols and 0 <= ny < rows:
#                 if not visited[ny][nx] and safe_map[ny][nx] == 0:
#                     visited[ny][nx] = True
#                     prev[ny][nx] = (cx, cy)
#                     queue.append((nx, ny))

#     if not found:
#         return []

#     # Reconstruct path
#     fm_path = []
#     node = (gx, gy)
#     while node is not None:
#         fm_path.append(node)
#         px, py = node
#         node = prev[py][px]
#     fm_path.reverse()
#     robot_path = [fieldmap_to_robot(fx, fy) for (fx, fy) in fm_path]
#     return robot_path

# -------------------------
# BFS without collections.deque, optimized for MicroPython
# -------------------------
def bfs_path(field_map, start_robot_grid, goal_robot_grid):
    start_f = robot_to_fieldmap(*start_robot_grid)
    goal_f = robot_to_fieldmap(*goal_robot_grid)
    rows = len(field_map)
    cols = len(field_map[0])

    # Expand obstacles for robot safety
    safe_map = [row[:] for row in field_map]
    for fy in range(rows):
        for fx in range(cols):
            if field_map[fy][fx] == 1:
                for dy in range(-SAFE_CELLS_Y, SAFE_CELLS_Y + 1):
                    for dx in range(-SAFE_CELLS_X, SAFE_CELLS_X + 1):
                        nx = fx + dx
                        ny = fy + dy
                        if 0 <= nx < cols and 0 <= ny < rows:
                            safe_map[ny][nx] = 1

    sx, sy = start_f
    gx, gy = goal_f

    if not (0 <= sx < cols and 0 <= sy < rows) or not (0 <= gx < cols and 0 <= gy < rows):
        return []
    if safe_map[sy][sx] == 1 or safe_map[gy][gx] == 1:
        return []

    visited = [[False] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    visited[sy][sx] = True

    current_layer = [(sx, sy)]
    found = False
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while current_layer:
        next_layer = []
        for cx, cy in current_layer:
            if (cx, cy) == (gx, gy):
                found = True
                break
            for dx, dy in directions:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    if not visited[ny][nx] and safe_map[ny][nx] == 0:
                        visited[ny][nx] = True
                        prev[ny][nx] = (cx, cy)
                        next_layer.append((nx, ny))
        if found:
            break
        current_layer = next_layer

    if not found:
        return []

    # Reconstruct path
    fm_path = []
    node = (gx, gy)
    while node is not None:
        fm_path.append(node)
        px, py = node
        node = prev[py][px]
    fm_path.reverse()
    robot_path = [fieldmap_to_robot(fx, fy) for (fx, fy) in fm_path]
    return robot_path

# -------------------------
# Navigate using BFS
# -------------------------
def navigate_grid(start_grid_robot, goal_grid_robot, verbose=True):
    if hub is None or robot is None:
        raise RuntimeError("robot and hub must be initialized before navigating")

    if verbose:
        print("Finding path:", start_grid_robot, "->", goal_grid_robot)

    path = bfs_path(FIELD_MAP, start_grid_robot, goal_grid_robot)
    if not path:
        print("No path found")
        return

    if verbose:
        print("Path:", path)

    for i in range(len(path)-1):
        cur_cell = path[i]
        next_cell = path[i+1]
        start_mm = grid_cell_center_mm_from_robot_grid(*cur_cell)
        end_mm = grid_cell_center_mm_from_robot_grid(*next_cell)
        if verbose:
            print(f"Segment {i+1}: {cur_cell} -> {next_cell}, heading {hub.imu.heading():.2f}")
        drive_to_point(start_mm[0], start_mm[1], end_mm[0], end_mm[1])
        if verbose:
            x_mm, y_mm, h_deg = state["position"]
            print(f"Arrived at approx (mm): ({x_mm:.1f}, {y_mm:.1f}), heading: {h_deg:.1f}")

    if verbose:
        print("Navigation complete.")

# -------------------------
# Robot initialization
# -------------------------
def robot_init(left_port=Port.A, right_port=Port.B, wheel_diameter=49.5, axle_track=73.5):
    global robot, hub
    hub = PrimeHub()
    left_motor = Motor(left_port)
    right_motor = Motor(right_port)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)
    x0_mm, y0_mm = grid_cell_center_mm_from_robot_grid(0, 0)
    state["position"] = (x0_mm, y0_mm, hub.imu.heading() if hasattr(hub, "imu") else 0.0)
    state["speed"] = 0
    return robot, hub

def navigate_to(goal_grid_robot, verbose=True):
    x_mm, y_mm, heading_deg = state["position"]
    current_x_grid = int(x_mm // GRID_CELL_SIZE)
    current_y_grid = int(y_mm // GRID_CELL_SIZE)
    start_grid_robot = (current_x_grid, current_y_grid)
    if verbose:
        print("Current odometry (mm):", (x_mm, y_mm))
        print("Converted to robot-grid:", start_grid_robot)
        print("Navigating to:", goal_grid_robot)
    navigate_grid(start_grid_robot, goal_grid_robot, verbose=verbose)
