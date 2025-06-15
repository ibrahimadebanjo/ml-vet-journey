
import PyPDF2
# roatating pages
minutesFile = open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\Recursion_Chapter1.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]

print(page.rotate(90))
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
""""
 Here we use getPage(0) to select the first page of the PDF u, and then 
we call rotateClockwise(90) on that page v. We write a new PDF with the 
rotated page and save it as  rotatedPage.pdf w.
"""