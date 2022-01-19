from PIL import Image,ImageFilter

image = Image.open('./1.jpg')
print(image.format,image.size, image.mode)
# image.show()
image.filter(ImageFilter.CONTOUR).show()