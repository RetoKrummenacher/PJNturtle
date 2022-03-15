# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:08:13 2022

@author: retok
"""


import sys
import os
# path setting for all the scripts
sys.path.append(os.path.dirname(__file__))

from pjnturtle import *

from pjnturtle.common.point import Point


# colored hexgon
def hexa(l, a, s):
    colVec = ['PURPLE','BLUE','GREEN','YELLOW','ORANGE','RED']
    i = 0
    while True:
        if  (-2 < l < 2) and (-2 < l < 2):
            break
        t.penColor(colVec[i])
        t.forward(l)
        t.turnRight(a)
        l = l-s
        if i == 5:
            i = 0
        else:
            i = i + 1

t = Turtle()
t.backgroundColor('BLACK')
t.clear()
t.goto(512,312)
t.penDown()
t.setOrientation(120)
hexa(200, 60.8, 0.5)

t.goto(250,250)
t.setOrientation(90)
t.drawTurtle()
t.display()


# fill test
t.backgroundColor('WHITE')
t.penDown()
t.clear()
t.home()
t.reset()
t.penColor('RED')
t.forward(200)
t.turnRight(90)
t.forward(200)
t.turnRight(90)
t.forward(200)
t.turnRight(90)
t.forward(200)
t.turnRight(90)
t.forward(200)
t.turnRight(135)
t.forward(100)
t.penColor('GREY')
t.penUp()
t.forward(50)
t.fill()
t.display()

pix = t.img.load()
for i in range(1024):
    for j in range(1024):
        if pix[i,j] != (255,255,255):
            print('True')
            print(i,j)


screen_point = Point(511,509)
screen_point.getPoint()
pixels = t.img.load()
color_to_fill = pixels[screen_point.x, screen_point.y]

color_to_fill == t.pen_color.get_rgb()
    

d = {}
d[screen_point.toString()] = screen_point

while(bool(d)):
    key, position = d.popitem()
    
    if ((position.x > 0 and position.x < 1023 and
         position.y > 0 and position.y < 1023) and
        (pixels[position.x, position.y] == color_to_fill)):
        
        # set color of pixel to pen color
        pixels[position.x, position.y] = t.pen_color.get_rgb()
        
        for e in [(0,-1),(0,1),(-1,0),(1,0)]:
            i, j = e
            new_point = Point(position.x + i, position.y + j)
            # just add new points not yet in d
            if ((d.get(new_point.toString(),0) == 0) and 
                (pixels[new_point.x, new_point.y] == color_to_fill)):
                d[new_point.toString()] = new_point 

display(t.img)


# text
t.backgroundColor('WHITE')
t.clear()
t.home()
t.penColor('RED')
t.write('Test Text', 40)
t.display()


# pensize and own color
t.backgroundColor('WHITE')
t.clear()
t.home()
t.penSize(5)
t.penColor(t.color(255,96,0))
t.forward(200)
t.turnRight(68)
t.penSize(1)
t.penColor('BLUE')
t.forward(200)
t.drawTurtle()
t.display()


# easy angle
t.backgroundColor('WHITE')
t.clear()
t.home()
t.drawTurtle()
t.penDown()
t.forward(50)
t.turnRight(90)
t.drawTurtle()
t.forward(50)
t.display()


# colored multiply sign
t.clear()
t.reset()
t.home()
t.turnRight(45)
t.penDown()
t.penColor('YELLOW')
t.forward(200)
t.penUp();
t.backward(200)

t.turnRight(90)
t.penDown()
t.penColor('GREEN')
t.forward(200)
t.penUp();
t.backward(200)

t.turnRight(90)
t.penDown()
t.penColor('BLUE')
t.forward(200)
t.penUp();
t.backward(200)

t.turnRight(90)
t.penDown()
t.penColor('RED')
t.forward(200)
t.penUp();
t.backward(200)

t.display()