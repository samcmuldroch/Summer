from PIL import Image
import os, sys, glob
from FileEditing import FileEditing

fileEditing = FileEditing()
god = Image.open("god.jpg")
heaven = Image.open("hevin.jpg")
desiredHeavenSize = (540, 360)
heaven.thumbnail(desiredHeavenSize, Image.ANTIALIAS)
godBox = (0, 657, 540, 960)
god.paste(heaven, godBox)
fileEditing.saveFile(god, "godAndHeaven.jpg")