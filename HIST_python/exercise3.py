#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 1. feb. 2015

@author: alh

simple calculator, user should be able to enter two values 
(int or float) and the function shall sumarize them. 
'''

def simpleCalc(val1 = '', val2 = ''):
    if not all((val1, val2)):
        val1 = convertString(raw_input("First variable: "))
        val2 = convertString(raw_input("Second variable: "))
    return val1 + val2

def convertString(val):
    '''
    du to the fact that raw_input returns a string explicit
    the string must be conveted first, float or int could have
    been used direclty, how ever would have failed if the user provided
    something other then specified.
    '''
    if '.' in val:
        return float(val)
    else:
        return int(val)
