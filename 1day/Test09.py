# Test09.py

# bool -> True, False

# and, or, not, if, for, while

print(True and False)
print(True & False)
print(True or False)
print(True | False)

print(6 and 3)  #3 둘다 값이 있는 트루라서 뒤에값 저장
print(6 & 3)    #2 비트연산 0110 & 0011이라 0010
print(6 or 3)   #6 첫번째거가 트루라 뒤에거 안보고 바로 6 출려ㄱ
print(6 | 3)    #7

print(3 and 6)  #6
print(3 or 6)   #3

print(0 and 6)  #
print(0 or 6)   #

# bool(data) --> false
# False : 0, '', [], {}, (), None, False 7가지

print(bool(0),bool(''),bool([]),bool({}))   #다들 비어있다는 뜻
print(bool(()),bool(None),bool(False))      #bool(0)는 비트가 비어있다는 뜻

# if not [] ;

print(True, not True)
print(not 1, not -1)  #-1도 비트로 보면 앞에 부호가 들어가니까 트루

print(int(not not -1))
