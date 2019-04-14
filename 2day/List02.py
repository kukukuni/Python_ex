# List02.py

a = [10,20,30]
print(len(a),a)

a.append(40)
print(len(a),a)

a.append(20)
print(len(a),a,a.count(20))

a.insert(1,50)
print(len(a),a)

a.pop()
print(len(a),a)

a.pop(1)
print(len(a),a)

a.remove(20)
print(len(a),a)

a += [20]
print(len(a),a)

a.extend([50,60])
print(len(a),a)

a += [70, 80]
print(len(a),a)

print(a.index(20))
a.pop(-3)
print(len(a),a)










