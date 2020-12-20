import math

shape_of_the_figure = (input())
size = float(input())

if shape_of_the_figure == "square":
    a = size
    area = a * a
elif shape_of_the_figure == "rectangle":
    a = size
    size2 = float(input())
    b = size2
    area = a * b
elif shape_of_the_figure == "circle":
    r = size
    area = math.pi * (r ** 2)
elif shape_of_the_figure == "triangle":
    a = size
    size2 = float(input())
    h = size2
    area = a * h / 2

print(f"{area: .3f}")