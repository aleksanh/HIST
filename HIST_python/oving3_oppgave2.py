#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 3. mar. 2015

@author: alh
'''
import string


def countLinesAndWords(fname):
    nwords = 0
    with open(fname) as fobj:
        for lines, words in enumerate(fobj):
            words = words.translate(None, string.whitespace)
            nwords += len(string.strip(words,'\n'))
    print lines + 1, nwords
    fobj.close()

countLinesAndWords(r'test.txt')

'''
    eksemplet ovenfor fungerer, men jeg er ikke forn�yd med � m� gj�re operasjonen 
    i to steg, i oppgaven oppggies det at kun bokstaver og linjer skal telles, har oversett 
    en funksjon eller en annen metode i string ?? 
    eksemplet nedenfor er min favorit, p� tross av at regexp er brysomt i seg selv. 
'''

import re
def countLinesAndWords2(fname):
    nwords = 0
    with open(fname) as fobj:
        for lines, words in enumerate(fobj):
            nwords += len(re.sub(r"\W", "", words))
    print lines + 1, nwords
    fobj.close()

countLinesAndWords2(r'test.txt')