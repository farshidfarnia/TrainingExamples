from turtle import *
from shapes import *
from random import randint

speed(0)
window = turtle.Screen()
window.bgcolor("#0000BC")

# Moon
draw_circle(turtle, "white", 120, 80, 50)
draw_circle(turtle, "#0000BC", 100, 80, 50)

# Stars
numberOfStars = randint(10,15)

for i in range(0,numberOfStars):
    x = randint(-180, 180)
    y = randint(-160, 180)
    size = randint(3, 20)

    drow_star(turtle, "white", x, y, size)

# Message
penup()
color("yellow")
goto(-110, -200)
write("Moonlight Greetings", font=("Arial", 20, "bold"))
hideturtle()
turtle.mainloop()