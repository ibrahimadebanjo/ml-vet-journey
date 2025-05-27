catNames = []
while True:
    print("Enter a cat Name " + str(len(catNames)) + " or press Enter to exit!")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("cat names are:")
for name in catNames:
    print(" " + name)
spam = [1, 2, 3, 4, 5, 6]
for num in range(len(spam)):
    print(num)
for num in spam:
    print(num)    
# same as range[1,2,3,4,5,6]
for i in [1, 2, 3, 4, 5, 6]:
    print(i)

spam = ["Ibrahim", "Owolabi", "At-taariq"]
for name in spam:
    print(name)
#or
spam = ["Ibrahim", "Owolabi", "At-taariq"] #No need to re write the variable because we are using len() function which will always return an integer
for name in range(len(spam)):
    print(name) 
supplies = ["rice", "Bens", "Yam", "maize"]
for i in range(len(supplies)):
    print("index :"+ str(i) +"Supplies :" + supplies[i])