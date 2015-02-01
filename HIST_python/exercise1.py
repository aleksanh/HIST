#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31. jan. 2015

@author: ahammernes
'''
import getpass

def subEx_a():
    print("Hello world")
    
def subEx_b():
    myName = "Aleksander"
    print("Hello, my name is " + myName)
    print "and your user names is: " + getpass.getuser()
    
def subEx_c(inStr):
    if inStr == "c":
        inStr = raw_input('Name to display: ')
    print "inputed string: " + inStr 
    
    
if __name__ == "__main__":  #ensures bellow is only executed if this file is run directly
    exLetter = raw_input('sub exercise to run: ')
    if exLetter == "a":
        subEx_a()
    elif exLetter == "b":
        subEx_b()
    elif exLetter[0] == "c":
        if len(exLetter) >1:
            exLetter = exLetter.split()
            exLetter = exLetter[1]
        subEx_c(exLetter)
