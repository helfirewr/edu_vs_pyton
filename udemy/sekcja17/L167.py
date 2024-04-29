import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

t.forward(100)
print("x:", t.xcor() )
print("y:", t.ycor() )

def keyPressedW():
    print("w clicked")
    t.fd(20)

def keyPressedS():
    print("w clicked")
    t.backward(20)

def keyPressedA():
    print("a clicked")
    t.left(20)

def keyPressedD():
    print("d clicked")
    t.right(20)

win.listen()
win.onkey( keyPressedW, "w" )
win.onkey( keyPressedS, "s" )
win.onkey( keyPressedA, "a" )
win.onkey( keyPressedD, "d" )

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)

win.mainloop()