import threading
import time
# Threading is useful when you want your computer to do other task while it's asleep
print("Start Program")
def takeNap():
    time.sleep(5)
    print("Wake Up")

threadObj = threading.Thread(target=takeNap)
threadObj.start()
#  Passing Arguments to the Thread’s Target Function
print("End Of Program")
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],kwargs={'sep': ' & '})
threadObj.start()
print("End Of Program")
#  an incorrect way to create the newthread that calls print():  threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
# NB: What happened here was a concurrency error






