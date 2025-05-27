# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
#  Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner
# or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
# sure why. Your program is exploring what’s called the Collatz sequence, some
# times called “the simplest impossible math problem.”)
#  Remember to convert the return value from input() to an integer with
# the int() function; otherwise, it will be a string value.
#  Hint: An integer number is even if number % 2 == 0, and it’s odd if
# number % 2 == 1.

# def callatz(number):
#     if number % 2 == 0:
#         print(str(number))
#     if number % 2 != 0:
#         return 3 * number + 1


# print("Enter a Number")
# number = int(input())
# if number % 2 == 1:
#     print("It is an odd number and the output is 1")
# else:
#     callatz(number)


# # deepseek correction
# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#     else:
#         result = 3 * number + 1
#     print(result)
#     return result

# print("Enter a number:")

# try:
#     number = int(input())
#     while number != 1:
#         number = collatz(number)
# except ValueError:
#     print("Error: You must enter a number.")
 
# 2 
def collatz(number):
    """Calculate the next number in the Collatz sequence."""
    if number % 2 == 0:  # Even number
        result = number // 2
    else:  # Odd number
        result = 3 * number + 1
    print(result)
    return result

def main():
    print("Enter a positive integer to start the Collatz sequence:")
    
    while True:
        try:
            number = int(input())
            if number <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Error: You must enter a valid integer (e.g., 5, 12).")

    # Generate Collatz sequence until reaching 1
    while number != 1:
        number = collatz(number)

if __name__ == "__main__":
    main()

    
