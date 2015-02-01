#!/usr/bin/env python
# -*- coding: utf-8 -*-

def subObjectives_a_c():
    '''
    Simple mathematics.  
    '''
    a = 1 + 3 * 3
    b = 1 + (5 * 3)
    c = (1 + 4) * 3 
    return [a, b, c]

#=============================================================================== dident get this to work.... 
# class subObjective_d(object):
#     '''
#     calculate the area and circumference of circle with a radius of  8  ? 
#     '''
#     def __init__(self, radius = 8):
#         self.pi = 3.14159265359 # define pi as a variable, avoiding the use of ex numpy 
#         self.r = radius 
#     
#     def calcArea(self):
#         return self.pi * self.r**2
#     
#     def calcCircumference(self):
#         return 2*(self.pi*self.r)
#===============================================================================

def subObjective_d(radius = 8):
    '''
     calculate the area and circumference of circle with a radius of  8  ? 
    '''

    pi = 3.14159265359 # define pi as a variable, avoiding the use of ex numpy 
    area = pi * radius**2
    circumFerence = 2*(pi*radius)
    
    return area, circumFerence