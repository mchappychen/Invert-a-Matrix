#returns: b[] x a
def multiply(a,b):
    result = []
    for i in range(len(b)):
        result.append(b[i] * a)
    return result


#returns [a[]+b[]]
def add(a,b):
    result = []
    if(len(a) != len(b)):
        print("Error in add(a,b): length of a[] not equal to length of b[]")
        return None
    for i in range(a):
        result.append(a[i]+b[i])
    return result


#prints a[[]]
def printMatrix(a):
    for x in a:
        string = "| "
        for y in x:
            string += str(y)+" "
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
        return None
    if(len(a) != len(a[0])):
        print("Error in inverse(a): You need to input a sqaure matrix")
    for x in a:
        for y in x:
            if(y == None):
                print("Error in inverse(a): Matrix is missing values")


#returns [a,identity] updated
def upperT(a,identity):
    for j in range(len(a[0])):
        for i in range(len(a)):
            if(i>j):
                a[i][j] = "a"
    return [a,identity]
    

#returns [a,identity] updated
def diag(a,identity):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i==j):
                a[i][j] = "b"
    return [a,identity]
    

#returns [a,identity] updated
def lowerT(a,identity):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i<j):
                a[i][j] = "c"
    return [a,identity]


#a[[]] = matrix to invert
def inverse(a):
    #Step 1: Check for errors:
    checkErrors(a)
            
    #Step 2: Print the Matrix + Identity Matrix
    print("\nYour Matrix looks like:\n")
    printMatrix(a)
        
    #Step 3: Create Identity Matrix
    identity = []
    for x in range(len(a)):
        element = []
        for y in range(len(a)):
            if(x == y):
                element.append(1)
            else:
                element.append(0)
        identity.append(element)
    print("Identity Matrix looks like:\n")
    printMatrix(identity)
    
    #Step 4: Do the operations 
    augment = upperT(a,identity)
    a = augment[0]
    identity = augment[1]
    augment = diag(a,identity)
    a = augment[0]
    identity = augment[1]
    augment = lowerT(a,identity)
    a = augment[0]
    identity = augment[1]
    
    #Step 5: Print both matricies
    print("\n\nAfter operations, your matrix looks like:\n")
    printMatrix(a)
    print("The Identity matrix now looks like:\n")
    printMatrix(identity)
    
    #Step 6: Return the updated Identity Matrix
    return identity
