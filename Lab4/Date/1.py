from asyncio import current_task
from datetime import datetime, timedelta, date
cur_dat = date.today()
print(f"Today is: {cur_dat}")
n = cur_dat - timedelta(days = 5 )
print(f"Before 5 days: {n}")