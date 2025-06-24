import random
import sys

# Maze settings
CELL_SIZE = 20
MAZE_COLS = 15
MAZE_ROWS = 10
WIDTH = MAZE_COLS * CELL_SIZE
HEIGHT = MAZE_ROWS * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions: (dx, dy)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


# Recursive backtracking maze generation
def generate_maze(maze, x, y):
    maze[y][x] = 1
    dirs = DIRS[:]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < MAZE_COLS and 0 <= ny < MAZE_ROWS and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            generate_maze(maze, nx, ny)


if __name__ == '__main__':
    # Maze grid: 0 = wall, 1 = path
    maze = [[0 for _ in range(MAZE_COLS)] for _ in range(MAZE_ROWS)]
    generate_maze(maze, 1, 1)
    print(maze)