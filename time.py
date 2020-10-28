import datetime


t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
y = '2020-10-25 00:00:00.000002'
z = '2020-10-25 00:00:00'

print(y < z)