List1 = ['hello', 'at', 'may', 'goat']
from functools import reduce

def length(x):
    '''places the length of the string and the string into a list with two
indices'''
    return [len(x),x]

def check(x,y):
    '''compares the values of the lengths of x and y,then returns the larger value.'''
    return max(x, y)

listoflists = list(map(length,List1))
list3 = reduce(check,listoflists)
print ("The largest string in the list is: " + list3[1])


#Zane ThummBorst
#I pledge my Honor that I have abided by the Stevens Honor System
#test case1 = ['hello', 'at', 'may', 'goat']
#test case2 = ['hello', 'evening', 'hi', 'hola']
#test case3 = ['hi', 'howdy', 'salutations', 'hey']
#test case4 = ['hi', 'hello', 'hey', 'goodbye']
