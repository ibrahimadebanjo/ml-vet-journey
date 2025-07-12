# Doing algorithm aalysis with time of execution
import time

def sum_of_n_2(n):
    start = time.time()

    sum = 0
    for i in range(1,n - 1):
        sum += i

    end = time.time()

    return sum, end-start

print(sum_of_n_2(4))   
print() 

def sum_of_n_3(n):
 return (n * (n + 1)) / 2
print(sum_of_n_3(4))

