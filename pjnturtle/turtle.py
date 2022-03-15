# -*- coding: utf-8 -*-
"""
PJNturtle Class
A Simple Turtle with Python for Jupyter Notebook

Available commands
    penDown()
    penUp()
    forward(length)
    backward(length)
    turnRight(degrees)
    turnLeft(defrees)
    display()
    clear()
"""



# Temporary for Spyder to work, not needed in Jupyter
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
import collections
from importlib import resources


from pjnturtle.common.point import Point
from pjnturtle.common.utils import Utils
from pjnturtle.common.penstate import PenState
from pjnturtle.common.color import Color
from pjnturtle.common.colordict import ColorDict

class Turtle:    
    
    def __init__(self):
        self.CANVAS_SIZE_X = 1024
        self.CANVAS_SIZE_Y = 1024
        
        self.colors = ColorDict()
                        
        self.pen_color = self.colors.colorDict.get('BLACK')
        # penstate enumeration, default down, thus drawing
        self.pen_state = PenState.PEN_DOWN
        # pensize in pixel, DEFAULT = 1
        self.pen_size = 2
        
        self.canvas_color = self.colors.colorDict.get('WHITE')
        
        # new CANVAS
        self.clear()
                
        # orientation of the turtle at start in degrees
        # 0 upwards, 180 downwards
        self.orientation = 0
        
        # home point
        self.center = Point(self.CANVAS_SIZE_X//2, self.CANVAS_SIZE_Y//2)
        
        # current postion, start at the center of CANVAS
        self.current_position = self.center
        
    def turnRight(self, angle):
        self.orientation += angle
        self.orientation = Utils.normalizeOrientation(self.orientation)        
    
    def turnLeft(self, angle):
        self.orientation -= angle        
        self.orientation = Utils.normalizeOrientation(self.orientation)
    
    def forward(self, length):        
        self.move(length)

    def backward(self, length):        
        self.move(-length)            
            
    def move(self, length):
        goal_position = Utils.goal_position(length, 
                                         self.orientation, 
                                         self.current_position)
        
        if self.pen_state is PenState(1):
            self.draw(goal_position)
            self.current_position = goal_position
        else:
            self.current_position = goal_position       
                
    def draw(self, goal_position):
        self.canvas.line(self.current_position.getPoint() + goal_position.getPoint(),
                         fill = self.pen_color.get_rgb(),
                         width = self.pen_size)  
        
    def penUp(self):
        self.pen_state = PenState.PEN_UP
        
    def penDown(self):
        self.pen_state = PenState.PEN_DOWN
        
    def clear(self):
        self.img = Image.new('RGB',(self.CANVAS_SIZE_X, self.CANVAS_SIZE_Y),
                        self.canvas_color.get_rgb())
        self.canvas = ImageDraw.Draw(self.img)
    
    def penColor(self, color):
        # as Python does not support function overloading, we do type check
        # alternative: using multipledispatch package
        if type(color) is str:
            self.pen_color = self.colors.colorDict.get(color)
        else:
            self.pen_color = color        

    def backgroundColor(self, color):
        if type(color) is str:
            self.canvas_color = self.colors.colorDict.get(color)
        else:
            self.canvas_color = color      
        
    def addColor(self, name : str, color : Color):
        self.colors = self.colors.addColor(name, color)
        
    def penSize(self, size):
        self.pen_size = size
        
    def home(self):
        self.current_position = self.center
        self.orientation = 0
        
    def reset(self):
        self.pen_size = 1
        self.pen_color = self.colors.colorDict.get('BLACK')
        
    def goto(self, x, y):
        self.current_position = Point(x,y)
        
    def setOrientation(self, angle):
        self.orientation = angle        
        
    def display(self):
        display(self.img)
        
    def drawTurtle(self):
        # resPath = os.path.join('resources','turtle.png')
        with resources.path('pjnturtle.resources', 'turtle.png') as path:
            with Image.open(path) as im:
                w, h = im.size
                # using integer devision as resize takes int
                w = w // 2
                h = h // 2            
                im = im.resize((w, h), resample = Image.BILINEAR)
                # rotation is counter clockwise, we need clockwise
                im = im.rotate(-self.orientation,
                                resample = Image.BILINEAR,
                                expand = 1)
          
        w, h = im.size
        # use box for position calculated from current position
        # upper left and lower right pixel coordinates
        upper_left_x = self.current_position.getX() - w // 2
        upper_left_y = self.current_position.getY() - h // 2
        
        box = (upper_left_x, upper_left_y,
               upper_left_x + w, upper_left_y + h)
                            
        self.img.paste(im, box, im)
        
    def write(self, text, fontSize):
        with resources.path('pjnturtle.resources','times-ro.ttf') as path:
            font = ImageFont.truetype(str(path), fontSize)
        self.canvas.text(self.current_position.getPoint(), text,
                         self.pen_color.get_rgb(), font = font)
        
    def fill(self):
        
        screen_point = self.current_position
        
        rgb_im = self.img.convert('RGB')
        r, g, b = rgb_im.getpixel(screen_point.getPoint())        
        color_to_fill = (r, g ,b)
        
        if (color_to_fill == self.pen_color.get_rgb()):
            return
        
        # using pythons deque() from collections
        q = collections.deque()
        q.append(screen_point)
        
        while(bool(q)):
            position = q.popleft()
            
            r, g, b = rgb_im.getpixel(position.getPoint())        
            this_color = (r, g ,b)
            
            if ((position.x >= 0 and position.x < self.CANVAS_SIZE_X and
                position.y >= 0 and position.y < self.CANVAS_SIZE_Y) and
                (this_color == color_to_fill)):
                
                self.img.putpixel(position.getPoint(), color_to_fill)
                
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i != 0 or j != 0) :
                            q.append(Point(position.x + i, position.y + j))
                            
                            
        
        
        
        
    
        
        

        
        
    
    
    
    