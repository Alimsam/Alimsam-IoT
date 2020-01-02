import requests, json, time
from finger import myFinger
import socket
import time
headers = {}
data = {}
resCode = ""
#ip = "54.180.88.152"
ip = "10.120.73.120"
socketPort = 3300

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print('wating for connecting to server')
#sock.connect((ip, socketPort))
#print('connected to Server')

while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('waiting for connectiong to Server')
    sock.connect((ip, socketPort))
    print('connected Server')
    print('waiting for request from socket server')
    data_size = 512
    recvData = sock.recv(data_size)
    Situation = str(recvData).split(',')[0]
    print(recvData)
    if Situation == "moving":
        finger = myFinger()
        isFinger = finger.searchFinger()
        if isFinger[0] == "true":
            data = "fingerSuccess:"+isFinger[0] + ",fingerId:"+isFinger[1]
        elif isFinger[0] == "false":
            data = "fingerSuccess:false"
            
    elif Situation == "outing":
        finger = myFinger()
        isFinger = finger.searchFinger()
        if isFinger[0] == "true":
            data = "fingerSuccess:"+isFinger[0] + ",fingerId:"+isFinger[1]
        elif isFinger[0] == "false":
            data = "fingerSuccess:false"
            
    elif Situation == "register":
        finger = myFinger()
        isSuc = finger.enrollFinger()
        if isSuc[0] == "true":
            data = "fingerSuccess:"+isSuc[0] + ",fingerId:"+isSuc[1]
        elif isSuc[0] == "false":
            data = "fingerSuccess:false"
        elif isSuc[0] == "already":
            data = "fingerSuccess:"+isSuc[0]
            
    print(data)
    sock.send(str(data))
    print("Finish")
    sock.close()
