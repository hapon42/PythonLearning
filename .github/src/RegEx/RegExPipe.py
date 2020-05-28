import re
stringRegex = re.compile(r'Bat(man|mobile|corona|But)')
mo = stringRegex.search('The Batcorona  epicenter is now in Latin America')
print(mo.group())