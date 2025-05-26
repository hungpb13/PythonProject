# Date & Time

import datetime

date = datetime.date(2025, 1, 1)
print(f"Date: {date}")

today = date.today()
print(f"Today: {today}")

time = datetime.time(12, 30, 30)
print(f"Time: {time}")

now = datetime.datetime.now()

# Format datetime
pattern = "%H:%M:%S %d/%m/%Y"
now = now.strftime(pattern)

print(f"Now: {now}")

target_datetime = datetime.datetime(2020, 1, 1, 12, 0, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

# Parse String to Date
date_str = "26-05-2025"
parsed_date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print(f"Parsed date: {parsed_date.strftime(pattern)}")

# Doing Date Arithmetic (Timedelta)
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print(f"Yesterday: {yesterday.strftime(pattern)}")
