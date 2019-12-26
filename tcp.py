# socket module import!
import socket
import time
# socket create and connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("54.180.88.152", 3000))
sock.connect(("10.120.73.120", 3300))
print('connected to Server')

while 1:
    # recv data
    print('waiting for ')
    data_size = 512
    data = sock.recv(data_size)
    resData = str(data).split("'")[1]
    print(resData)
# connection close
sock.close()