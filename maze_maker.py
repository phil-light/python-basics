import random
import sys

# Maze settings
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions: (dx, dy)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


# Recursive backtracking maze generation
def generate_maze(maze, maze_rows, maze_cols, x, y):
    maze[y][x] = 1
    dirs = DIRS[:]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < maze_cols and 0 <= ny < maze_rows and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            generate_maze(maze, maze_rows, maze_cols, nx, ny)


if __name__ == '__main__':
    # Maze grid: 0 = wall, 1 = path
    cols = 8
    rows = 5
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    generate_maze(maze, rows, cols, 1, 1)
    print(maze)