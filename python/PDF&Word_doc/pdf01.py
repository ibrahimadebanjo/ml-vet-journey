import PyPDF2
pdfFileObj = open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\Recursion_Chapter1.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]
# for Extracting the text in the pages
print(pageObj.extract_text())
# Decrypting PDFs
pdfReader = PyPDF2.PdfReader(open(
    "C:\\Users\\IBRAHIM\Documents\\ml-vet-journey\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\ALX Professional Foundations Completion Requirements & Policies-protected (1).pdf", 'rb'))
print(pdfReader.is_encrypted)
# print(pdfReader.pages[0])
pdfReader.decrypt('$owolabi2443')
print(pdfReader.pages[0])
