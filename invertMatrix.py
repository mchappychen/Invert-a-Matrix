#returns: b[] x a
def multiply(a,b):
    if(a == 0):
        print("Error in multiply(): You can't multiply matrix by 0")
        return None
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
        return None
    if(len(a) != len(a[0])):
        print("Error in inverse(a): You need to input a sqaure matrix")
    for x in a:
        for y in x:
            if(y == None):
                print("Error in inverse(a): Matrix is missing values")


#returns [a,identity] updated
def upperT(a,identity):
    """Plan:
        1. Find an element within the upper triangle
        2. If the element is 0, do nothing
        3. If the element is 1-9:
            find the diagonal element in the same column
            if the element is negative, multiply the diagonal-element row by (element)
            if the element is positive, multiply the diagonal-element row by (-1.0 * element)
            add the diagonal-element row into the element row
    """
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i<j and a[i][j] != 0):
                rowDiagonal = a[j]
                if(a[i][j] > 0):
                    rowDiagonal = multiply(a[i][j],rowDiagonal)
                    rowIdentity = multiply(a[i][j],identity[j])
                    a[i] = add(a[i],rowDiagonal)
                    identity[i] = add(a[i],rowIdentity)
                else:
                    rowDiagonal = multiply(a[i][j] * -1, rowDiagonal)
                    rowIdentity = multiply(a[i][j] * -1, identity[j])
                    a[i] = add(a[i],rowDiagonal)
                    identity[i] = add(a[i],rowIdentity)
    return [a,identity]


#returns [a,identity] updated
def diag(a,identity):
    """Plan:
        1. Find a diagonal element
        2. If the diagonal element is 1, do nothing
        3. If the diagonal element is 2-9, multiply the row by 1.0/element
        4. If the diagonal element is 0:
            find another row that is 1-9, multiply it by 1.0/element, add it to the row
    """
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i==j and a[i][j] != 1):
                if(a[i][j] != 0):
                    arrayA = multiply(1.0/a[i][j],a[i])
                    a[i] = arrayA
                    arrayIdentity = multiply(1.0/a[i][j],identity[i])
                    identity[i] = arrayIdentity
                else:
                    fail = True
                    for x in range(len(a)):
                        if(a[x][j] != 0 and x != i):
                            fail = False
                            arrayA = multiply((1.0/(a[x][j])),a[x])
                            a[i] = add(a[i],arrayA)
                            arrayIdentity = multiply((1.0/(a[x][j])),identity[x])
                            identity[i] = add(identity[i],arrayIdentity)
                            break
                    if(fail):
                        print("Error in diag(): Everything column "+str(j)+" is 0")
                            
    return [a,identity]
    

#returns [a,identity] updated
def lowerT(a,identity):
    """Plan:
        1. Find an element within the lower triangle
        2. If the element is 0, do nothing
        3. If the element is 1-9:
            find the diagonal element in the same column
            if the element is negative, multiply the diagonal-element row by (1.0 * element)
            if the element is positive, multiply the diagonal-element row by (-1.0 * element)
            add the diagonal-element row into the element row
    """
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i>j):
                a[i][j] = -1
            
    return [a,identity]


#a[[]] = matrix to invert
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
