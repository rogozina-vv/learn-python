import turtle
import math

turtle.shape('turtle')

class figure:
    def parametrs_of_figure(self):
        print ("у каждой фигуры есть такие параметры, как периметр и площадь")
    def draw_figure(self):
        print ("каждую фигуру можно нарисовать")

class circle(figure):
    def __init__(self, x_center, y_center, lenght_x):
        self.x_center = x_center
        self.y_center = y_center
        self.lenght_x = lenght_x
    def parametrs_of_figure(self):
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        perimeter = round((2*math.pi*lenght_x), 2)
        area = round((math.pi*(lenght_x**2)), 2)
        return "периметр круга = " + str(perimeter) + ", а его площадь = " + str(area)
    def draw_figure(self, color):
        self.color = color
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        turtle.penup()
        turtle.setpos (x_center, y_center)
        turtle.pendown()
        turtle.pencolor(color)
        turtle.circle(lenght_x)
        turtle.penup()

class rectangle(figure):
    def __init__(self, x_center, y_center, lenght_x, lenght_y):
        self.x_center = x_center
        self.y_center = y_center
        self.lenght_x = lenght_x
        self.lenght_y = lenght_y
    def parametrs_of_figure(self):
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        lenght_y = int(self.lenght_y)
        perimeter = 2 * (lenght_x + lenght_y)
        area = lenght_x * lenght_y
        return "периметр прямоугольника = " + str(perimeter) + ", а его площадь = " + str(area)
    def draw_figure(self, color):
        self.color = color
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        lenght_y = int(self.lenght_y)
        turtle.home()
        turtle.penup()
        turtle.setpos (x_center, y_center)
        turtle.pendown( )
        turtle.pencolor(color)
        turtle.forward(lenght_x)
        turtle.left(90)
        turtle.forward(lenght_y)
        turtle.left(90)
        turtle.forward(lenght_x)
        turtle.left(90)
        turtle.forward(lenght_y)
        turtle.penup()

class triangle(figure):
    def __init__(self, x_center, y_center, lenght_x, lenght_y):
        self.x_center = x_center
        self.y_center = y_center
        self.lenght_x = lenght_x
        self.lenght_y = lenght_y
    def parametrs_of_figure(self):
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        lenght_y = int(self.lenght_y)
        perimeter = math.trunc(lenght_x + 2 * math.hypot(lenght_x/2, lenght_y))
        area = math.trunc(lenght_x * lenght_y / 2)
        return "периметр треугольника = " + str(perimeter) + ", а его площадь = " + str(area)
    def draw_figure(self, color):
        self.color = color
        x_center = int(self.x_center)
        y_center = int(self.y_center)
        lenght_x = int(self.lenght_x)
        lenght_y = int(self.lenght_y)
        turtle.home()
        turtle.setpos (x_center, y_center)
        turtle.pendown( )
        turtle.pencolor(color)
        turtle.forward(lenght_x)
        turtle.setpos (x_center + lenght_x / 2, y_center + lenght_y)
        turtle.setpos (x_center, y_center)
        #turtle.mainloop()

# circle_first = circle(50, 50, 35)
# print (circle_first.parametrs_of_figure())
# circle_first.draw_figure('red')

# rectangle_first = rectangle(50,50,100,80)
# print (rectangle_first.parametrs_of_figure())
# rectangle_first.draw_figure('yellow')

# triangle_first = triangle(-100, 1, 50, 60)
# print (triangle_first.parametrs_of_figure())
# triangle_first.draw_figure('blue')

def task_1(x_start, y_start , lenght_of_side, step):
    turtle.reset() 
    turtle.pendown()
    for elem in range(1, round(lenght_of_side/2/step)+1):
        rectangular_for_drawing = rectangle(x_start, y_start, lenght_of_side, lenght_of_side)
        rectangular_for_drawing.draw_figure('blue')
        x_start = x_start + step
        y_start = y_start + step
        lenght_of_side = lenght_of_side - 2 * step

task_1(-150, -150, 300, 20)

def task_2(number_of_angle, Radius):
    turtle.reset() 
    turtle.pendown()
    for elem in range(1, number_of_angle + 1):
        circle_for_drawing = circle(0, 0, Radius)
        circle_for_drawing.draw_figure('red')
        turtle.right(360 / number_of_angle)

task_2(6, 50)

def task_3(n,R,l):
    turtle.reset() 
    turtle.pendown()
    turtle.left(90)
    for elem in range(1, n + 1):
        circle_for_drawing = circle(0, 0, R)
        circle_for_drawing.draw_figure('red')
        turtle.right(180)
        circle_for_drawing.draw_figure('red')
        turtle.right(180)
        R = R + l
    turtle.speed(10)
    turtle.mainloop()

task_3(10, 50, 10)