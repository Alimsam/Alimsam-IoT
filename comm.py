import requests, json, time
from finger import myFinger
import socket
import time
headers = {}
data = {}
resCode = ""
#ip = "192.168.219.107"
ip = "10.120.73.120"
socketPort = 3300
serverPort = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('wating for connecting to server')
sock.connect((ip, socketPort))
print('connected to Server')

while 1:
    print('waiting for request from socket server')
    data_size = 512
    data = sock.recv(data_size)
    Situation = str(data).split(',')[0]
    
    if Situation == "moving":
        place = str(data).split(',')[1]
        finger = myFinger()
        isFinger = finger.searchFinger()
        if isFinger[0] == "true":
            data = {"fingerSuccess":isFinger[0], "fingerId":isFinger[1], "place": place}
        elif isFinger[0] == "false":
            data = {"fingerSuccess":"false"}
            
    elif Situation == "outing":
        finger = myFinger()
        isFinger = finger.searchFinger()
        if isFinger[0] == "true":
            data = {"fingerSuccess":isFinger[0], "fingerId":isFinger[1]}
        elif isFinger[0] == "false":
            data = {"fingerSuccess":"false"}
            
    elif Situation == "register":
        name = str(data).split(',')[1]
        studentId = str(data).split(',')[2]
        finger = myFinger()
        isSuc = finger.enrollFinger()
        if isSuc[0] == "true":
            data = {"fingerSuccess":isSuc[0], "fingerId":isSuc[1], "name": name, "studentId": studentId}
        elif isSuc[0] == "false":
            data = {"fingerSuccess":"false"}
            
    print("Response json(str) : ",data)
    sock.send(str(data))
    # res = requests.post("http://" + ip + ":" + str(serverPort) + "/" + Situation + "/fingerSuccess", json=data, headers=headers)
    print("Finish")
