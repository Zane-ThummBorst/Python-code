from functools import reduce

def change(amount,coins):
    '''returns the minimum amount of coins needed for the amount if possible'''

    def stop(y,z):
        '''tells the program to stop if the program can no longer reduce the amount'''
        if isinstance(y, bool):
            return y and amount%z == amount
        else:
            return amount%y == amount and amount%z == amount
        
    def checkRemainder(y,z):
        '''determines what coins to use first based on the smallest remainder in the current amount'''
        if(amount%y < amount%z):
            return y
        elif (amount%y > amount%z):
            return z
        else:
            return max(y,z)
    
    if amount == 0:
        return 0
    elif reduce(stop,coins) or amount < 0:
        return float("inf")
    else:
        r = reduce(checkRemainder,coins)
        return 1 + change(amount-r,coins)


#Zane ThummBorst
#I pledge on my honor that I have abided by the Stevens Honor System
