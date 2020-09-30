a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = len(a)
m = len(b)
c = []
for i in range(n):
    for j in range (m):
        if a[i]==b[j]:
            c.append(int(a[i]))

list.sort(c)
print(c)