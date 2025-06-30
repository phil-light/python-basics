import random
import ipyturtle3 as turtle
from ipyturtle3 import hold_canvas



# Directions: (dx, dy)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# Recursive backtracking maze generation
def generate_maze(maze_rows, maze_cols, unique_maze_number):
    random.seed(unique_maze_number)
    # Maze grid: 0 = wall, 1 = path
    maze = [[0 for _ in range(maze_cols)] for _ in range(maze_rows)]
    return _gen_maze(maze, maze_rows, maze_cols, 1, 1)


def _gen_maze(maze, maze_rows, maze_cols, x, y):
    maze[y][x] = 1
    dirs = DIRS[:]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < maze_cols and 0 <= ny < maze_rows and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            _gen_maze(maze, maze_rows, maze_cols, nx, ny)
    return maze


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
        for r, row in enumerate(maze):
            if r % 2 == 1:
                waller.movedown(cell_size)
            else:
                for c, is_clear in enumerate(row):
                    if c + 1 == len(row):
                        waller.penup()
                        waller.moveleft(canvas_width - cell_size)
                        waller.movedown(cell_size)
                    else:
                        if not is_clear and not row[c + 1]:
                            waller.pendown()
                        else:
                            waller.penup()
                        waller.moveright(cell_size)

        waller.penup()
        waller.moveup(canvas_height)

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

        waller.penup()
        waller.color(random.choice(colors))
        waller.home()
        waller.moveleft((canvas_width / -2) + (random.random() * canvas_width))
        waller.moveup((canvas_height / -2) + (random.random() * canvas_height))


def make_maze_runner(turtle_screen):
    runner = turtle.Turtle(turtle_screen)
    runner.shape("turtle")
    runner.width(3)
    return runner


def start_maze(runner, canvas_width, canvas_height, cell_size):
    random.seed()
    runner.penup()
    runner.home()
    runner.left(90)
    runner.forward(canvas_height / 2 - cell_size)
    runner.left(90)
    runner.forward(canvas_width / 2 - cell_size)
    runner.left(180)
    runner.pendown()
    runner.color(random.choice(colors))


colors = ['maroon'
,'red'
,'purple'
,'fuchsia'
,'green'
,'lime'
,'olive'
,'yellow'
,'navy'
,'blue'
,'teal'
,'aqua'
,'orange'
,'aliceblue'
,'aquamarine'
,'blueviolet'
,'brown'
,'cadetblue'
,'chocolate'
,'coral'
,'cornflowerblue'
,'crimson'
,'darkblue'
,'darkcyan'
,'darkgoldenrod'
,'darkgray'
,'darkgreen'
,'darkkhaki'
,'darkmagenta'
,'darkolivegreen'
,'darkorange'
,'darkorchid'
,'darkred'
,'darksalmon'
,'darkseagreen'
,'darkslateblue'
,'darkslategray'
,'darkturquoise'
,'darkviolet'
,'deeppink'
,'deepskyblue'
,'dimgray'
,'dodgerblue'
,'firebrick'
,'forestgreen'
,'greenyellow'
,'hotpink'
,'indianred'
,'lawngreen'
,'olivedrab'
,'orangered'
,'orchid'
,'peru'
,'pink'
,'plum'
,'rosybrown'
,'royalblue'
,'saddlebrown'
,'salmon'
,'sandybrown'
,'seagreen'
,'sienna'
,'slateblue'
,'slategray'
,'springgreen'
,'steelblue'
,'tomato'
,'turquoise'
,'violet'
,'yellowgreen']


if __name__ == '__main__':
    # Maze grid: 0 = wall, 1 = path
    cols = 8
    rows = 5
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    generate_maze(maze, rows, cols, 1, 1)
    print(maze)