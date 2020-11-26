import numpy as np
from numpy import linalg as la


class vector(object):

    def __init__(self, x):
        self.matrix = np.array(x)

        print('Создан объект класса')

    def __add__(self, other):
        if not isinstance(other, vector):
            raise ValueError('объект не принадлежит классу')
        if np.shape(self.matrix) != np.shape(other.getmatrix()):
            raise ValueError('Векторы имеют разные размеры')

        return vector(np.array(self.matrix + other.getmatrix()))

    def __mul__(self, skalyar):

        return vector(self.matrix * skalyar)

    def __pow__(self, other):
        if not isinstance(other, vector):
            raise ValueError('объект не принадлежит классу')

        if np.shape(self.matrix) != np.shape(other.getmatrix()):
            raise ValueError('Векторы имеют разные размеры')

        skoal_mul = 0
        for i in range(len(self.matrix)):
            skoal_mul += self.matrix[i] + other.getmatrix()[i]

        return vector(skoal_mul)

    def __abs__(self):
        num = 0
        for i in self.matrix:
            num += i ** 2
        num = np.sqrt(num)

        return vector(num)

    def __mod__(self, other):
        result = []
        if not isinstance(other, vector):
            raise ValueError('объект не принадлежит классу')

        if np.shape(self.matrix) != np.shape(other.getmatrix()):
            raise ValueError('Векторы имеют разные размеры')
        if np.shape(self.matrix) != (3,):
            raise ValueError('Данные векторы нельзя перемножить поскольку они не соответсвуют (1,3)')

        res1 = la.det([self.matrix[-2:], other.getmatrix()[-2:]])
        result.append(res1)

        res2 = la.det([other.getmatrix()[0:3:2], self.matrix[0:3:2]])
        result.append(res2)

        res3 = la.det([self.matrix[:2], other.getmatrix()[:2]])
        result.append(res3)

        return vector(np.array(result))

    def getmatrix(self):

        return self.matrix


a = vector([1, 2, 3, 4, 5, 5])
b = vector([1, 2, 3, 4, 5, 6])
vect1 = vector([2, 3, 4])
vect2 = vector([56, 0, 0])

vect3 = vect1 % vect2
d = a * 5
e = a + b


print(d.getmatrix(), vect3.getmatrix())
