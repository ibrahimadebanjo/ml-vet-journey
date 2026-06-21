import numpy as np
#loading txt file
txt= np.loadtxt("/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/text.txt")
print(txt)
#loading csv files 
csv= np.genfromtxt("/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/text.csv", delimiter = ',')
print(csv)
arr = np.array([2,4,7])
np.savetxt('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/text.csv', arr , delimiter = ",")

print(csv)