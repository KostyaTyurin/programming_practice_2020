a = list(map(int, input().split()))
b =[]
for num in a:
    if num in b:
        print(num, '- YES')
    else:
        print(num, '- NO')
        b.append(num)
