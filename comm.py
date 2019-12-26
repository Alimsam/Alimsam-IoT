import requests, json, time
from finger import myFinger
import socket
import time
headers = {}
data = {}
resCode = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("54.180.88.152", 3000))
sock.connect(("10.120.73.120", 3300))
print('connected to Server')

while 1:
    print('waiting for ')
    data_size = 512
    data = sock.recv(data_size)
    Situation = str(data).split("'")[1]
    
    if Situation == "moving" or Situation == "outing":
        finger = myFinger()
        isFinger = finger.searchFinger()
        
        if isFinger[0] == "true":
            data = {"fingerSuccess":isFinger[0], "fingerData":isFinger[1], "fingerId":isFinger[2]}
        elif isFinger[0] == "false":
            data = {"fingerSuccess":"false"}
    
    elif Situation == "register":
        finger = myFinger()
        isSuc = finger.enrollFinger()
        if isSuc[0] == "true":
            data = {"fingerSuccess":isSuc[0], "fingerData":isSuc[1], "fingerId":isSuc[2]}
        elif isSuc[0] == "false":
            data = {"fingerSuccess":"false"}
    res = requests.get("http://10.120.73.120:3000/"+Situation+"/fingerSuccess", json=data, headers=headers)