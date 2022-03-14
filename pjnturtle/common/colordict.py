# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:03:44 2022

@author: retok
"""

from .color import Color

class ColorDict:
    
    def __init__(self):
        self.fillColorDict()       
        
        
    def fillColorDict(self):
        colDict = {}
        colDict['BLACK'] = Color(0,0,0)
        colDict['BLUE'] = Color(0,0,255) 
        colDict['GREEN'] = Color(0,204,0)
        colDict['GREY'] = Color(153,153,153)
        colDict['ORANGE'] = Color(255,102,0)
        colDict['PURPLE'] = Color(128,0,128)
        colDict['RED'] = Color(255,0,0)
        colDict['WHITE'] = Color(255,255,255)
        colDict['YELLOW'] = Color(255,255,0)
            
        self.colorDict = colDict
    
    def addColor(self, name : str, color : Color ):
        self.colorDict[name] = color
        return self.colorDict
        