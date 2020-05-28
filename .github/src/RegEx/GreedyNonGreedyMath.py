import re
phoneRegEx = re.compile(r'([+63]|\0)?\d\d\d\d\d\d\d\d\d\d')
mo = phoneRegEx.search('Find my number in this string. Show my Number +639188081384 when you found it.')
print(mo.group())
