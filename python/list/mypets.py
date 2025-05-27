pets = ["betty", "pooka", "fat-tail", "Zophie"]
print("Pls Enter pet name:")
name = input()
if name not in pets:
    print("I don't have pet names : " + name)
else:
    print("I have the pet named :" + name)

#Multiple assignment trick    
cat = ["big","white","loud","persian"]
size,color,disposition,breed = cat
print(size)
print(color)
print(disposition)
print(breed)
#Instead of size = cat[0]....


