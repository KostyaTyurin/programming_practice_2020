text = input('Введите текст ')
n = int(input(' Введите количество повторов '))
text1 = []
for i in range(n):
    text1.append(text)
print('Hello,', ', '.join(text1))