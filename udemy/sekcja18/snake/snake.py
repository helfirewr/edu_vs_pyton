import turtle

class Snake:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    MOVE_DISTANCE = 20

    def __init__(self, startX, startY):
        self.startX = startX
        self.startY = startY
        self.segments = []
        self.refresh()

    def refresh(self):
        print("snake reset")
        for seg in self.segments:
            seg.goto(2000,2000)
        self.segments.clear()

        self.segments = []
        self.addSegment(self.startX, self.startY)
        self.head = self.segments[0]
        self.direction = None

    def addSegment(self, x, y):
        t = turtle.Turtle("square")
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.goto(x,y)
        t.color("red")
        t.showturtle()
        self.segments.append(t)

    def extend(self):
        self.addSegment(1000, 1000)

    
    def keyUp(self):
        self.direction = Snake.UP

    def keyDown(self):
        self.direction = Snake.DOWN

    def keyLeft(self):
        self.direction = Snake.LEFT

    def keyRight(self):
        self.direction = Snake.RIGHT

    def move(self):
        headX = self.head.xcor()
        headY = self.head.ycor()

        if self.direction == Snake.UP:
            headY += Snake.MOVE_DISTANCE
        if self.direction == Snake.DOWN:
            headY -= Snake.MOVE_DISTANCE
        if self.direction == Snake.LEFT:
            headX -= Snake.MOVE_DISTANCE
        if self.direction == Snake.RIGHT:
            headX += Snake.MOVE_DISTANCE

        index = len(self.segments) - 1
        while index > 0:
            newX = self.segments[index - 1].xcor()
            newY = self.segments[index - 1].ycor()
            self.segments[index].goto(newX, newY)
            index -= 1

        self.head.goto(headX, headY)

    
    def checkSelfCollision(self):
        for seg in self.segments:
            if seg == self.head:
                continue
            elif self.head.distance(seg) < 20:
                return True

        return False

    def checkWallsCollision(self, screenWidth, screenHeight):
        halfWidth = screenWidth / 2
        halfheight = screenHeight / 2
        x = self.head.xcor()
        y = self.head.ycor()

        if x > halfWidth or x < -halfWidth or y > halfheight or y < -halfheight:
            return True
        else:
            return False
