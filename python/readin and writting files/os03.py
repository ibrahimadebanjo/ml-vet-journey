import pprint
#  Saving Variables with the pprint.pformat() function
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\readin and writting files\\myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()