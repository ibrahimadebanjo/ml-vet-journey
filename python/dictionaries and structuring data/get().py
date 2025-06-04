foodItems = {"rice": 2000, "beans": 4000, "eggs": 5000}
print("I am buying " + str(foodItems.get("rice", 0)) + " rice")
print("I am buying " + str(foodItems.get("spag", 3000)) + " spag")
# Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.