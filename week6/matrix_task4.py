def main(matrix):
    return print(sum(matrix[i][i] for i in range(len)))


def not_main(matrix):

    return print(sum(matrix[i][len - 1 - i] for i in range(len)))



matrix = []
len = int(input())
for i in range(len):
    matrix.append([])
    k = list(map(int, input().split()))
    for j in range(len):
        matrix[i].append(k[j])



text = input('Что собираемся считать: сумму главной (main) или побочной диагонали (not main)? ')
if text == 'main':
    main(matrix)

elif text == 'not main':
    not_main(matrix)

