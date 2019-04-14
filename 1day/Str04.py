# Str04.py

a = '  Hello'
b = 'Hello  '
c = ' Hello '
#빈칸 제거는 strip
print(a.lstrip())
print(b.rstrip())
print(c.strip())

d = 'Hello안녕12'

print(d.isalpha())
print(d.isalnum())

e = 'Hello 안녕 12'

print(e.isalpha())
print(e.isalnum())

f = 'Pithon'
print(f.replace('i','y'))

x = 'Java.C.SQL.Python'
y = x.replace('.',' ')

x = 'Java.C.SQL.Python'
y = x.split('.')
print(y)

z = '.'.join(y)
print(z)

k = 'Java   C  SQL    Python'

#m = k.replace('  ',' ')
#m = m.replace('  ',' ')
#m = m.replace(' ','.')
m = '.'.join(k.split())
print(m)








