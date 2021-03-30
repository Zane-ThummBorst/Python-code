from functools import reduce

def makeChange(val,coins):
    ''' returns the minimum amount of coins needed for val and what coins are used'''
    if 0 == val:
        ''' checks to see if val is empty'''
        return [0,[]]
    if coins == [] or val < 0:
        '''checks to see if  it is possible to get an amount of coins'''
        return [float("inf"),[]]
    else:
        x = makeChange(val - coins[0],coins)
        x[0] = x[0] + 1
        y = makeChange(val,coins[1:])

    if min(x[0], y[0]) == x[0]:
        '''checks which path has the least amount of coins'''
        return [x[0], x[1] + [coins[0]]]
    else:
        return [y[0], y[1]]


def LCS(a, b):
    '''finds the largest string in each pair'''
    if not (a and b):
        ''' checks to see if either a or b is empty'''
        return ''
    if (a[0]==b[0]):
        '''compares the first indices of a and b'''
        return a[0] + LCS(a[1:], b[1:])
    '''use it or lose it'''
    x = LCS(a[1:],b)
    y = LCS(a,b[1:])
    if len(x) > len(y):
        return x
    '''returns y because returning x would inverse a and b'''
    if len(x) == len(y):
        return y
    else:
        return y




def PLCS(a, b):
    def PLCS_helper(s1,s2,L):
        ''' helper function to create a list of indices'''
        if not s2:
            '''checks if s2 is empty'''
            return []
        if s1[0] == s2[0]:
            '''compares s1 and s2; adds to the list if true'''
            return [L] + PLCS_helper(s1[1:],s2[1:], L + 1)
        else:
            return PLCS_helper(s1[1:],s2,L+1)
    substring = LCS(a,b)
    if not substring:
        '''cheacks if any substring exists'''
        return[[-1],[-1]]
    '''creates the list containing two lists of indices'''
    return[PLCS_helper(a,substring,0),PLCS_helper(b,substring,0)]


#Zane Thummborst
#I pledge my honor that I have abided by the Stevens Honor System
