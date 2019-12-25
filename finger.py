import time
f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
class myFinger:
    def __init__(self):
        try:
            print("yes")
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')
            print ("complete")
        except Exception as e:
            print('Exception message: ' + str(e))
            exit(1)

    
    def getisFinger():
        return isFinger
    def getfinData():
        return FinData
    def getfinId():
        return FinId

    def enrollFinger():
        time.sleep(2)
        print('Waiting for finger...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x02)
        if ( f.compareCharacteristics() == 0 ):
            print ("Fingers do not match")
            time.sleep(2)
            #
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))
        return ["true",str(f.downloadCharacteristics(0x01)).encode('utf-8'), str(positionNumber)]
    def searchFinger():
        try:
            print('Waiting for finger...')
            while( f.readImage() == False ):
                #pass
                time.sleep(.5)
                return
            f.convertImage(0x01)
            result = f.searchTemplate()
            positionNumber = result[0]
            accuracyScore = result[1]
            if positionNumber == -1 :
                print('No match found!')
                return "false"
            else:
                print('Found template at position #' + str(positionNumber))
                isFinger="true"
#                 FinId = str(positionNumber)
#                 FinData = str(f.downloadCharacteristics(0x01)).encode('utf-8')
                print(str(positionNumber))
                return ["true",str(f.downloadCharacteristics(0x01)).encode('utf-8'), str(positionNumber)]
        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)
            
    def clear():
        isFinger = ""
        FinData = ""
        FinId = ""
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
        

