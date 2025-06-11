import re
phoneNumberRegEx = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# Matching Regex object
# searc() and match() method
mo = phoneNumberRegEx.search("My number is 949-485-4747")
print("Phone Number Found:" + mo.group())
# Grouping with parenthesis
phoneNumberRegEx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumberRegEx.search("My Number is 234-477-7374")
print("Phone Number Found :" + mo.group(0))
print("Phone Number Found :" + mo.group(1))
print("Phone Number Found :" + mo.group(2))
print("Phone Number Found :" + mo.group())
phoneNumberRegEx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegEx.search('My phone number is (415) 555-4242.')
print(mo.group())
