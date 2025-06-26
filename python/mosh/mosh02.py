# Nesting loop
# it can be used to generate a list of coordinates(x,y)
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
# outer loop run once first then inner loop runs till it
# completes it's looping, then loop again through outer loop once then inner loop till it completes
# like that till the outer loop is over
# exercise
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
# Exercise
numbers = [7, 4, 5, 6, 7, 9]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

#  three dimentional list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# accessing inner list
print(matrix[0][1])  # this represent index of 2
# looping
for row in matrix:
    for item in row:
        print(item)
