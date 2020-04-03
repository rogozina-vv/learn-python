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
        turtle.home()
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
        turtle.penup()
        turtle.home()
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
        turtle.penup()
        turtle.home()
        turtle.setpos (x_center, y_center)
        turtle.pendown()
        turtle.pencolor(color)
        turtle.forward(lenght_x)
        turtle.setpos (x_center + lenght_x / 2, y_center + lenght_y)
        turtle.setpos (x_center, y_center)
        #turtle.mainloop()

set_of_shapes = []
# 1 - Ввод данных
def data_entry():
    n = int(input ("Я могу нарисовать столько фигур, сколько хочешь... только скажи сколько?"))
    for i in range(1, n+1):
        type_of_figure = int(input("1 - Круг, 2 - Прямоугольник, 3 - Треугольник. Выбирай?"))
        if type_of_figure == 1:
            x, y, r = (int(j) for j in input('Введи через прообел координаты начальной точки и радиус').split())
            set_of_shapes.append(circle(x, y, r))
        elif type_of_figure == 2:
            x, y, a, b = (int(j) for j in input('Введи через прообел координаты начальной точки, длину и ширину').split())
            set_of_shapes.append(rectangle(x, y, a, b))
        else:
            x, y, a, b = (int(j) for j in input('Введи через прообел координаты начальной точки, длину основания и высоту').split())
            set_of_shapes.append(triangle(x, y, a, b))

data_entry()

# Для проверки удобнее использовать это
# f1 = circle(20, -40, 49)
# f2 = rectangle(100, 0, 200, 50)
# f3 = rectangle(90, 10, 250, 10)
# f4 = circle(20 , 10, 60)
# f5 = triangle(-20, -20, 70, 80)
# f6 = triangle(40, 20, 60, 45)
# set_of_shapes = [f1, f2, f3, f4, f5, f6]

n = len(set_of_shapes)

# 2 - Отрисовка фигур
def drawing_shapes():
    for i in range(0,n):
        if math.fmod(i, 2) == 1:
            set_of_shapes[i].draw_figure('blue')
        else:
            set_of_shapes[i].draw_figure('red')

drawing_shapes()

# 3 - Проверка пересечений с помощью функции test
def test(a, b): #проверяем пересекается ли пара фигур
    if a.__class__.__name__ == b.__class__.__name__ == "circle":
        #проверяем расстояние между центрами
        if math.fabs(a.lenght_x - b.lenght_x) <= math.sqrt((a.x_center - b.x_center) ** 2 + (a.y_center + a.lenght_x - b.y_center - b.lenght_x) ** 2) <= (a.lenght_x + b.lenght_x):
            print ('Окружности пересекаются')
        else:
            print ('Окружности НЕ пересекаются')

    elif a.__class__.__name__ == b.__class__.__name__ == "rectangle":
        x1 = a.x_center
        y1 = a.y_center
        lx1 = a.lenght_x
        ly1 = a.lenght_y
        x2 = b.x_center
        y2 = b.y_center
        lx2 = b.lenght_x
        ly2 = b.lenght_y
        #от противного: сначала условие непересечения каждой из сторон, затем два частных случая внутри и снаружи
        usl_up = y1 + ly1 < y2 
        usl_down = y2 + ly2 < y1 
        usl_right = x1 + lx1 < x2
        usl_left = x2 + lx2 < x1
        usl_in = (x1 < (x2 and (x2 + lx2)) < (x1 + lx1)) and (y1 < (y2 and (y2 + ly2)) < (y1+ly1)) 
        usl_out = (x2 < (x1 and (x1 + lx1)) < (x2 + lx2)) and (y2 < (y1 and (y1 + ly1)) < (y2+ly2)) 
        if usl_up or usl_down or usl_right or usl_left or usl_in or usl_out:
            print ("Прямоугольники НЕ пересекаются")
        else:
            print ("Прямоугольники пересекаются")

    elif a.__class__.__name__ == "circle" and b.__class__.__name__ == "rectangle" or b.__class__.__name__ == "circle" and a.__class__.__name__ == "rectangle":
        if b.__class__.__name__ == "circle":
            xc = b.x_center # a -  прямоугольник
            yc = b.y_center + b.lenght_x
            rad = b.lenght_x
            xr = a.x_center
            yr = a.y_center
            xlen = a.lenght_x
            ylen = a.lenght_y
        else: # a - круг
            xc = a.x_center
            yc = a.y_center + a.lenght_x
            rad = a.lenght_x
            xr = b.x_center
            yr = b.y_center
            xlen = b.lenght_x
            ylen = b.lenght_y
        # расстояния от центра окружности до каждой из вершин прямоугольника
        r_first = math.sqrt((xr - xc) ** 2 + (yr - yc) ** 2)
        r_second = math.sqrt((xr + xlen - xc) ** 2 + (yr - yc) ** 2) 
        r_third = math.sqrt((xr + xlen - xc) ** 2 + (yr + ylen - yc) ** 2) 
        r_fourth = math.sqrt((xr - xc) ** 2 + (yr + ylen - yc) ** 2)
        # расстояния от центра окружности до сторон прямоугольника
        r_horyzont = math.fabs(yc - yr) or math.fabs(yr + ylen - yc)
        r_vertical = math.fabs(xc - xr) or math.fabs(xr + xlen - xc)
        #условия пересечения
        # окружность пересекает сторону || оси X
        usl_X = xr < xc < (xr + xlen) and r_horyzont < rad < (r_first and r_second and r_third and r_fourth)
        # окружность пересекает сторону || оси Y
        usl_Y = yr < yc < (yr + ylen) and r_vertical < rad < (r_first and r_second and r_third and r_fourth)
        # окружность содержит хотя бы одну вершину, но не все
        usl_top = (r_first < rad or r_second < rad or r_third < rad or r_fourth < rad) and (rad < r_first or rad < r_second or rad < r_third or rad < r_fourth) 
        if  usl_X or usl_Y or usl_top:
            print ("Прямоугольник и окружность пересекаются ")
        else:
            print ("Прямоугольник и окружность НЕ пересекаются")

    elif a.__class__.__name__ == b.__class__.__name__ == "triangle":
        x1 = a.x_center
        y1 = a.y_center
        lx1 = a.lenght_x
        ly1 = a.lenght_y
        x2 = b.x_center
        y2 = b.y_center
        lx2 = b.lenght_x
        ly2 = b.lenght_y
                #действуем от противного и рассомтрим случаи, когда треугольники точно не пересекутся
        #последовательно: второй треугольник не пересекает первый с каждой из трех сторон и два частных, когда один внутри другого
        #верхушка второго ниже дна первого
        usl_down = y2 + ly2 < y1  
        # левая вершина основания второго тр. находится выше правой боковой стороны первого тр.(псевдоскалярное произвдение)
        usl_right = y1 < y2 < y1 + ly1 and ((-1 / 2 * lx1) * (y2 - y1) - (x2 - x1 - lx1) * ly1) < 0 
        # правая вершина основания второго тр. находтся выше левой боковой стороны первого тр.(псевдоскалярное произвдение)
        usl_left = y1 < y2 < y1 + ly1 and ((1 / 2 * lx1) * (y2 - y1) - (x2 - x1 + lx2) * ly1) > 0 
        # треугольник содержит второй тр.
        right_scal_in = (-lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 - x1 - lx1)) > 0 and (-lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 / 2 - x1 - lx1)) > 0 
        left_scal_in = (lx1 / 2 * (y2 - y1) - ly1 * (x2 - x1)) < 0 and (lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 / 2 - x1)) < 0
        usl_in = right_scal_in and left_scal_in and y1 < y2
        #треугольник внутри второго треугольника
        right_scal_out = (-lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 - x1 - lx1)) < 0 and (-lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 / 2 - x1 - lx1)) < 0 
        left_scal_out = (lx1 / 2 * (y2 - y1) - ly1 * (x2 - x1)) > 0 and (lx1 / 2 * (y2 + ly2 - y1) - ly1 * (x2 + lx2 / 2 - x1)) > 0
        usl_out = right_scal_out and left_scal_out and y1 > y2
        if usl_down or usl_left or usl_right or usl_in or usl_out:
            print ('Треугольники НЕ пересекаются')
        else:
            print ('Треугольники пересекаются')
    
    elif a.__class__.__name__ == "rectangle" and b.__class__.__name__ == "triangle" or b.__class__.__name__ == "rectangle" and a.__class__.__name__ == "triangle":
        if a.__class__.__name__ == "rectangle":
            xr = a.x_center
            yr = a.y_center
            lxr = a.lenght_x
            lyr = a.lenght_y
            xt = b.x_center
            yt = b.y_center
            lxt = b.lenght_x
            lyt = b.lenght_y 
        else:
            xt = a.x_center
            yt = a.y_center
            lxt = a.lenght_x
            lyt = a.lenght_y
            xr = b.x_center
            yr = b.y_center
            lxr = b.lenght_x
            lyr = b.lenght_y 
        # от противного, рассматривая прямоугольник : сначала условия пересечения сторон ближайшей вершиной тр. снаружи, затем два частных случая непересечения, когда фигура внутри
        #верхушка треугольника ниже дна прямоугольника
        usl_down = yt + lyt < yr 
        #дно треугольника выше верха прямоугольника
        usl_up = yr + lxr < yt
        #треугольник не заходит в прямоугольник справа
        usl_right = xr + lxr < xt
        #треугольник не заходит в прямоугольник слева
        usl_left = xt + lxt < xr
        #треугольник внутри 
        usl_tr_in = xr < xt and xt + lxt < xr + lxr and yt + lyt < yr + lyr
        #прямоугольник внутри (низ через координаты, верх через псевдоскалярное)
        usl_rec_in = yt < yr and xt < xr and xr + lxr < xt + lxt and ((-1 / 2 * lxt) * (yr + lyr - yt) - (lyt * (xr - xt + lxr - lxt))) > 0 and ((1 / 2 * lxt) * (yr + lyr - yt) - (lyt * (xr - xt))) < 0 
        if usl_up or usl_down or usl_left or usl_right or usl_tr_in or usl_rec_in:
            print ('Треугольник и прямоугольник НЕ пересекаются')
        else:
            print ('Треугольник пересекает прямоугольник')
    else: 
        if a.__class__.__name__ == "circle":
            xc = a.x_center
            yc = a.y_center + a.lenght_x
            rad = a.lenght_x
            xt = b.x_center
            yt = b.y_center
            lxt = b.lenght_x
            lyt = b.lenght_y
        else:
            xc = b.x_center
            yc = b.y_center + b.lenght_x
            rad = b.lenght_x
            xt = a.x_center
            yt = a.y_center
            lxt = a.lenght_x
            lyt = a.lenght_y
        r_first =  math.sqrt((xc - xt) ** 2 + (yc - yt) ** 2)
        r_second = math.sqrt((xc - xt - lxt) ** 2 + (yc - yt) ** 2)
        r_third = math.sqrt((xc - xt - lxt / 2) ** 2 + (yc - yt - lyt) ** 2)
        # расстояние от центра окружности до правой стороны треугольника
        r_right_side = ((-lxt / 2 * (yc-yt)) - (lxt * (xc - xt -lxt))) / 2 / math.sqrt((-lxt/2) ** 2 + lxt ** 2)
        r_left_side = (lxt * (yc - yt) - lyt * (xc - xt)) / 2 / math.sqrt((lxt / 2) **2 + lyt ** 2) 
        #проверка попадания перпендикуляра из центра окружности на стороны
        r_right_scal = (- lxt/2 * (xc - xt - lxt) + lxt * (yc - yt)) > 0 and ((lxt / 2 * (xc - xt - lxt /2) - lyt * (yc - yt -lyt))) > 0
        r_left_scal = ((lxt / 2 * (xc - xt) + lyt * (yc - yt))) > 0 and (-lxt / 2 * (xc - xt - lxt / 2) - lyt * (yc - yt - lyt)) > 0
        # условия пересечение сторон
        usl_down = xt < xc < xt + lxt and math.fabs(yc - yt) < rad < (r_first or r_second or r_third) 
        usl_right = r_right_side < rad < (r_first or r_second or r_third) and r_right_scal
        usl_left = r_left_side < rad < (r_first or r_second or r_third) and r_left_scal
        # условие содержания окружностью одной или двух вершин
        usl_top = (r_first or r_second or r_third) < rad < (r_first or r_second or r_third)
        if usl_down or usl_left or usl_right or usl_top:
            print ('Треугольник и окружность пересекаются')
        else:
            print ('Треугольник и окружность НЕ пересекаются')

def test_of_shapes(): #проходимся по списку
    s = n
    for i in range(0, n):
        for j in range (1, s):
            a = set_of_shapes[i]
            b = set_of_shapes[i + j]
            print ('Результат по фигурам №', i + 1, ' и №' , i + j + 1)
            test(a,b)
        s = s - 1    

test_of_shapes()

#предыдущие задания:

# circle_first = circle(50, 50, 35)
# print (circle_first.parametrs_of_figure())
# circle_first.draw_figure('red')

# rectangle_first = rectangle(50,50,100,80)
# print (rectangle_first.parametrs_of_figure())
# rectangle_first.draw_figure('yellow')

# triangle_first = triangle(-100, 1, 50, 60)
# print (triangle_first.parametrs_of_figure())
# triangle_first.draw_figure('blue')

# def task_1(x_start, y_start , lenght_of_side, step):
#     turtle.reset() 
#     turtle.pendown()
#     for elem in range(1, round(lenght_of_side/2/step)+1):
#         rectangular_for_drawing = rectangle(x_start, y_start, lenght_of_side, lenght_of_side)
#         rectangular_for_drawing.draw_figure('blue')
#         x_start = x_start + step
#         y_start = y_start + step
#         lenght_of_side = lenght_of_side - 2 * step

# task_1(-150, -150, 300, 20)

# def task_2(number_of_angle, radius):
#     turtle.reset() 
#     turtle.pendown()
#     for elem in range(1, number_of_angle + 1):
#         circle_for_drawing = circle(0, 0, radius)
#         circle_for_drawing.draw_figure('red')
#         turtle.right(360 / number_of_angle)

# task_2(6, 50)

# def task_3(number_of_angle, radius, step):
#     turtle.reset() 
#     turtle.pendown()
#     turtle.left(90)
#     for elem in range(1, number_of_angle + 1):
#         circle_for_drawing = circle(0, 0, radius)
#         circle_for_drawing.draw_figure('red')
#         turtle.right(180)
#         circle_for_drawing.draw_figure('red')
#         turtle.right(180)
#         radius = radius + step
#     turtle.speed(10)
#     turtle.mainloop()

# task_3(10, 50, 10)