import types_of_shapes
import math
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
        r_down = math.fabs(yc - yr) 
        r_up = math.fabs(yr + ylen - yc)
        r_left = math.fabs(xc - xr) 
        r_right = math.fabs(xr + xlen - xc)
        #условия пересечения
        # окружность пересекает сторону || оси X
        usl_X = (xr < xc < (xr + xlen)) and ((r_down < rad < (r_first and r_second)) or (r_up < rad < (r_third and r_fourth)))
        # окружность пересекает сторону || оси Y
        usl_Y = (yr < yc < (yr + ylen)) and ((r_left < rad < (r_first and r_fourth)) or r_right < rad < (r_second and r_third))
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
        # от противного, рассм.прямоугольник : сначала условия пересечения сторон ближайшей вершиной тр. снаружи, 
        # затем два частных случая непересечения, когда фигура внутри
        #верхушка треугольника ниже дна прямоугольника
        usl_down = yt + lyt < yr 
        #дно треугольника выше верха прямоугольника
        usl_up = yr + lyr < yt
        #треугольник не заходит в прямоугольник справа
        usl_right = xr + lxr < xt
        #треугольник не заходит в прямоугольник справа-снизу.
        scal_right1 = (lxt * (xr + lxr - xt) + lyt * (yr - yt)) > 0 #условие что перпенд. с 2 верш. прям. падает на левую сторону треуг.
        scal_right2 = (- lxt / 2 * (xr + lxr - xt - lxt / 2) - lyt * (yr - yt - lyt)) > 0 # через скалярное промзведение
        len_right = (lxt / 2 * (yr - yt) - lyt * (xr + lxr - xt))  > 0 #тр. ниже 
        usl_right_down = (xt <= xr + lxr <= xt + lxt / 2) and ( yt <= yr <= yt + lyt) and scal_right1 and scal_right2 and len_right
        #треугольник не заходит в прямоугольник слева
        usl_left = xt + lxt < xr
        #треугольник не заходит в прямоугольник слева-снизу.
        scal_left1 = (- lxt / 2 * (xr - xt - lxt) + lyt * (yr - yt)) > 0
        scal_left2 = (lxt / 2 * ( xr - xt - lxt / 2) - lyt * (yr - yt - lyt / 2)) > 0
        len_left = (- lxt / 2 * (yr - yt) - lyt * (xr - xt - lxt)) < 0 #тр. ниже 
        usl_left_down = (xt + lxt / 2 <= xr <= xt + lxt) and ( yt <= yr <= yt + lyt) and scal_left1 and scal_left2 and len_left
        #треугольник внутри 
        usl_tr_in = xr < xt and xt + lxt < xr + lxr and yt + lyt < yr + lyr
        #прямоугольник внутри (низ через координаты, верх через псевдоскалярное)
        usl_rec_in = yt < yr and xt < xr and xr + lxr < xt + lxt and (lxt / 2  * (yr + lyr - yt) - lyt * (xr - xt )) < 0 and ((- lxt / 2) * (yr + lyr - yt) - lyt * (xr + lxr - xt - lxt)) > 0 
        if usl_up or usl_down or usl_left or usl_right or usl_tr_in or usl_rec_in or usl_right_down or usl_left_down:
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
        # расстояние от центра окружности до вершин треугольника +
        r_first =  math.sqrt((xc - xt) ** 2 + (yc - yt) ** 2)
        r_second = math.sqrt((xc - xt - lxt) ** 2 + (yc - yt) ** 2)
        r_third = math.sqrt((xc - xt - lxt / 2) ** 2 + (yc - yt - lyt) ** 2)
        # расстояние от центра окружности до стороны треугольника (через формулы площадей треугольников: псевдоскаляр и основание на высоту)
        r_right_side = ((-lxt / 2 * (yc-yt)) - (lyt * (xc - xt -lxt))) / math.sqrt((-lxt/2) ** 2 + lyt ** 2)
        r_left_side = (lxt / 2 * (yc - yt) - lyt * (xc - xt)) / math.sqrt((lxt / 2) **2 + lyt ** 2) 
        # проверка попадания перпендикуляра из центра окружности на стороны
        r_right_scal = (- lxt/2 * (xc - xt - lxt) + lyt * (yc - yt)) > 0 and ((lxt / 2 * (xc - xt - lxt /2) - lyt * (yc - yt -lyt))) > 0
        r_left_scal = ((lxt / 2 * (xc - xt) + lyt * (yc - yt))) > 0 and (-lxt / 2 * (xc - xt - lxt / 2) - lyt * (yc - yt - lyt)) > 0
        # условия пересечение сторон
        usl_down = xt < xc < xt + lxt and math.fabs(yc - yt) < rad < (r_first or r_second or r_third) 
        usl_right = (r_right_side < rad < (r_first or r_second or r_third)) and r_right_scal
        usl_left = (r_left_side < rad < (r_first or r_second or r_third)) and r_left_scal
        # условие содержания окружностью одной или двух вершин
        usl_top = (r_first or r_second or r_third) < rad < (r_first or r_second or r_third)
        if usl_down or usl_left or usl_right or usl_top:
            print ('Треугольник и окружность пересекаются')
        else:
            print ('Треугольник и окружность НЕ пересекаются')

def test_of_shapes(sos, n): #проходимся по списку
    s = n
    for i in range(0, n):
        for j in range (1, s):
            a = sos[i]
            b = sos[i + j]
            print ('Результат по фигурам №', i + 1, ' и №' , i + j + 1)
            test(a,b)
        s = s - 1    
