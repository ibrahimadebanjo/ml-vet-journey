# The time.time() function
import time, sys
print(time.time())
#  measure how long a piece of code takes to run.


def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i

    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(sys.set_int_max_str_digits((prod)))))
print('Took %s seconds to calculate.' % (endTime - startTime))
