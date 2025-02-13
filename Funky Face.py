from turtle import*

class Face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'
    def setSize(self, radius):
        self.size = radius
    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutLine()
        self.drawEye(45)
        self.drawEye(135)
        self.drawMouth()
        self.drawNose()
        pensize(5)
    def gohome(self):
        penup()
        goto (self.coord)

        setheading(0)
    def drawOutLine (self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.gohome()
    def drawEye (self, turn):
        penup()
        left(turn)
        forward(self.size / 2)
        pendown()
        dot(self.size/10)
        self.gohome()
    def drawMouth(self):
        penup()
        left(90)
        pendown()
        circle(self.size/1.7,90)
        self.gohome()
    def drawNose(self):
        if self.noseSize == 'large':
            dot(self.size/2, "grey")
        elif self.noseSize == 'small':
            dot(self.size/6, "grey")
        else:
            dot(self.sixe/4, "grey")
            self.gohome()


f1 = Face(0, 0)
f1.draw()

showturtle()
done()