import datetime
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# Converting string dates to datetime Object
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))

