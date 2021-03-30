#Zane ThummBorst
#I pledge my honor that I have abided by the Stevens Honor System
def dotProduct(L,K):
    '''Takes the dot product of two list'''
    if L == []:
        return 0
    else:
        return (L[0]*K[0] + dotProduct(L[1:],K[1:]))

def expand(S):
    '''Takes a string and puts its individual letters into a list'''
    if S == "":
        return []
    else:
        return list(S[0])+expand(S[1:])


def deepMember(e,L):
    '''Checks to see if the values e is anywhere in the list L'''
    if L == []:
        return False
    elif isinstance(L[0],list):
        L2 = deepMember(e,L[0])
        return L2 if L2 == True else deepMember(e,L[1:])
    elif e != L[0]:
        return deepMember(e,L[1:])
    elif e == L[0]:
        return True
    return False

        
def removeAll(e,L):
    '''Removes all values of e in list L at the top level'''
    if L == []:
        return L
    elif e != L[0]:
        return [L[0]] + removeAll(e,L[1:])
    elif e == L[0]:
        return (removeAll(e,L[1:]))
    
def deepReverse(L):
    ''' reverses all elements in the list at every level (even values in a list of lists)'''
    if L == []:
        return []
    elif isinstance(L[0],list):
        L2 = deepReverse(L[0])
        return deepReverse(L[1:]) + [L2]
    elif L != []:
        return deepReverse(L[1:]) + [L[0]]
    elif L == []:
        return []
