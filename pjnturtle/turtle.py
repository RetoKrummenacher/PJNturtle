# -*- coding: utf-8 -*-
# turtle.py
# Copyright (C) 2022 Reto Krummenacher and contributors
#
# This module is part of PJNturtle and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php


from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
from importlib import resources

from pjnturtle.common.point import Point
from pjnturtle.common.utils import Utils
from pjnturtle.common.penstate import PenState
from pjnturtle.common.color import Color
from pjnturtle.common.colordict import ColorDict

class Turtle:    
    
    def __init__(self):
        self.__canvas_SIZE_X = 1024
        self.__canvas_SIZE_Y = 1024
        
        self.__colors = ColorDict()
                        
        self.__pen_color = self.__colors.colorDict.get('BLACK')
        # penstate enumeration, default down, thus drawing
        self.__pen_state = PenState.PEN_DOWN
        # pensize in pixel, DEFAULT = 1
        self.__pen_size = 2
        
        self.__canvas_color = self.__colors.colorDict.get('WHITE')
        
        # new CANVAS
        self.clear()
                
        # orientation of the turtle at start in degrees
        # 0 upwards, 180 downwards
        self.__orientation = 0
        
        # home point
        self.__center = Point(self.__canvas_SIZE_X//2, self.__canvas_SIZE_Y//2)
        
        # current postion, start at the center of CANVAS
        self.__curent_position = self.__center
        
    def turnRight(self, angle):
        self.__orientation += angle
        self.__orientation = Utils.normalizeOrientation(self.__orientation)        
    
    def turnLeft(self, angle):
        self.__orientation -= angle        
        self.__orientation = Utils.normalizeOrientation(self.__orientation)
    
    def forward(self, length):        
        self.__move(length)

    def backward(self, length):        
        self.__move(-length)            
            
    # private emthod
    def __move(self, length):
        goal_position = Utils.goal_position(length, 
                                         self.__orientation, 
                                         self.__curent_position)
        
        if self.__pen_state is PenState(1):
            self.__draw(goal_position)
            self.__curent_position = goal_position
        else:
            self.__curent_position = goal_position       
            
    # private method
    def __draw(self, goal_position):
        self.__canvas.line(self.__curent_position.getPoint() + goal_position.getPoint(),
                         fill = self.__pen_color.get_rgb(),
                         width = self.__pen_size)  
                
    def penUp(self):
        self.__pen_state = PenState.PEN_UP
        
    def penDown(self):
        self.__pen_state = PenState.PEN_DOWN
        
    def clear(self):
        self.__img = Image.new('RGB',(self.__canvas_SIZE_X, self.__canvas_SIZE_Y),
                        self.__canvas_color.get_rgb())
        self.__canvas = ImageDraw.Draw(self.__img)
    
    def penColor(self, color):
        # as Python does not support function overloading, we do type check
        # alternative: using multipledispatch package
        if type(color) is str:
            self.__pen_color = self.__colors.colorDict.get(color)
        else:
            self.__pen_color = color        

    def backgroundColor(self, color):
        if type(color) is str:
            self.__canvas_color = self.__colors.colorDict.get(color)
        else:
            self.__canvas_color = color      
        
    def addColor(self, name : str, color : Color):
        self.__colors.addColor(name, color)
        
    def color(self, r: int, g: int, b: int) -> Color:
        return Color(r, g, b)    
        
    def penSize(self, size):
        self.__pen_size = size
        
    def home(self):
        self.__curent_position = self.__center
        self.__orientation = 0
        
    def reset(self):
        self.__pen_size = 1
        self.__pen_color = self.__colors.colorDict.get('BLACK')
        
    def goto(self, x, y):
        self.__curent_position = Point(x,y)
        
    def setOrientation(self, angle):
        self.__orientation = angle        
        
    def display(self):
        display(self.__img)
        
    def drawTurtle(self):
        with resources.path('pjnturtle.resources', 'turtle.png') as path:
            with Image.open(path) as im:
                w, h = im.size
                # using integer devision as resize takes int
                w = w // 2
                h = h // 2            
                im = im.resize((w, h), resample = Image.BILINEAR)
                # rotation is counter clockwise, we need clockwise
                im = im.rotate(-self.__orientation,
                                resample = Image.BILINEAR,
                                expand = 1)
          
        w, h = im.size
        # use box for position calculated from current position
        # upper left and lower right pixel coordinates
        upper_left_x = self.__curent_position.getX() - w // 2
        upper_left_y = self.__curent_position.getY() - h // 2
        
        box = (upper_left_x, upper_left_y,
               upper_left_x + w, upper_left_y + h)
                            
        self.__img.paste(im, box, im)
        
    def write(self, text, fontSize):
        with resources.path('pjnturtle.resources','times-ro.ttf') as path:
            font = ImageFont.truetype(str(path), fontSize)
        self.__canvas.text(self.__curent_position.getPoint(), text,
                         self.__pen_color.get_rgb(), font = font)
                
    def fill(self):
        
        screen_point = self.__curent_position
                
        pixels = self.__img.load()
        color_to_fill = pixels[screen_point.x, screen_point.y]
        
        if (color_to_fill == self.__pen_color.get_rgb()):
            return
        
        # using python dictionary
        d = {}
        d[screen_point.toString()] = screen_point
        
        # bool(d) returns true if dictionary is not empty
        while(bool(d)):
            key, position = d.popitem()
            
            if ((position.x > 0 and position.x < self.__canvas_SIZE_X - 1 and
                 position.y > 0 and position.y < self.__canvas_SIZE_Y - 1) and
                (pixels[position.x, position.y] == color_to_fill)):
                
                # set color of pixel to pen color
                pixels[position.x, position.y] = self.__pen_color.get_rgb()
                
                for e in [(0,-1),(0,1),(-1,0),(1,0)]:
                    i, j = e
                    new_point = Point(position.x + i, position.y + j)
                    # just add new points not yet in d
                    if (d.get(new_point.toString(),0) == 0):
                        d[new_point.toString()] = new_point                            
                            
        
        
        
        
    
        
        

        
        
    
    
    
    