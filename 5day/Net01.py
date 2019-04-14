# Net01.py
# Server
# command A 창에서 실행 
from socket import *
svrIP = '192.168.56.1' # Host IP
svrPort = 64000
svrAddr = (svrIP,svrPort)
svrSocket = socket(AF_INET,SOCK_STREAM) #TCP통신을 하겠다.
svrSocket.bind(svrAddr)
svrSocket.listen(0)                     #포트를 열어두겠다.
# Listening 상태 완료

# Connect  허락 
cliSocket, cliAddr = svrSocket.accept()

# 메세지 전송(send)
cliSocket.send(b"Welcome Py Server")

# 메세지 수신(recv)
data = cliSocket.recv(1024)
print(data.decode('utf-8'))
