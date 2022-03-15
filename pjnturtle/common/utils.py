# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:10:49 2022

@author: retok
"""

import math
from point import Point

class Utils:
    
    def degreeToRad(degree):
        return degree / 360.0 * math.pi * 2.0
    
    def normalizeOrientation(angle):
        # For the orientation to be between 0 and 359 degrees
        # works with negative numbers as well -45 % 360 = 315
        return angle % 360            
        
    def goal_position(length, orientation, current):
                
        degreeInRad = Utils.degreeToRad(orientation-90)
        
        goal_x = int(round(math.cos(degreeInRad) * length + current.getX(),0))
        goal_y = int(round(math.sin(degreeInRad) * length + current.getY(),0))
        
        return Point(goal_x, goal_y)
    