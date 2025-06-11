import os
print(os.path.join('usr', 'bin', 'spam'))
# If I had called this function on OS X or Linux, the string would have been 'usr/bin/spam'.
myFiles = ['os.py']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
print(os.getcwd())  # For getting current working directory
os.chdir('C:\\Windows\\System32')
print(os.getcwd())  # used for Changing directory
# os.chdir('C:\\ThisFolderDoesNotExist') #Error
# Creatin new folders with os.makedirs()
# os.makedirs('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\hi') # it only make directory once else it will throw an error
# Handling Absolute and Relative Paths
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.getcwd())
# Basename
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)
#  Finding File Sizes and Folder Contents using os.path.getsize(path) and os.listdir(path)
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.listdir('C:\\Windows\\System32'))
# Checking Path Validity using os.path.exists(path), os.path.isfile(path) and os.path.isdir(path)
print( os.path.exists('C:\\Windows'))
print( os.path.exists('C:\\some_made_up_folder'))
print( os.path.isdir('C:\\Windows\\System32'))
print( os.path.isfile('C:\\Windows\\System32'))
print( os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print( os.path.isfile('C:\\Windows\\System32\\calc.exe'))
# You can check whether there is a DVD or flash Drive atached currently to the system by using os.path.exists('D:\\')
print(os.path.exists('D:\\'))
# the file reading/writing Process
#  1.  Opening Files with the open() Function
helloFile = open('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\readin and writting files\\readorwrite.txt')
print(helloFile)
# 2. Reading the Contents of Files
helloContent = helloFile.read()
print(helloContent)
# Writing to files
baconFile = open('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\readin and writting files\\readorwrite.txt', 'w')   
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\readin and writting files\\readorwrite.txt', 'a') 
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\readin and writting files\\readorwrite.txt')
content = baconFile.read()
baconFile.close()
print(content)

