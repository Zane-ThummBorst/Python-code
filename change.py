from functools import reduce

def change(amount,coins):
    ''' return minimum amount of coins required to reach total'''
    if 0 == amount:
        ''' first base case of coins reaching amount'''
        return 0
    if coins == [] or amount < 0:
        ''' base case to test if its possilbe to reach amount'''
        return float("inf")
    else:
        '''use it or lose it method'''
        x = change(amount - coins[0],coins) + 1
        y = change(amount,coins[1:])
    return min(x,y)



#Zane ThummBorst
#I pledge on my honor that I have abided by the Stevens Honor System
