from PIL import Image
import image

file = Image.open('5.1/jelly_beans (1).jpg')
jb = file.load()

width = file.width
height = file.height

