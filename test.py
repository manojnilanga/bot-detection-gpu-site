from datetime import datetime, timedelta

# datetime object containing current date and time
now = datetime.now()

print("now =", now)
print(now)

now_plus_10 = now + timedelta(seconds = 10)
print(now_plus_10)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)