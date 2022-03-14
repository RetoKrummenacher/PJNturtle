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

t = PJNturtle()
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
t.clear()
t.home()
t.reset()
t.penColor('RED')
t.forward(200)
t.turnRight(120)
t.forward(200)
t.turnRight(120)
t.forward(200)
t.penUp()
t.turnLeft(140)
t.forward(50)
t.fill()
t.display()


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
t.penColor(Color(255,96,0))
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