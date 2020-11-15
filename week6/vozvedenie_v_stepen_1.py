d = 1


def power(a, n, d):

    if n > 0:
        for i in range(n):
            d *= a
    if n < 0:
        for i in range(abs(n)):
            d /= a

    if n == 0:
        d = 1

    return d

a = float(input('Введите действительное положительное число a = '))

n = int(input('Введите целое число n = '))
if a < 0:
    print('Попробуйте снова a = ')
    a = float(input())

print(power(a, n, d))

