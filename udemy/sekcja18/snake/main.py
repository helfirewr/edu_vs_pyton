import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title("Snake game")
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor("green")

snake = Snake(0,0)
win.listen()
win.onkey(snake.keyUp, "Up")
win.onkey(snake.keyDown, "Down")
win.onkey(snake.keyLeft, "Left")
win.onkey(snake.keyRight, "Right")

win.onkey(snake.keyUp, "w")
win.onkey(snake.keyDown, "s")
win.onkey(snake.keyLeft, "a")
win.onkey(snake.keyRight, "d")

food = Food()

while True:
    win.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.checkSelfCollision() or snake.checkWallsCollision(width,height):
        food.refresh()
        snake.refresh()

win.mainloop()