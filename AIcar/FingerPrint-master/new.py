import FingerPrint
myFP = FingerPrint()
try:
    myFP.open()
    print("Please touch the fingerprint sensor")
    if myFP.verify():
        print("Hello! Master")
    else:
        print("Sorry! Man")
finally:
    myFP.close()
