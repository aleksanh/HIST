'''
Created on 12. feb. 2015

@author: alh
'''

def a():
    #generate a list with the days of a week
    lst = ['monday', 'tusday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday']
    return lst

def b(lst):
    # print all the elements in a list. 
    
    for i in lst:
        print i
        
def b_showOff(lst):
    
    for i in lst:
        for char in i:
            print char
        print ' '
        
def c(lst):
    numElements = len(lst)
    print 'length of the list is: ' + str(numElements) + 'elements'
    return(numElements)

def d():
    lst = a()
    lst.sort()
    print '\nweek list printed alphabeticly'
    for i in lst:
        print i 
    
    
if __name__ == '__main__':
    lst = a()  #get the list of days in a week. 
    b(lst) # print all the elements in the list. 
    b_showOff(lst) # print in another fancy way..... 
    c(lst) # print the length of list
    d() #perform task d
    
    
