from functools import reduce

def toC(temp):
    '''convert the given temperature from ^F to ^C'''
    return (10/18)*(temp-32)
def toF(temp):
    '''convert the given temperature from ^c to ^F'''
    return (18/10)*temp+32
def listToC(l):
    '''convert a list F telp into C'''
    return list(map(toC,l))
def tempStats(listF):
    '''convert a list of F into C and computesimple statisitcs'''
    def myMin(x,y):
       # if (x < y):
        #    result = x
        #else:
         #   result = y
        r#eturn result
        return x if x<y else y
    def myMax(x,y)
        return x if x>y else y
    
    listC = listToC(listF)
    mintemp = list(reduce(myMin,min(listC)))
    maxtemp = list(reduce(myMax,max(listC)))
    return [mintemp,maxtemp,listC]
