"""
    1. Run the program
    2. Type inverse( [ [a,b],[c,d] ] )
        where abcd are numbers
    inverse() takes in a single sqaure matrix
    
    | a b |
    | c d |
    
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
        xxxx    xxxx    xxxx    xxxx    xxxx    xxxx
        xxxx  > xxxx  > xxxx  > 0xxx  > 0xxx  > 0xxx
        xxxx    0xxx    0xxx    0xxx    00xx    00xx
        0xxx    0xxx    00xx    00xx    00xx    000x
        
        row := row - (current/above) * (above_row)
        if current = 0, do nothing
    """
    return [a,identity]


#returns [a,identity] updated
def diag(a,identity):
    """Plan:        
        1xxx    1xxx    1xxx    1xxx
        0xxx  > 01xx  > 01xx  > 01xx
        00xx    00xx    001x    001x
        000x    000x    000x    0001
        
        row := (1/current) * row
        if current = 1, do nothing
    """                     
    return [a,identity]
    

#returns [a,identity] updated
def lowerT(a,identity):
    """Plan:
        1xx0    1xx0    1x00    1x00    1x00    1000
        01xx  > 01x0  > 01x0  > 01x0  > 0100  > 0100
        001x    001x    001x    0010    0010    0010
        0001    0001    0001    0001    0001    0001

        row := row - (current/below) * (below_row)
        if current = 0, do nothing
    """
    return [a,identity]


#switches rows so that 0 is in bottom left or top right
def switch(a,identity):
    """Plan:
        For each step, start from the bottom-up
        1. Check if an entire row has 0s, then it's un-invertible
        2. Check if an entire row has 3 0s, position it at the right row, and lock the row
            If there are 2 rows that need to get in the same row, it's un-invertible
        3. Check if an entire row has 2 0s, place it not on diagonal, starting from bottom, lock the row
            If the the row needs to place in a locked row, check above
            If it's on a diagonal, check the row above
            If you get to the top-most row, and it's locked, it's un-invertible
        4. Check if an entire row has 1 0s, lock the row
            If it's on a diagonal, check the row above
            If the row needs to be place in a locked row, check above
            If you get to the top-most row, and it's locked, it's un-invertible
        5. Check the matrix if there's a number below a 0 below the diagonal
            if there is, then it's un-invertible
        6. Check the matrix if there's a number above a 0 above the diagonal
            if there is, then it's un-invertible
        7. Check if there's a 0 in the diagonal
            if there is, you screwed up, since this should not be possible, and it's un-invertible
        7. return the matrix
    """
        return[a,identity]
    

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
        1. Switch
        2. UpperT
        3. Diag
        4. LowerT
    """
    
    #1. Switch
    augment = switch(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter switch(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)

    #2. UpperT
    augment = upperT(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter upperT(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #3. Diag
    augment = diag(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter diag(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #4. LowerT
    augment = lowerT(a,identity)
    a = augment[0]
    identity = augment[1]
    print("\nAfter lowerT(), augmented matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    #Step 4: Return the Identity Matrix
    return identity
