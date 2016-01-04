import math
from PIL import Image, ImageDraw


class Turtle:
    pass


def inititialiseTurtle(turtle, draw_obj, position=[0, 0], heading=0.0, width=10, pen=False, fill=(255, 255, 255)):
    turtle.position = position
    turtle.angle = heading
    turtle.pen = pen
    turtle.fill = fill
    turtle.width = width
    turtle.draw_obj = draw_obj


def penUp(turtle):
    turtle.pen = False


def penDown(turtle):
    turtle.pen = True


def turn(turtle, angle):
    new_angle = turtle.angle + angle
    turtle.angle = math.fmod(new_angle, 360)


def move(turtle, steps):
    theta = math.radians(turtle.angle)
    px = steps * math.cos(theta)
    py = steps * -math.sin(theta)
    if turtle.pen:
        turtle.draw_obj.line(
            (
                round(turtle.position[0]), round(turtle.position[1]), round(turtle.position[0] + px),
                round(turtle.position[1] + py)
            ),
            fill=turtle.fill,
            width=turtle.width
        )
    turtle.position = [(turtle.position[0] + px), (turtle.position[1] + py)]


def circle(turtle, radius, segments):
    turtle.pen = True

    angleStep = float(360 / segments)
    distanceStep = math.sqrt((2 * radius * radius) - (2 * radius * radius * math.cos(math.radians(angleStep))))

    for i in range(0, segments):
        move(turtle, distanceStep)
        turn(turtle, angleStep)


def square(turtle, length):
    turtle.pen = True

    move(turtle, length)
    turn(turtle, 90)
    move(turtle, length)
    turn(turtle, 90)
    move(turtle, length)
    turn(turtle, 90)
    move(turtle, length)
    turn(turtle, 90)


img = Image.new("RGB", (500, 500))
draw = ImageDraw.Draw(img)

myTurtle = Turtle()
inititialiseTurtle(
    turtle=myTurtle,
    draw_obj=draw,
    position=(250, 250),
    heading=0,
    width=3,
    pen=True,
    fill=(100, 255, 255)
)

circle(turtle=myTurtle, radius=100, segments=38)
square(turtle=myTurtle, length=100)

img.show()
