'''
Created on 2. mar. 2015

@author: alh
'''


def celsiusFar(cel):
    return cel*(9/5) + 32  #returns celius degrees as farenheit.

def userInput():
    celDeg = input('Input temprature in degrees: ')
    #obtain convertion
    far = celsiusFar(celDeg)
    print  str(celDeg) + ' Degrees is equal to ' + str(far) + ' Farenheit Degrees'
    
    
if __name__ == '__main__':
    userInput()