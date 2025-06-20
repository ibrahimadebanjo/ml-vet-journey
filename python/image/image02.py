from PIL import Image
catImg = Image.open("C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\zophie.png")
print(catImg.size)
width, height = catImg.size
print(width)
print(height)
print(catImg.filename)
print(catImg.format)
print(catImg.format_description)
catImg.save('zophie.jpg')
# Cropping Image
croppedIm = catImg.crop((335, 345, 565, 560))
catImg.save('cropped.png')


