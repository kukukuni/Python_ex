# for08.py

nd1 = [[10,20,30],
       [40,50,60],
       [70,80,90]]

##10 20 30 
##40 50 60 
##70 80 90

for i in range(len(nd1)):
    for j in range(len(nd1[i])):
        print(nd1[i][j],end=' ')
    print()


###############################
nd2 = [[10,20,30,40],
       [40,50],
       [70,80,90]]

##10 20 30 40 
##40 50 
##70 80 90

for i in range(len(nd2)):
    for j in range(len(nd2[i])):
        print(nd2[i][j],end=' ')
    print()




