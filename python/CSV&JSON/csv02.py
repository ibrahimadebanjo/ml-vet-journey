import csv
exampleFile = open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\exampleWithHeader3.csv")
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + " " + str(row))