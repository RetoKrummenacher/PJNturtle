# -*- coding: utf-8 -*-
# turtle.py
# Copyright (C) 2022 Reto Krummenacher and contributors
#
# This module is part of PJNturtle and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPoint(self):
        return (self.x, self.y)
    
    def toString(self):
        return ','.join((str(self.x),str(self.y)))