'''
Created on 2. mar. 2015

@author: alh
'''

#oppgave a
def writeToFile(filename, strList):
    fobj = open(filename,'w')
    
    for str in strList:
        fobj.write(str + '\n')
    fobj.close()
    
#oppgave b , det er ikke sagt hva som skal gjores med linja, jeg printer....    
def readLineInfile(filename,lineofint):
    fobj = open(filename,'r')
    
    lines = fobj.readlines()
    print lines[lineofint]
    fobj.close()
#oppgave c
def readNchars(filename, chartoread):    
    fobj = open(filename,'r')
    
    chars = fobj.read(chartoread+1) #legger til 1 pga 0 index i python
    print chars
    fobj.close()
    


strList = ['Hallo', 'Skriver en linje til', 'Her kommer enda en linje']
filename = r'test.txt'

if __name__ == '__main__':
    while True:
        opp=  raw_input('oppgave som skal testes a,b eller c? (q = exit) :')
        if opp == 'a': 
            writeToFile(filename, strList)
        if opp == 'b': 
            readLineInfile(filename, 1)
        if opp == 'c':   
            readNchars(filename, 10)
        if opp == 'q':
            break 
