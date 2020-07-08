from PIL import Image
im = Image.open("index.jpeg")
im.rotate(45).show()
