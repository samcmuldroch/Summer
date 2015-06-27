import Image
#import Stdin(?)

print("Hi")
imageNameAsInputString = sys.stdin.readline()
im = Image.open(imageNameAsInputString)
im.show()

#http://effbot.org/imagingbook/introduction.htm
