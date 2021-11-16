import re

pattern = re.compile('\d+')
number = '500-800-4623'

parts = pattern.findall(number)

print("Poszczegolne czesci numeru: {}".format(parts))