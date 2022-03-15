# -*- coding: utf-8 -*-
# turtle.py
# Copyright (C) 2022 Reto Krummenacher and contributors
#
# This module is part of PJNturtle and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

import math
from .point import Point

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
    