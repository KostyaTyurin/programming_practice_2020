dict = {}
n = int(input())
for i in range(n):
    a = input().split()
    if not a[0] in dict:
        dict[a[0]] = {a[1]:a[2]}
    else:
        if not a[1] in dict[a[0]].keys():
            dict[a[0]].update({a[1]: a[2]})


for x in sorted(dict.keys()):
    for y in sorted(dict[x].keys()):
        print (x,':',y, dict[x][y])
print(dict)