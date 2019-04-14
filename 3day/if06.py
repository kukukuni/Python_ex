# if06.py
# 점수(국어,영어)를 입력받아서
# 총점, 평균을 출력하세요
print("국어 점수 입력")
iKor = int(input())
print("영어 점수 입력")
iEng = int(input())

iTotal = iKor + iEng
iAvg = iTotal/2
print('총점 : {0}, 평균 : {1}'.format(iTotal,iAvg))

# 평균낙제,과목낙제 
if (iKor<60) | (iEng<60): print('과목낙제')
elif (iAvg>=90): print('우수')
elif (iAvg>=80): print('보통')
elif (iAvg>=70): print('부족')
else : print('평균낙제')

print('성적 발표 완료')
