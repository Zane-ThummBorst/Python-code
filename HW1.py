from functools import reduce
from math import factorial
from math import sqrt

def taylorApproxE(lastIter):
    ''' aproximates the taylor series of e to the specified interation'''
    def add(x,y):
        '''adds x and y'''
        return x + y
    def inverse(x):
        ''' inverses x'''
        return 1/x
    L = list(map(factorial,(range(lastIter+1))))
    inverseL = list(map(inverse,L))
    print(reduce(add,inverseL))

def vectorNorm(vect1):
    '''  calculates the vector norm of the list'''
    def square(x):
        '''squares the x given'''
        return x*x
    def add(x,y):
        '''adds x and y'''
        return x + y
    squareList =list(map(square, vect1))
    print(sqrt(reduce(add, squareList)))
    
def arithMean(vect1):
    '''calculates the mean of the list given'''
    def add(x,y):
        '''adds x and y together'''
        return x + y
    L = reduce(add,vect1)
    print(L/len(vect1))

# Zane ThummBorst
# I pledge my honor that I have abided by the Stevens Honor System
