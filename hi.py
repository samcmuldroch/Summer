from PIL import Image
import os, sys

print("Hi")
imageNameAsInputString = sys.stdin.readline()
im = Image.open(imageNameAsInputString)
im.show()

#http://effbot.org/imagingbook/introduction.htm
#Test for commit changes
