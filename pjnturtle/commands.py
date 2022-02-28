import math
from PIL import Image, ImageDraw

from color import Color
    
def draw_test():
    
    w, h = 1000,1000
    
    img = Image.new('RGB',(w,h),Color.WHITE)
    draw = ImageDraw.Draw(img)
    
    # draw axis    
    draw.line((0,h/2,w,h/2),fill=Color.BLACK)
    draw.line((w/2,0,w/2,h),fill=Color.BLACK)
    
    return img
