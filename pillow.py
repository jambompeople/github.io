from PIL import Image
im = Image.open("/home/jambompeople/Downloads/index.jpeg")
im2 = im.resize((18,18), resample = Image.BILINEAR)
pixel = im2.load()
for i in range(0,18):
    for j in range(0, 6):
        pixel[i, j] = (0, 0, 0)

for i in range(0,18):
    for j in range(6, 12):
        pixel[i, j] = (255, 0, 0)

for i in range(0,18):
    for j in range(12, 18):
        pixel[i, j] = (255, 255, 0)

im3 = im2.resize(im.size, Image.NEAREST)
im3.show()
