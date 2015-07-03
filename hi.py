#citation: http://effbot.org/imagingbook/introduction.htm

from PIL import Image
import os, sys

def askingUserForFileName():
	print("What is the file name of your image?")
	print("(It better be saved in this currenty directory.")
	return raw_input("Write the file name here: ")


#covert files to JPEG
def convertFileToJPEG(fileName): 
    f, e = os.path.splitext(fileName)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile


def saveFile(image, fileName):
	newFileName = "BETTER" + fileName
	image.save(newFileName)

#BOXING AND ROTATING BACK IN
def boxingAndRotating(fileName):
	im = Image.open(fileName)
	box = (50, 50, 300, 300) #left, upper, right, lower
	region = im.crop(box)
	region = region.transpose(Image.ROTATE_180)
	im.paste(region, box)
	saveFile(im, fileName)



running = True
while running:
	print("What would you like to do?")
	print("(d for making your image dope, j for saving as jpeg, h for help, q for quit)")
	answer = raw_input("Type your letter here: ")
	if (answer == "d"):
		fileName = askingUserForFileName()
		boxingAndRotating(fileName)
		print("Checkout your image 2.0 ;)")
		running = False
	elif (answer == "h"):
		print("Call 911.")
		running = False
	elif (answer == "q"):
		print("Ugh. Bye.")
		running = False
	elif (answer == "j"):
		fileName = askingUserForFileName()
		print("Too easy. Done")
	else:
		print("That wasn't one of the options moron. Try again.")