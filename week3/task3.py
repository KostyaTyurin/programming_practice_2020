a= list(map(int, input().split()))
n = len(a)
b=0
for i in range(n):
    for j in range(n):
        if i!=j and a[i]==a[j]:
           b=(b+1)
d=b//2
print(d)
