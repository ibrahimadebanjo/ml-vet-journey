# sets
set_1 = {1, True, "Owolabi", 5, 2.1}
print(set_1)
print(False in set_1)
print("Dog" in set_1)
print(1 in set_1)
# Dictionaries
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
  print(capitals[k]," is the capital of ", k)

#   Test formatting
name = "Adebanjo Ibrahim"
age = 23
print(f"{name}  is {age}")

counter = 1
while counter <= 5:
 print("Hello, world")
 counter = counter + 1


 