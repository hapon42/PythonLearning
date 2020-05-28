
import re
phoneRegEx = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
result = phoneRegEx.search('This is my phone number: 09188081384')
print(result.group())
print(phoneRegEx.findall('This are my phone numbers: 09188081384 and 09188081385'))