import re

pattern = re.compile('this')
string = 'search this inside this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)#checks if exact matches, which they arent.
d = pattern.match(string)
print(a.group())