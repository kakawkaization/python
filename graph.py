import calendar

w = 0
h = 0
days_num = (calendar.monthrange(2018,9)[1])

days = {x + 1: x + 1 for x in range(days_num)}

l_days = list(days.keys())
for a in l_days[1::4]:
    days[a] = 'work:day'
    w += +1
for a in l_days[2::4]:
    days[a] = 'work:night'
    w += +1
for a in l_days[::4]:
    days[a] = 'home:second'
    h += +1
for a in l_days[3::4]:
    days[a] = 'home:first'
    h += +1

n = input('Enter number of day: ')

print(days[int(n)])
print('Work days in month: ' + str(w))
print('Weekend days in month: ' + str(h))
