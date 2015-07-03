from PIL import Image
import os, sys, glob
from FileEditing import FileEditing

#http://charlesmartinreid.com/wordpress/2012/08/python-image-averaging-and-color-averaging/
def analyze(fileName):
	im = Image.open(fileName)
	width, height = im.size
	pixels = im.load()
	pixelArray = []
	r = 0
	g = 0
	b = 0
	pixelCount = 0
	for i in range(width):
		for j in range(height):
			curPixel = pixels[i, j]
			pixelArray.append(curPixel)
			pixelCount += 1
			r += curPixel[0]
			g += curPixel[1]
			b += curPixel[2]
	rAvg = r/pixelCount
	bAvg = b/pixelCount
	gAvg = g/pixelCount
	return (rAvg, gAvg, bAvg)

fileEditing = FileEditing()
for fileName in glob.glob("*.jpg"):
	rawFileName, ext = os.path.splitext(fileName)
	r, g, b = analyze(fileName)
	imNew = Image.new("RGB", (100, 100), (r, b, g))
	fileEditing.saveFile(imNew, rawFileName + "averageColor." + ext)

