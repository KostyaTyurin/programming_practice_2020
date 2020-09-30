n = int(input())  # количество обьектов в списке
a = []
for i in range(n):
    a.append(int(input()))
b = 0
for c in range(1,n-1):
    if a[c] > a[c - 1] and a[c] > a[c + 1]:
        b = b + 1
print(b)





