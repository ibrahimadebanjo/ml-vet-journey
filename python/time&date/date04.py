import time, datetime

startTime = datetime.datetime(2029, 10, 30, 0, 0, 0)
while datetime.datetime.now() < startTime:
    print("Looping")
    time.sleep(1)
print("Program now starting on Halloween 2029")
# Threading

