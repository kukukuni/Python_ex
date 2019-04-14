# Func09.py
CountLogin = 0

def Login(name) :
    global CountLogin
    CountLogin = CountLogin + 1
    print(name+"이 로그인")

def Logout(name):
    global CountLogin
    CountLogin = CountLogin - 1
    print(name + "이 로그아웃")

Login('Jane')
print(CountLogin)
Login('Tom')
print(CountLogin)
Login('Alice')
print(CountLogin) 
Logout('Tom')
print(CountLogin)
