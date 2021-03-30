from functools import reduce
def gauss(N):
    return reduce(add,list(range(N+1)))
def add(x,y):
    print(x+y**2)
    return x+y**2
sum = gauss(4)
print(sum)

