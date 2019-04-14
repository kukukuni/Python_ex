#keyword comp
A = [['삼성',0],['LG',0],['kT',0],['하이닉스',1],['SKT',0],['IBM',9]]
HeadLineCount = 10
B = []
Result = []
def dododo():
    B.clear()
    for k in range(0,HeadLineCount):
        B.append([])

    for i in range(0,len(A)):
        for j in range(0,HeadLineCount):
            if (A[i][1] == j):
                B[j].append(A[i][0])

    print(B)
    Result.clear()
    for h in range(0,len(B)):
        Tempstr = ','.join(B[h])
        if(Tempstr!=''):
            print(Tempstr)


dododo()