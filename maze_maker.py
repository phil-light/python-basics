import random
import ipyturtle3 as turtle
from ipyturtle3 import hold_canvas


colors = ['silver'
,'gray'
,'maroon'
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
,'antiquewhite'
,'aquamarine'
,'azure'
,'beige'
,'bisque'
,'blanchedalmond'
,'blueviolet'
,'brown'
,'burlywood'
,'cadetblue'
,'chartreuse'
,'chocolate'
,'coral'
,'cornflowerblue'
,'cornsilk'
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
,'floralwhite'
,'forestgreen'
,'gainsboro'
,'ghostwhite'
,'gold'
,'goldenrod'
,'greenyellow'
,'honeydew'
,'hotpink'
,'indianred'
,'indigo'
,'ivory'
,'khaki'
,'lavender'
,'lavenderblush'
,'lawngreen'
,'lemonchiffon'
,'lightblue'
,'lightcoral'
,'lightcyan'
,'lightgoldenrodyellow'
,'lightgray'
,'lightgreen'
,'lightpink'
,'lightsalmon'
,'lightseagreen'
,'lightskyblue'
,'lightslategray'
,'lightsteelblue'
,'lightyellow'
,'limegreen'
,'linen'
,'mediumaquamarine'
,'mediumblue'
,'mediumorchid'
,'mediumpurple'
,'mediumseagreen'
,'mediumslateblue'
,'mediumspringgreen'
,'mediumturquoise'
,'mediumvioletred'
,'midnightblue'
,'mintcream'
,'mistyrose'
,'moccasin'
,'navajowhite'
,'oldlace'
,'olivedrab'
,'orangered'
,'orchid'
,'palegoldenrod'
,'palegreen'
,'paleturquoise'
,'palevioletred'
,'papayawhip'
,'peachpuff'
,'peru'
,'pink'
,'plum'
,'powderblue'
,'rosybrown'
,'royalblue'
,'saddlebrown'
,'salmon'
,'sandybrown'
,'seagreen'
,'seashell'
,'sienna'
,'skyblue'
,'slateblue'
,'slategray'
,'snow'
,'springgreen'
,'steelblue'
,'tan'
,'thistle'
,'tomato'
,'turquoise'
,'violet'
,'wheat'
,'whitesmoke'
,'yellowgreen'
,'rebeccapurple']


# Directions: (dx, dy)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# Recursive backtracking maze generation
def generate_maze(maze_rows, maze_cols, x, y):
    # Maze grid: 0 = wall, 1 = path
    maze = [[0 for _ in range(MAZE_COLS)] for _ in range(MAZE_ROWS)]

    maze[y][x] = 1
    dirs = DIRS[:]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < maze_cols and 0 <= ny < maze_rows and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            generate_maze(maze, maze_rows, maze_cols, nx, ny)
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


def start_maze(runner):
    runner.penup()
    runner.home()
    runner.left(90)
    runner.forward(130)
    runner.left(90)
    runner.forward(230)
    runner.left(180)
    runner.pendown()
    runner.color(random.choice(colors))


if __name__ == '__main__':
    # Maze grid: 0 = wall, 1 = path
    cols = 8
    rows = 5
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    generate_maze(maze, rows, cols, 1, 1)
    print(maze)