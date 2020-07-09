from PIL import Image
im = Image.open("/home/jambompeople/Downloads/index.jpeg").convert("LA")
imgsmall = im.resize((16,16),resample = Image.BILINEAR)
pixels = imgsmall.load()
pixels[0,0] = (255, 0, 0)
result = imgsmall.resize(im.size, Image.NEAREST)
result.show()
