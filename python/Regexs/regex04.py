import re
# The Wildcard Character .
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search("First Name: Ibrahim Last Name: Adebanjo")
print(mo.group(1))
print(mo.group(2))
# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo.group())
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo.group())
# Case insensitive Matching using re.I or re.IGNORECASE as second arguments to re.compile()
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
print(mo.group())
mo = robocop.search('ROBOCOP protects the innocent.')
print(mo.group())