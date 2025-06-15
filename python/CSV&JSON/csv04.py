import csv
# The delimiter and lineterminator Keyword arguments
csvFile = open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\outputFile2.csv", 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator="\n\n")
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csvFile.close()