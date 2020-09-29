def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
a = list(map(float, input().split()))
print(distance(a[0],a[1],a[2],a[3]))
