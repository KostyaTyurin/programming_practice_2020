import numpy as np


def krug(r):
    return np.pi * r ** 2


def square(a, b):
    return a * b


def triangle(c, h):
    return 0.5 * c * h

a = input('What are you gonna count (triangle, square, circle?) ')

if a == 'triangle':
    c = int(input(' длина = '))
    h = int(input('высота = '))
    print(triangle(c, h))


if a == 'square':
    a = int(input('ширина = '))
    b = int(input('длина = '))
    print(square(a, b))


if a == 'circle':
    r = float(input(' радиус = '))
    print(krug(r))