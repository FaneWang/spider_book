import tesserocr
from PIL import Image

image = Image.open("untitled.png")
print(image)
result = tesserocr.image_to_text(image)
print(result)
# print(tesserocr.file_to_text('untitled.png'))