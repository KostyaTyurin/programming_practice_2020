n = int(input())
rez = 0
b = 1
for i in range(n):
    b *= i+1
    rez += b
print(rez)