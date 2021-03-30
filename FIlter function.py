# recursion using filter

def myFilter(f,L):
    ''' home-brew version of filter'''
    baseVal = []
    def recursiveStep(head,tail):
        if f(head):
            return [head] + myFilter(f,tail)
        else:
            return myFilter(f,tail)

    return baseVal if not L\
           else recursiveStep(L[0], L[1:])
