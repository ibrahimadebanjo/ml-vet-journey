import datetime
import time
# By using a while loop and time.sleep() method you can pause your programs until a specific date.

halloween2016 = datetime.datetime(2026, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    print("looping")
    time.sleep(1)
