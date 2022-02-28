import math
from PIL import Image, ImageDraw

from color import Color
    
def draw_test():
    
    w, h = 1000,1000
    
    img = Image.new('RGB',(w,h), (255,255,255))
    draw = ImageDraw.Draw(img)
    
    # draw axis    
    draw.line((0,h/2,w,h/2), (0,0,0))
    draw.line((w/2,0,w/2,h), (0,0,0))
    
    return img
