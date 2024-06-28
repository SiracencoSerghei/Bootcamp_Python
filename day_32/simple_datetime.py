import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)
print(year)
print(type(now))

day_of_week = now.weekday()
print(f"{day_of_week = }")

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(f"{date_of_birth = }")
date_of_birth = date_of_birth.strftime("%Y-%m-%d")
print(f"{date_of_birth = }")
