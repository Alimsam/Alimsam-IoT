# socket module import!
import socket

# socket create and connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("54.180.88.152", 3000))
sock.connect(("10.120.73.120", 3300))
print('connected to Server')

# send msg
#test_msg = "test"
#sock.send(test_msg.encode('utf-8'))
#print('send msg to Server')

# recv data
print('waiting for ')
data_size = 512
data = sock.recv(data_size)
print('receive data from Server')
print(data)

# connection close
sock.close()