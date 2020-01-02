import time
from pyfingerprint.pyfingerprint import PyFingerprint

f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

tmp=""
class myFinger:
    def __init__(self):
        try:
            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')
            print ("complete")
        except Exception as e:
            print('Exception message: ' + str(e))
            exit(1)

    def enrollFinger(a):
        time.sleep(2)
        print('Waiting for finger...')
        while f.readImage() == False :
            pass
        print("processing...")
        f.convertImage(0x01)
        result = f.searchTemplate()
        #tmp = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        positionNumber = result[0]
        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            time.sleep(2)
            return ['already']
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x02)
        if ( f.compareCharacteristics() == 0 ):
            print ("Fingers do not match")
            time.sleep(2)
            return ['false']
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))
        return ["true", str(positionNumber)]
    
    def searchFinger(a):
        try:
            print('Waiting for finger...')
            while( f.readImage() == False ):
                #pass
                time.sleep(.5)
                pass
            f.convertImage(0x01)
            result = f.searchTemplate()
            positionNumber = result[0]
            accuracyScore = result[1]
            if positionNumber == -1 :
                print('No match found!')
                return ["false"]
            else:
                print('Found template at position #' + str(positionNumber))
                print(str(positionNumber))
                return ["true", str(positionNumber)]
        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)
            return ["false"]
# 
#     while 1:
#         #s = int(input())
#         #if s == 0:
#         if comm.resData() == "No":
#             isFinger = ""
#             FinData = ""
#             FinId = ""
# 
#             finput = comm.resData() 
#             if finput == 0:
#                 enrollFinger()
# 
#             elif finput == 1:
#                 searchFinger()
        

