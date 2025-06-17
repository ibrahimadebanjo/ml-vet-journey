import datetime
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

# For example, to calculate the date 1,000 days from now,
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

# timedelta object can be sutracted or added using + and - operator
# They can also be multiplied or divided by an integer using * and \ operator
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)

print(oct21st - (2 * aboutThirtyYears))
print(oct21st)




