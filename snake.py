import time
from tkinter import *
from tkinter import ttk
from random import randint

width = 525
height = 525
item = 15
snake_size = 3
snake_list = []
snake_x = 10
snake_y = 10
nav_x = -1
nav_y = 0
is_Game = False

cnt_apple = 3
coords = []
cnt_walls = 0
coords_walls = []
score = 0
def  check_is_game(snake_list):
    global is_Game
    for x in range(snake_size-1):
        if snake_x == snake_list[x][0] and snake_y == snake_list[x][1]:
            return False
    for i in range(cnt_walls):
        if snake_x == coords_walls[i][0] and snake_y == coords_walls[i][1]:
            return False

def can_snake_eat_apple():
    global snake_size, score, cnt_apple
    deli = 0
    flag = False
    for i in range(len(coords)):
        if coords[i][0] == snake_x and coords[i][1] == snake_y:
            snake_size += 1
            score += 1
            cnt_apple -= 1
            canvas.delete(coords[i][2])
            lbl['text'] = f'Cчёт {score}'
            deli = i
            flag = True
    if flag:
        coords.pop(deli)
        flag = False
def check_border(x, y):
    global snake_y, snake_x
    if x >= 35:
        snake_x = 0
    if x <= -1:
        snake_x = 34
    if y >= 35:
        snake_y = 0
    if y <= -1:
        snake_y = 34
def create_apples(canvas):
    global coords, cnt_apple
    cnt_apple = randint(2, 6)
    for i in range(cnt_apple):
        x = randint(2, 33)
        y = randint(2, 33)
        for i in range(cnt_walls):
            if x == coords_walls[i][0] and y == coords_walls[i][1]:
                continue

        iddf = canvas.create_oval(x*item, y*item, x*item+item, y*item+item, fill='red')
        coords.append([x, y, iddf])
def check_size():
    if snake_size <= len(snake_list):
        poped = snake_list.pop(0)
        canvas.delete(poped[2])
def move_snake(event):
    global snake_y, snake_x, snake_size, coords, score, cnt_apple, nav_x, nav_y
    if event.keysym == 'Up' or event.keysym == 'w':
        nav_x = 0
        nav_y = -1

    if event.keysym == 'Down' or event.keysym == 's':
        nav_x = -0
        nav_y = 1
    if event.keysym == 'Right' or event.keysym == 'd':
        nav_x = 1
        nav_y = 0
    if event.keysym == 'Left' or event.keysym == 'a':
        nav_x = -1
        nav_y = 0

    snake_x += nav_x
    snake_y += nav_y
    check_border(snake_x, snake_y)

    can_snake_eat_apple()
    if cnt_apple == 0:
        create_apples(canvas)

    check_size()
    create_snake(canvas, snake_x, snake_y)
    check_is_game(snake_list)

def draw_field(canvas):
    for x in range(0, width, item):
        for y in range(0, height, item):
            canvas.create_rectangle(x, y, x+item, y+item, fill="#021703", outline="#082609")

def create_snake(canvas, snake_x, snake_y):
    global snake_list
    idf = canvas.create_rectangle(snake_x*item, snake_y*item, snake_x*item+item,
                                     snake_y*item+item, fill='green', outline='black')
    snake_list.append([snake_x, snake_y, idf])

def create_walls(canvas):
    global cnt_walls, coords_walls
    cnt_walls = randint(15, 20)
    for i in range(cnt_walls):
        x = randint(2, 33)
        y = randint(2, 33)
        if (x == 10 and y == 10) or (x == 10 and y == 11) or (x == 10 and y == 12):
            continue

        iddf = canvas.create_rectangle(x * item, y * item, x * item + item, y * item + item, fill='black')
        coords_walls.append([x, y, iddf])

def start_game():
    global is_Game, snake_y, snake_x
    create_all()
    is_Game = True
    while is_Game == True:
        time.sleep(0.17)
        snake_x += nav_x
        snake_y += nav_y
        check_border(snake_x, snake_y)

        can_snake_eat_apple()
        if cnt_apple == 0:
            create_apples(canvas)

        check_size()
        create_snake(canvas, snake_x, snake_y)
        fl = check_is_game(snake_list)
        if fl == False:
            break
        root.update_idletasks()
        root.update()

root = Tk()
root.geometry(f'{width+150}x{height}')
root.resizable(False, False)
root.title('Змейка')

canvas = Canvas(bg="white", width=width, height=height)
canvas.pack(anchor='w', expand=1)
lbl = ttk.Label(text=f'Cчёт: {score}')
lbl.place(x=545, y=20)
btn = ttk.Button(text='Start', command=start_game)
btn.place(x=540, y=100)

def create_all():
    global snake_y, snake_x, snake_size, snake_list, nav_x, nav_y, is_Game, cnt_apple, \
        cnt_walls, coords_walls, coords, score
    snake_size = 3
    snake_list = []
    snake_x = 10
    snake_y = 10
    nav_x = -1
    nav_y = 0
    is_Game = False

    cnt_apple = 3
    coords = []
    cnt_walls = 0
    coords_walls = []
    score = 0
    draw_field(canvas)
    create_snake(canvas, 10, 12)
    create_snake(canvas, 10, 11)
    create_snake(canvas, snake_x, snake_y)
    create_apples(canvas)
    create_walls(canvas)

canvas.bind_all('<KeyPress-Up>', move_snake)
canvas.bind_all('<KeyPress-Down>', move_snake)
canvas.bind_all('<KeyPress-Right>', move_snake)
canvas.bind_all('<KeyPress-Left>', move_snake)
canvas.bind_all('<a>', move_snake)
canvas.bind_all('<w>', move_snake)
canvas.bind_all('<s>', move_snake)
canvas.bind_all('<d>', move_snake)
root.update()

root.mainloop()