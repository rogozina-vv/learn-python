import types_of_shapes
import pickle
set_of_shapes = []
def data_entry():
    global set_of_shapes
    var = int(input("Итак, ты хочешь: 1 - Ввести параметры фигур вручную; 2 - Посмотреть на рабуту программы с готовыми фигурами"))
    if var == 1:
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
        with open('data.pickle','wb') as f:
            s = set_of_shapes
            pickle.dump(s, f)
    else:
        with open('data.pickle', 'rb') as f:
            set_of_shapes = pickle.load(f)