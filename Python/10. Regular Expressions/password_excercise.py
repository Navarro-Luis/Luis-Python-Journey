#atleast 8 char long
#contrain any sort letters, numbers !@##$%#
#has to end with a number

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'lnavarro5@fordham.edu'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'djfdsfs#$3'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)