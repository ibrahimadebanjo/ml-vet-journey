# Simple balance parenthesis algorithm using stack
from stack01 import Stack
def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(" :
            s.push(symbol)
        elif s.is_empty():
            balanced = False
        else:
            s.pop()

        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False
print(par_checker("((()))"))    
print(par_checker("(()"))                    