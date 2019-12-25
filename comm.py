import requests, json, time
from finger import myFinger
headers = {}
data = {}
resCode = ""
# def resData():
#     if resCode == "moving" or "outing":
#         return 1
#     elif resCode == "register":
#         return 0
#     else :
#         return "No"

while 1:
    print("start")
    res = requests.get("http://10.120.73.120:3000/finger/fingerStart?method=outing", json=data, headers=headers)
    print("json:",res.json()['fingerStart'])
    if str(res.json()['fingerStart']) == "moving" or str(res.json()['fingerStart']) == "outing":
        finger = myFinger()
        finger.searchFinger()
        Finger = finger.getisFinger()
        FingerData = finger.getfinData()
        FingerId = finger.getfinId()
        if finger == "true":
            data = {"fingerSuccess":Finger, "fingerData":FingerData, "fingerId":FingerId}
            
        elif finger == "false":
            data = {"fingerSuccess":Finger}
            
        elif finger == "add":
            data = {"fingerSuccess":Finger, "fingerData":FingerData, "fingerId":FingerId}
    elif str(res.json()['fingerStart']) == "register":
        finger = myFinger
        finger.enrollFinger()
    time.sleep(1)
# HTTP CODE 
#print(res.status_code) 
# # HTTP 응답 원문 
# print(res.text) 
# HTTP 요청 값 
# print(res.request, res.request.body, res.content) 
# HTTP 응답 원문(JSON)을 디코딩하여 Dictionary로 반환 
#     if res.json()['fingerStart'] == "moving":
#     
#     elif res.json()['fingerStart'] == "outing":