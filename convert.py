import sys
from PIL import Image, ImageOps

MAX_SIZE = 200 
CHARS = [ ".",",","*","^","#","$","%","&" ]
STEP = 255 / len(CHARS) 

[ filename, image_file_path, ascii_out_file_path ] = sys.argv

raw_img = Image.open( image_file_path )
width, height = raw_img.size

scale_f = MAX_SIZE/ max( width, height )

width  = int(width  * scale_f)
height = int(height * scale_f * .5)

raw_img = raw_img.resize( ( width, height ) )
gs_img = ImageOps.grayscale( raw_img )

px = gs_img.load()

txt = ""



for y in range(height):
    for x in range(width):
        index = px[ x, y ] // STEP
        txt += CHARS[int(index)]
    txt += "\n"

print( txt )

