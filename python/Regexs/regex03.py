import re
# Greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo = greedyHaRegex.search('HaHaHaHaHa')
print(mo.group())
# Non greedy Matching
nonGreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo = nonGreedyHaRegex.search("HaHaHaHaHa")
print(mo.group())
# difference between search() and findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)  # when regex has groups findall() method return lists of tuples
# Characeter Classes
xmassRegex = re.compile(r"\d+\s\w+")
mo = xmassRegex.findall(
    "'12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")
print(mo)
# Making Your OWn Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)
# Negative Character Class using Caret Character ^
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)
# the caret and dollar Sign charactersr
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.'))

#  The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567'))
print((wholeStringIsNum.search('12345xyz67890')))
print(wholeStringIsNum.search('12  34567890') )

