n = int(input('введите количество минут' ))
days = n//(60*24)
hours = (n-60*24*days)//60
minutes = (n- 60*24*days-60*hours)
print(days, 'days', hours, 'hours', minutes, 'minutes')