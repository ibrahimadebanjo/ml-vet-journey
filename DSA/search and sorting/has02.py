s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
s.remove(3)
string = "hwhhhwwwwwwwwwrkwljlqklrhkkklqklq"
sett = set(string)
print(sett)
for i in sett:
    print(i)

# HashMaps - Dictionaries
d = {
    "green": 1,
    "blue": 2,
    "white": 3
}

print(d)
d["blue"] = 4
print(d)

for key, value in d.items():
    print((f"key {key} : value {value}"))
