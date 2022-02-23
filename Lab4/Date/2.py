from datetime import date, timedelta
now = date.today()
for i in range(1, -2,  -1):
    print(now - timedelta(days=i))