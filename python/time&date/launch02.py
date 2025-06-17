import subprocess, webbrowser

# Opening website with python 

webbrowser.open("https")
#  Running Other Python Scripts
subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])
#  Opening Files with Default Applications

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['start', 'hello.txt'], shell=True)
