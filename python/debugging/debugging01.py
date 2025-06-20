import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open(
        "C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\debugging\\errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback Info was written to errorInfo.txt")
