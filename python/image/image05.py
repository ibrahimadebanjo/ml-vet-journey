from PIL import Image
catImg = Image.open(
    "C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\Automate_the_Boring_Stuff_3e_onlinematerials\\Automate_the_Boring_Stuff_3e_onlinematerials\\zophie.png")
print(catImg.size)
# Resizing an image
width, height = catImg.size

quartersizedIm = catImg.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catImg.resize((width, height + 300))
svelteIm.save('svelte.png')
# Rotating and flipping images
catImg.rotate(90).save('rotated90.png')
catImg.rotate(180).save('rotated180.png')
catImg.rotate(270).save('rotated270.png')
# rotate method has an optional expand method
catImg.rotate(6).save('rotated6.png')
catImg.rotate(6, expand=True).save('rotated6_expanded.png')

# Mirror flipping images through transpose() method
catImg.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catImg.transpose(Image.FLIP_TOP_BOTTOM).save("vertical_flip.png")
