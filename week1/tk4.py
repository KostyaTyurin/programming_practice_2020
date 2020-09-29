v = float(input('Введите скорость движения '))
t = float(input("Введите время движения "))
if v<0:
    rez = int(((v*t)%109))
elif v>0:
    rez = (v*t)%109
print(int(rez))