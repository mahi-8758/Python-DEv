from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("darkgray")
t.pensize(10)
color = ['black', 'white']
def random_color():
    c1 = 'black'
    c2 = 'white'
    a = c1, c2
    num = 1

    for _ in range(160):
    
        if num % 2 == 0:
            return c1
        num += 1
        return c2
        
    
t.speed("fastest")
for _ in range(172):
    
    t.color(random_color())
    t.circle(100)
    t.setheading(t.heading() + 5)


screen.exitonclick()
    


    
    

    
    

    
        