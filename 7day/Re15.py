# Re15.py
import re
m = re.match('([0-9]+) ([0-9]+)','10 295')
print(m.group(1)) # group 첫번째 반환
print(m.group(2)) # group 두번째 반환
print(m.group())  # group 모두 반환
print(m.group(0))