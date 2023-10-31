import turtle

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("Light green")
drawing_screen.title("Python Turtle")


turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def turtle_forward():
    turtle_instance.forward(100)
def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.right(10)
def rotate_angle_left():
    turtle_instance.left(10)
def clear_screen():
    turtle_instance.clear()
def turtle_return_home():
    turtle_instance.home()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()

drawing_screen.listen()
drawing_screen.onkey(fun=turtle_forward,key="space")
drawing_screen.onkey(fun=rotate_angle_right,key="Down")
drawing_screen.onkey(fun=rotate_angle_left,key="Up")
drawing_screen.onkey(fun=clear_screen,key="c")
drawing_screen.onkey(fun=turtle_return_home,key="h")

drawing_screen.onkey(fun=turtle_pen_up,key="q")
drawing_screen.onkey(fun=turtle_pen_down,key="w")




turtle.done()