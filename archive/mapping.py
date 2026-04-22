"""
Utilities for working with robot navigation maps at 5 cm resolution.
Includes collision checking and conversions.
"""

from map import GRID_CELL_SIZE, FIELD_MAP, ROBOT_WIDTH, ROBOT_LENGTH

def is_cell_free(grid_x, grid_y, field_map=FIELD_MAP, robot_size=(ROBOT_WIDTH, ROBOT_LENGTH)):
    """
    Check if the robot can occupy a cell without colliding with obstacles.

    Args:
        grid_x (int): X coordinate in grid.
        grid_y (int): Y coordinate in grid.
        field_map (list[list[int]]): 2D map of the field (0=free, 1=obstacle)
        robot_size (tuple): (width_mm, length_mm) of robot.

    Returns:
        bool: True if robot can fit at this cell.
    """
    width_cells = int((robot_size[0] + GRID_CELL_SIZE - 1) / GRID_CELL_SIZE)  # ceil division
    length_cells = int((robot_size[1] + GRID_CELL_SIZE - 1) / GRID_CELL_SIZE)

    rows = len(field_map)
    cols = len(field_map[0])

    for dx in range(width_cells):
        for dy in range(length_cells):
            x = grid_x + dx
            y = grid_y + dy
            if x >= cols or y >= rows:
                return False
            if field_map[y][x] != 0:
                return False
    return True

def grid_to_mm(grid_pos):
    """
    Convert grid coordinates to millimeters.
    
    Args:
        grid_pos (tuple): (x_grid, y_grid)
    
    Returns:
        tuple: (x_mm, y_mm)
    """
    return (grid_pos[0] * GRID_CELL_SIZE, grid_pos[1] * GRID_CELL_SIZE)

def mm_to_grid(mm_pos):
    """
    Convert millimeter coordinates to grid coordinates.
    
    Args:
        mm_pos (tuple): (x_mm, y_mm)
    
    Returns:
        tuple: (x_grid, y_grid)
    """
    return (int(mm_pos[0] / GRID_CELL_SIZE), int(mm_pos[1] / GRID_CELL_SIZE))
