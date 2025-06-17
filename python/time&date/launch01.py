import subprocess
calcProcess = subprocess.Popen("C:\\Windows\\System32\\calc.exe")
print(calcProcess.poll() == None)
print(calcProcess.poll())
print(calcProcess.wait())
print(calcProcess.poll())

# Passsing command line argument
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
