import random
import ipyturtle3 as turtle
from ipyturtle3 import hold_canvas

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

def draw_maze(my_ts, my_canvas, canvas_width, canvas_height, cell_size, maze):
    my_ts.clear()

    waller = turtle.Turtle(my_ts, isHolonomic=True)
    waller.shape("square")
    waller.width(10)
    waller.penup()
    waller.moveleft(canvas_width // 2)
    waller.moveup(canvas_height // 2)
    waller.pendown()

    with hold_canvas(my_canvas):
        for r, row in enumerate(maze[::2]):
            for c, is_clear in enumerate(row):
                if c + 1 == len(row):
                    waller.penup()
                    waller.moveleft(canvas_width - cell_size)
                    waller.movedown(cell_size * 2)
                else:
                    if not is_clear and not row[c + 1]:
                        waller.pendown()
                    else:
                        waller.penup()
                    waller.moveright(cell_size)

        waller.penup()
        waller.moveup(canvas_height + cell_size)

        transposed_iterator = zip(*maze)

        for c, col in enumerate(transposed_iterator):
            if c % 2 == 1:
                waller.moveright(cell_size)
            else:
                for r, is_clear in enumerate(col):
                    if r + 1 == len(maze):
                        waller.penup()
                        waller.moveright(cell_size)
                        waller.moveup(canvas_height - cell_size)
                    else:
                        if not is_clear and not maze[r + 1][c]:
                            waller.pendown()
                        else:
                            waller.penup()
                        waller.movedown(cell_size)


if __name__ == '__main__':
    # Maze grid: 0 = wall, 1 = path
    cols = 8
    rows = 5
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    generate_maze(maze, rows, cols, 1, 1)
    print(maze)