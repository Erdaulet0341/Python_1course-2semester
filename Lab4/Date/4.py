from datetime import datetime, date, timedelta
from random import randrange
random_sec = randrange(0,59)
now =datetime.now()
k = now + timedelta(seconds = random_sec)
print(f"current time = {now}")
print(f"After random = {k}")