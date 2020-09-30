a = []
n = int(input())
for i in range(n):
    a.append(input())
a.sort()
s = str()
num = 0
num1 = 0
b = set(a)
for i in b:
    num1 = a.count(i)
    if num<num1:
        num = num1
        s = i
print(s, num)