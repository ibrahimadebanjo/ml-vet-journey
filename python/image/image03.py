from PIL import Image
catImg = Image.open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\zophie.png")
print(catImg.size)
# Copying an image
catCopyImg = catImg.copy()
# pasting an image
faceIm = catImg.crop((335, 345, 565, 560))
print(faceIm.size)
catCopyImg.paste(faceIm, (0, 0))
catCopyImg.paste(faceIm, (400, 500))
catCopyImg.save('pasted.png')
             