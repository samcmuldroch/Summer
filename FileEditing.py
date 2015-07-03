from PIL import Image
import os, sys

class FileEditing(object):

	def askingUserForFileName(self):
		print("What is the file name of your image?")
		print("(It better be saved in this currenty directory.")
		return raw_input("Write the file name here: ")


	#covert files to JPEG
	def convertFileToJPEG(self, fileName): 
	    f, e = os.path.splitext(fileName)
	    outfile = f + ".jpg"
	    if infile != outfile:
	        try:
	            Image.open(infile).save(outfile)
	        except IOError:
	            print "cannot convert", infile


	def saveFile(self, image, fileName):
		newFileName = "BETTER" + fileName
		image.save(newFileName)

	#BOXING AND ROTATING BACK IN
	def boxingAndRotating(self, fileName):
		im = Image.open(fileName)
		box = (50, 50, 300, 300) #left, upper, right, lower
		region = im.crop(box)
		region = region.transpose(Image.ROTATE_180)
		im.paste(region, box)
		saveFile(im, fileName)