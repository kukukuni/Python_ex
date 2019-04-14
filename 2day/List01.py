# List01.py

#ArrayList --> List(Python, R, Scratch)
#Array는 크기를 변환할 수 없지만, ArrayList는 변환이 가능
#Java에서는 ArrayList를 쓰는 반면에
#데이터를 많이쓰는 Python, R, Scratch는 List가 가능

a = ['사과', '배', '바나나']
print(a,type(a))

a += ['포도']
print(a,type(a))

a = a + ['딸기']
print(a,type(a))

a += [10]
print(a,type(a[5]))

b = [10, 'A', "안녕", True, 3.14, [10,20,30]]
#이 값들은 다 주소다. 링크따라서 오는 것이기 때문에
#타입이 달라도 같이 쓸 수 있다.
print(b[0],id(b[0]),b[5][0],id(b[5][0])) 

c = ['강', 10, 3.14, True, None, a]
print(len(c))
#None도 칸으로 센다.











