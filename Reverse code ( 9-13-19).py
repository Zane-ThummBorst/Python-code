def reverse(L):
#    if not L:
#        return []
#    else:
#        head,tail = L[0],L[1]
#        return reverse(tail) + [head]

    baseVal = []
    def recursiveStep(head,tail):
        return reverse(tail) + [head]

    return baseVal if not L \
           else recursiveStep(L[0],L[1:])

def member(x,L):
    '''check whether x occurs within L'''
    baseVal = False
    def recursiveStep(head,tail):
        return (x == head) or member(x,tail) # return x == head only when it is true, otherwise it continues with recursion

    return baseVal if not L \
           else recursiveStep(L[0],L[1:])


def myMap(f,L):
    '''home brew version of map'''
    baseVal = []
     
    def recursiveStep(head,tail):
        return [f(head)] + myMap(f,L[1:])
    
    return baseVal if not L \
           else recursiveStep(L[0],L[1:])


def myReduce(f,L):
    '''home brew version of map'''
    baseVal = L[0] # this crashes on empty list
    def recursiveStep(head,tail):
        return myReduce(f, [f(head,tail[0])]+tail[1:]) #f(head, tail[0]) + myReduce(f,tail)
    
    # reduce is different!
    return baseVal if 1 == len(L) \
           else recursiveStep(L[0],L[1:])
