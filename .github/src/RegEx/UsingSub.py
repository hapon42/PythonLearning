import re
agentRegEx = re.compile(r'Agent \w+')
print(agentRegEx.findall('Agent Norman passed the Repl Python project to Agent Brown'))
print(agentRegEx.sub('REDACTED','Agent Norman passed the Repl Python project to Agent Brown'))
