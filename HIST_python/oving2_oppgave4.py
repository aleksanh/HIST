'''
Created on 2. mar. 2015

@author: alh
'''
import operator


class simplecalc(object):
    def __init__(self,val1,val2,userOperator,auto):
        self.val1 = self.auto_int_float(val1)
        self.val2 = self.auto_int_float(val2)
        self.op = userOperator
        
        
    def calc(self):
        if self.op == '+':
            return operator.add(self.val1, self.val2)
        if self.op == '-':
            return operator.sub(self.val1, self.val2)
        if self.op == '*':
            return operator.mul(self.val1, self.val2)
        
    def string_checker(self, value_str):
        if not value_str:
            return '0'
        return value_str


    def auto_int_float(self, value_str):
        ok_value = self.string_checker(value_str)
        if '.' in ok_value:
            return float(ok_value)
        else:
            return int(ok_value)
        

def userInput():
    usrInp = raw_input('Welcome to simple calc, please input two values and a operator with space between them: ')
    if len(usrInp) < 5:
        raise ValueError('Inputed data not of proper length')
    userInp = usrInp.split()
    
    c = simplecalc(userInp[0], userInp[1], userInp[2], True)
    print c.calc()
    
    
if __name__ == '__main__':
    userInput()

        
        