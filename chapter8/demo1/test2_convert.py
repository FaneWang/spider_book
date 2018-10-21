import tesserocr
from PIL import Image

image = Image.open("2.png")
# # result = tesserocr.image_to_text(image)
# # print(result)
image = image.convert('L')
# image = image.convert('1')
threshold = 130
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)
