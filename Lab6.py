#Zane ThummBorst
#I Pledge My Honor That I Have Abided By The Stevens Honor System.
def decimalToBinary(num):
    '''converts from a decimal to binary'''
    if num >= 1:
        '''return creates list of the binary value, and recursivly calls the function'''
        return [num%2]+decimalToBinary(num//2)
    else:
        '''returns an empty string if num is less than 1'''
        return []



def binaryToDecimal(num):
    '''converts from a binary to a decimal'''
    if not num:
        '''checks if list is empty'''
        return 0
    elif num[-1] == 1:
        '''checks last value of num if it is equal to one'''
        return 2**(len(num)-1) + binaryToDecimal(num[0:len(num)-1])
    else:
        '''final test case where num[0] equals zero, so it does not get addded to the list'''
        return binaryToDecimal(num[0:len(num)-1])



def incrementBinary(num):
    '''increments the niary number by 1'''
    if not num:
        ''' because we reach this test case, we add one to the end to increase list length'''
        return [1]
    if num[0] == 0:
        ''' checks for first value in list that is zero'''
        num[0] = 1
        return num
    elif num[0] == 1:
        ''' recursivly calls if LSB is equal to 1.'''
        num[0] = 0
        return [num[0]] + incrementBinary(num[1:])




def addBinary(num1,num2):
    '''adds two binary numbers'''
    def checklen(num1,num2):
        '''makes both lists equal in length'''
        if len(num1) == len(num2):
            return [num1,num2]
        elif len(num1) > len(num2):
            return checklen(num1,num2 + [0])
        else:
            return checklen(num1 + [0],num2)
        
    def helpAdd(c,num1,num2):
        ''' adds both binary numbers with the help of a carry variable'''
        if not num1 or not num2:
            if c > 0:
                '''adds the carry if it is a value'''
                return [c]
            else:
                return []
        else:
            '''bit addition'''
            head1 = num1[0]
            head2 = num2[0]
            x = head1+head2+c
            return [x%2] + helpAdd(x//2,num1[1:],num2[1:])

    L = checklen(num1,num2)
    '''list with equal length lists'''
    num1 = L[0]
    num2 = L[1]
    return helpAdd(0,num1,num2)



        

