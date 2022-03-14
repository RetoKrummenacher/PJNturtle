# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:45:47 2022

@author: retok
"""


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