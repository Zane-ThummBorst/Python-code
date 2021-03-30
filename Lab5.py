#Zane Thummborst
#I pledge on my honor that I have abided by the Stevens Honor System
def svTree(trunkLength,depth):
    '''draws a tree given a length and a depth'''
    if depth > 0:
        turtle.forward(trunkLength)
        turtle.left(20)
        svTree(trunkLength*.5,depth-1)
        turtle.right(40)
        svTree(trunkLength*.5,depth-1)
        turtle.left(20)
        turtle.backward(trunkLength)

svTree(150,5)

    
