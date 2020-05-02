import types_of_shapes
import math 
import turtle
def drawing_shapes(sos,n):
    for i in range(0,n):
        if math.fmod(i, 2) == 1:
            sos[i].draw_figure('blue')
        else:
            sos[i].draw_figure('red')
    turtle.mainloop()
