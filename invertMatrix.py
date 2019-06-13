"""
    Author: Michael
    1. Run the program
    2. Type inverse( [ [a,b],[c,d] ] )
        where abcd are numbers
    inverse() takes in a single sqaure matrix
"""
from sys import exit

#returns: b[] x a
def multiply(a,b):
    if(a == 0):
        print("Error in multiply(): You can't multiply matrix by 0")
        exit()
    result = []
    for i in range(len(b)):
        result.append(b[i] * a)
    return result


#returns [a[]+b[]]
def add(a,b):
    result = []
    if(len(a) != len(b)):
        print("Error in add(a,b): length of a[] not equal to length of b[]")
        exit()
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result


#prints a[[]]
def printMatrix(a):
    for x in a:
        string = "|\t"
        for y in x:
            string += str(y)+"\t"
        string += "|"
        print(string)
    print("")
    

#prings a[[]] | b[[]]
def printAugmentedMatrix(a,b):
    for x in range(len(a)):
        string = "|\t"
        for y in range(len(a[0])):
            string += str(round(a[x][y],2)) + "\t"
        string += "|\t"
        for y in range(len(b[0])):
            string += str(round(b[x][y],2)) + "\t"
        string += "|"
        print(string)
    print("")


#makes sure a[[]] is correct format
def checkErrors(a):
    try:
        t = a[0][0]
        del t
    except TypeError:
        print("Error in inverse(a): You need to input a matrix")
        exit()
    if(len(a) != len(a[0])):
        print("Error in inverse(a): You need to input a sqaure matrix")
        exit()
    for x in a:
        for y in x:
            if(y == None):
                print("Error in inverse(a): Matrix is missing values")
                exit()


#returns [a,identity] updated
def upperT(a,identity):
    """Plan:
        
    """
    return [a,identity]


#returns [a,identity] updated
def diag(a,identity):
    """Plan:
        
    """                     
    return [a,identity]
    

#returns [a,identity] updated
def lowerT(a,identity):
    """Plan:
        
    """
    return [a,identity]


#switches rows so that 0 is in bottom left or top right
def switch(a,identity):
    """Plan:
    """

def inverse(a):
    
    #Step 1: Check for errors:
    checkErrors(a)
        
    #Step 2: Create Identity Matrix
    identity = []
    for x in range(len(a)):
        element = []
        for y in range(len(a)):
            if(x == y):
                element.append(1)
            else:
                element.append(0)
        identity.append(element)

    #Step 3: Print augmented matrix
    print("\nAugmented Matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    """Master Plan:
        1. Swith rows until 0s are at the bottom or top of diagonal in switch()
        2. Set the bottom-left triangle to 0 in upperT()
        3. Set the diagonal to 1 in diag()
    """
    
    #Step 4: Switch rows so that 0s 
    #Step 4: Convert diagonal into 1
    augment = diag(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter diag(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #Step 5: Convert upper triangle into 0
    augment = upperT(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter upperT(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #Step 6: Convert lower triangle into 0
    augment = lowerT(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter lowerT(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #Step 7: Return the updated Identity Matrix
    return identity
