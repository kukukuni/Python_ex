# for12_Quiz.py

# Quiz 1) a 에서 abc 가 아닌 문자는 무엇인가요? (중복제거)

a = 'aybxczbcyazcaxbc'
   
b = { s for s in a if s not in 'abc' }

print(b)

# [ 입력변수 if 조건 for 추출변수 in 대상 if 조건 ]

# Quiz 2) 학생들의 국어점수가 70 이상이면 '합격', 아니면 '불합격'
국어점수 = {'Tom':90,'Jane':60,'Alice':70}
print(국어점수)

#  a if 조건 else b
r = { 학생이름:'합격' if 국어점수[학생이름] >=70 else '불합격'
                  for 학생이름 in 국어점수.keys()}

print(r)

# 결과 ==> {'Tom': '합격', 'Jane': '불합격', 'Alice': '합격'}

# Quiz 3 ) 수학 점수가 0이 아닌 학생들만 출력하세요
#          단, 70이상은 합격, 미만은 불합격 표시

수학점수 = {'Tom':90,'Jane':60,'Alice':0,'Hong':78,'Kim':45}

z = { 학생이름:'합격' if 수학점수[학생이름] >=70 else '불합격'
      for 학생이름 in 수학점수.keys() if 수학점수[학생이름] != 0  }
#처음부터 제외할 데이터에 대해서는 for뒤에 if를 쓰고,
#가져온 데이터의 if처리를 할때는 for문의 앞에서 한다.

# 3줄 요약
# 맨뒤의 if는 for에 들어가는 in의 것들을 일차적으로 걸러서 넣게해준다.
# 거른 후에 if의 기준을 가지고 참이면 앞의것 거짓이면 else로 되게 한다.
# 그래서 ('합격' if 수학점수[학생이름] >=70 else '불합격')이런 식으로 해도 됨
print(z)

# 결과 ==> {'Tom':'합격','Jane':'불합격,'Hong':'합격','Kim':'불합격}

