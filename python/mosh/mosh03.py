numbers = [1, 2, 3, 6, 7, 9]
numbers2 = numbers.copy()
# numbers2 = numbers.remove()
print(numbers2)
# unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# instead do unpacking
x, y, z = coordinates

phone = input("phone :")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = "" 
for i in phone:
    output += digits_mapping.get(i, "!") + " "
print(output)
