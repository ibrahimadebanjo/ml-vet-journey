import csv
# writer objects
outputFile = open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\outputFile.csv", "w")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
