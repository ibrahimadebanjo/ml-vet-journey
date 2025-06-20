
from PIL import Image
catImg = Image.open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\zophie.png")
print(catImg.size)
faceIm = catImg.crop((335, 345, 565, 560))
catImWidth, catImHeight = catImg.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catImg.copy()
for left in range(0, catImWidth, faceImWidth):
         for top in range(0, catImHeight, faceImHeight):
             print(left, top)
             catCopyTwo.paste(faceIm, (left, top))


catCopyTwo.save('tiled.png')