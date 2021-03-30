#
# Zane ThummBorst
#
#9/9/19
#
# demonstrate recursiuon through the factorial
# and list length

def myFactorial(x):
    ''' return the factorial of x assuming x is > 0'''
#    if x == 0:
#        return 1
#    else:
#        return x * myFactorial(x-1)
    return 1 if x==0 else x*myFactorial(x-1)

#print(myFactorial(2))

def myLength(L):
    '''return the length of the list L'''
    if L == []:
        return 0
    else:
        return 1 + myLength(L[1:])
    
#print(myLength([1,2,3]))
def LCS(S1,S2):
    ''' return the longest common subsequence between the strings'''
#    if len(S1) == 0 or len(S2) == 0:
#        return 0
#    elif S1[0] == S2[2]:
#        #A common firsdt character adds 1 to LCS
#        return 1 + LCS(S1[1:], S2[1:])
#    else:
#        #Drop either first character and recurse
#        max(LCS(S1, S2[1:]), LCS(S1, S2[1:]))


#NEXT EXAMPLE IS CRUCIAL FOR RECURSION LAB
def deepLength(L):
    if not L:
        return 0
    else:
        head, tail = L[0], L[1:]
        headVal = deepLength(head) if isinstance(head,list)else 1
        return headVal + deepLength(tail)


                   
