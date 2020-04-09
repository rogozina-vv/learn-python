import types_of_shapes
set_of_shapes = []
def data_entry():
    n = int(input ("Я могу нарисовать столько фигур, сколько хочешь... только скажи сколько?"))
    for i in range(1, n+1):
        type_of_figure = int(input("1 - Круг, 2 - Прямоугольник, 3 - Треугольник. Выбирай?"))
        if type_of_figure == 1:
            x, y, r = (int(j) for j in input('Введи через прообел координаты начальной точки и радиус').split())
            set_of_shapes.append(types_of_shapes.circle(x, y, r))
        elif type_of_figure == 2:
            x, y, a, b = (int(j) for j in input('Введи через прообел координаты начальной точки, длину и ширину').split())
            set_of_shapes.append(types_of_shapes.rectangle(x, y, a, b))
        else:
            x, y, a, b = (int(j) for j in input('Введи через прообел координаты начальной точки, длину основания и высоту').split())
            set_of_shapes.append(types_of_shapes.triangle(x, y, a, b))
