'''
Created on 12. feb. 2015

@author: alh
'''


import math 

def a():
    valA = math.sqrt(math.pi)
    # sqrt can also be done as:
    #valAA = math.pi**0.5  
    return valA

def b(val):
    '''
        take the give val and return it as a string with only 3 decimals. 
    '''
    return '%.3f' % val

def c(val):
    '''
        take the give val and return it as a string with max 6 value, this is on the notion 
        on that the val is x.xxxxxxx  
    '''
    return '%1.5f' % val


class d(object):
    '''
    '''
    def __init__(self):
        self.createStringMatrix()
        
    def myRanger(self,initialVal, stop, step):
        while initialVal <= stop+step:
            yield initialVal
            initialVal += step 
            
    def createStringMatrix(self):
        print 'x sin(x)  cos(y)'
        iterator = self.myRanger(-1, 1, 0.05)
        #lst = [math.sin(i), math.cos(i) i for i in iterator]  #way wont this work ?? 
        for x in iterator:
            print '%.2f  %.4f  %.4f' % (x, math.sin(x), math.cos(x))
        

if __name__ == '__main__':
    print 'The square root of pi: ' + str(a())
    print 'The square root of pi with 3 decimals: ' + b(a())
    print 'The square root of pi with max 6 values: ' + c(a())
    print 'Oppgave D: '
    d()