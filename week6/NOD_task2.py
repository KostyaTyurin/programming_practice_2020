mnogestvo = list(map(int, input('Введите множество чисел ').split()))
sorted(mnogestvo)
d = list(set(mnogestvo))
m = []
for i in d:
    m.append(int(i))

m.sort()
print(m)


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    nod1 = a + b
    return print('NOD (', m[i], ',', m[k], ') - ', nod1)


for i in range(len(m)):
    for k in range(i + 1, len(m)):
        a = m[i]
        b = m[k]
        nod(a, b)




