import turtle as t
import guizero as g
from random import randint
player = t.Turtle()

def stars():
    t.bgcolor("black")
    player.penup()
    player.speed(0)
    for i in range(0,30,1):
        player.setposition(randint(-480,480),randint(-400,400))
        player.dot(10,"white")
    player.home()
    player.left(90)
    player.speed(1)
    player.color("white")

def shoot():
    shot = t.Turtle()
    shot.setposition(player.xcor(),player.ycor())
    shot.color("light blue")
    shot.setheading(player.heading())
    shot.speed(5)
    while (shot.xcor() > -500 and shot.xcor() < 500) and (shot.ycor() > -500 and shot.ycor() < 500):
        shot.forward(50)
    














stars()
shoot()
