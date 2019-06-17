from sys import exit
import random

debug = False
secretDebug = True

def matrixMult(a,b): #returns [] of a[] x b[]
    result = []
    for i in range(len(a)):
        array = []
        for j in range(len(b[0])):
            element = 0
            for k in range(len(a[0])):
                element += a[i][k] * b[k][j]
            array.append(element)
        result.append(array)
    return result

def multiply(a,b): #returns: [] of a x b[]
    if(a == 0):
        exit("Error in multiply(): You can't multiply matrix by 0")
    result = []
    for element in b:
        result.append(element * a)
    return result

def add(a,b): #returns [] of a[]+b[]
    result = []
    if(len(a) != len(b)):
        exit("Error in add(a,b): length of a[] not equal to length of b[]")
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result

def printMatrix(a): #prints a matrix
    for x in a:
        string = "|\t"
        for y in x:
            string += str(round(y,2)+0)+"\t"
        string += "|"
        print(string)
    print("")

def printAugmentedMatrix(a,b): #prints a[]|b[]
    for x in range(len(a)):
        string = "|\t"
        for y in range(len(a[0])):
            string += str(round(a[x][y],2)+0) + "\t"
        string += "|\t"
        for y in range(len(b[0])):
            string += str(round(b[x][y],2)+0) + "\t"
        string += "|"
        print(string)
    print("")
    
def checkErrors(a): #Makes sure inverse() input is correct format
    try:
        t = a[0][0]
        del t
    except TypeError:
        exit("Error in inverse(a): You need to input a matrix")
    if(len(a) != len(a[0])):
        exit("Error in inverse(a): You need to input a square matrix")
    for x in a:
        for y in x:
            if(y == None):
                exit("Error in inverse(a): Matrix is missing values")
                
def formatZeros(a): #turns -0.0 into 0.0
    for x in range(len(a)):
        for y in range(len(a)):
            a[x][y] += 0
    return a

def upperT(a,identity): #returns [a,identity] updated
    """Plan:
        x x x x     x x x x     x x x x     x x x x     x x x x     x x x x
        x x x x --> x x x x --> 0 x x x --> 0 x x x --> 0 x x x --> 0 x x x
        x x x x     0 x x x     0 x x x     0 x x x     0 0 x x     0 0 x x 
        0 x x x     0 x x x     0 x x x     0 0 x x     0 0 x x     0 0 0 x
        
        loop from bottom-to-up:
            if it's not 0:
                while(above is 0):
                    above := above again
                    if above out of index:
                        throw error
                row := row + (-1 * current/above) * (above_row)
    """
    for columns in range(len(a)-1):
        for rows in range(len(a)-1,columns,-1):
            if(a[rows][columns] != 0):
                above = 1
                while(a[rows-above][columns] == 0):
                    above += 1
                    if(rows-above < 0):
                        print("Error in UpperT() for (",rows,",",columns,"), a looks like:\n")
                        printMatrix(a)
                        exit("There's a 0 above the number")
                multiplier = (-1.0 * a[rows][columns])/a[rows-above][columns]
                a[rows] = add(multiply(multiplier,a[rows-above]) , a[rows])
                identity[rows] = add(multiply(multiplier,identity[rows-above]) , identity[rows])
    a = formatZeros(a)
    identity = formatZeros(identity)
    return [a,identity]

def diag(a,identity): #turns diagonal into 1
    """Plan:        
        1 x x x     1 x x x     1 x x x     1 x x x 
        0 x x x --> 0 1 x x --> 0 1 x x --> 0 1 x x
        0 0 x x     0 0 x x     0 0 1 x     0 0 1 x
        0 0 0 x     0 0 0 x     0 0 0 x     0 0 0 1
        
        loop diagonally:
            if current is not 1:
                row := (1/current) * row
    """
    for row_index in range(len(a)):
        for column_index in range(len(a[0])):
            if(row_index == column_index and a[row_index][column_index] != 1):
                if(a[row_index][column_index] == 0):
                    print("Error in diag(): There's a 0 on the diagonal in ("+str(row_index)+","+str(column_index)+")")
                    print("Matrix is un-invertible")
                    return None
                multiplier = 1.0/a[row_index][column_index]
                a[row_index] = multiply(multiplier,a[row_index])
                identity[row_index] = multiply(multiplier,identity[row_index])
    a = formatZeros(a)
    identity = formatZeros(identity)
    return [a,identity]

def lowerT(a,identity): #returns [a,identity] updated
    """Plan:
        1 x x 0     1 x x 0     1 x x 0     1 x 0 0     1 x 0 0     1 0 0 0
        0 1 x x --> 0 1 x 0 --> 0 1 x 0 --> 0 1 x 0 --> 0 1 0 0 --> 0 1 0 0
        0 0 1 x     0 0 1 x     0 0 1 0     0 0 1 0     0 0 1 0     0 0 1 0 
        0 0 0 1     0 0 0 1     0 0 0 1     0 0 0 1     0 0 0 1     0 0 0 1

        loop from top-to-down:
            if it's not 0:
                while(below is 0):
                    below := below again
                    if below out of index
                        throw error
                row := row + (-1 * (current/below)) * (below_row)
    """
    for columns in range(len(a)-1,0,-1):  
        for rows in range(0,columns,1):
            if(a[rows][columns] != 0 and (rows != columns)):
                below = 1
                while(a[rows+below][columns] == 0):
                    below += 1
                    if(rows+below > len(a)-1):
                        print("Error in lowerT() for (",rows,",",columns,"), a looks like:\n")
                        printMatrix(a)
                        exit("There's a 0 above the number")
                multiplier = (-1.0 * a[rows][columns])/a[rows+below][columns]
                a[rows] = add(multiply(multiplier,a[rows+below]) , a[rows])
                identity[rows] = add(multiply(multiplier,identity[rows+below]) , identity[rows])
    a = formatZeros(a)
    identity = formatZeros(identity)
    return [a,identity]

def checkInverseMatrix(A_inverse,A): #checks if A-inverse x A = Identity
    """Plan:
        1. Create identity matrix
        2. Multiply A_inverse by A
        3. Check if the result is equivalent to identity matrix
    """
    #1 Create identity matrix
    identity = []
    for x in range(len(A_inverse)):
        row = []
        for y in range(len(A_inverse)):
            if(x == y):
                row.append(1.0)
            else:
                row.append(0.0)
        identity.append(row)
                
    #2 Multiply A_inverse by A
    A_inverse = matrixMult(A_inverse,A)
    
    #3 Check if the result is equal to identity
    A_inverse = formatZeros(A_inverse)
    if(debug):
        print("A-1 x A becomes:\n")
        printMatrix(A_inverse)
    success = True
    for x in range(len(A_inverse)):
        for y in range(len(A_inverse)):
            if(x == y):
                if(round(A_inverse[x][y],2) != 1.00):
                    print("A-1 x A Error: (",x,",",y,") is",round(A_inverse[x][y],2),"but should be 1")
                    success = False
            else:
                if(round(A_inverse[x][y],2) != 0.0):
                    print("A-1 x A Error: (",x,",",y,") is",round(A_inverse[x][y],2),"but should be 0")
                    success = False
    if(success):
        if(debug):
            print("Successfully inverted matrix\n")
    else:
        print("Matrix inversion failed")

def switch(a,identity): #repositions 0s so that it isn't on diagonal
    """Plan:
        1. If an entire row is 0:
            throw an error, it's un-invertible
        2. Create a new array[] 
        3. For each row:
            Make another array, called a vector[]
            In the vector, put the indices of where the row can be switched to
            Append the vectors into array[]
        3. For each vector[] in array[]:
            Change vector from this: [a,b,c] --> [x,[a,b,c]]
                where x is the number of 0s in that (corresponding) row
        4. For each vector[] in array[]:
            Change vector from this: [x,[a,b,c]] --> [x,[a,b,c],m]
                where m is the position of where the array will be switched
                    find m by:
                        1. creating a canBePlaced[] of the rows that the row can be switched into
                        2. If it's empty, it's un-invertible, throw an error
                        3. If it only has one item, that is m
                        4. If it has more than one item, choose the item with the smallest length
        5. Swap all the rows accordingly into another matrix, then set that matrix to a/identity
        6. Check if there's any 0s in the diagonal, if there is, throw an error
    """
    for x in range(len(a)): #1 If an entire row is 0: un-invertible
        allZeros = True
        for y in range(len(a)):
            if(a[x][y] != 0.0):
                allZeros = False
                break
        if(allZeros):
            print("Error in switch(): Row ",x," is all 0s")
            return None
    array = [] #2 Create a new array[]
    for x in range(len(a)): #3 Place vector[]s in array = [[],[],[]]
        vector = []
        for y in range(len(a)):
            if(a[x][y] != 0):
                vector.append(y)
        array.append(vector)
    array2 = [] #3 For each vector[] in array[], [a,b,c] --> [x,[a,b,c]]
    for vector in array:
        zeroes = 0
        for x in range(len(a)):
            if(not x in vector):
                zeroes += 1
        array2.append([zeroes,vector])
    array = array2.copy()
    del array2
    for y in range(len(a)-1,-1,-1): #4 [x,[a,b,c]] --> [x,[a,b,c],m]
        canBePlaced = []
        for x in range(len(array)):
            if(y in array[x][1] and len(array[x]) < 3):
                canBePlaced.append(x)
        if(len(canBePlaced) == 0):
            print("Error in Switch(): Matrix is un-invertible by me")
            return None
        elif(len(canBePlaced) == 1):
            array[canBePlaced[0]].append(y)
        else:
            smallest = canBePlaced[0]
            for x in range(1,len(canBePlaced)):
                if(len(array[x][1]) < len(array[smallest][1])):
                    smallest = canBePlaced[x]
            array[smallest].append(y)
    newMatrixA = [] #5 Swap all the rows into a new matrix
    newMatrixIdentity = []
    for x in range(len(array)):
        for y in range(len(array)):
            if(array[y][2] == x):
                newMatrixA.append(a[y])
                newMatrixIdentity.append(identity[y])
                break
    a = newMatrixA.copy()
    identity = newMatrixIdentity.copy()
    del newMatrixA
    del newMatrixIdentity
    for row_index in range(len(a)): #6 checks for any 0s in diagonal
        for column_index in range(len(a[0])):
            if(row_index == column_index and a[row_index][column_index] == 0):
                printAugmentedMatrix(a,identity)
                exit("Error in switch(): There's a 0 in a diagonal in row "+ str(row_index))    
    a = formatZeros(a)
    identity = formatZeros(identity)
    return[a,identity]
    
def inverse(a): #inverts a matrix
    #Copy a into temp without making a reference
    temp = []
    for x in a:
        temp2 = []
        for y in x:
            temp2.append(y)
        temp.append(temp2)
    #Step 1: Check for errors:
    checkErrors(a)
        
    #Step 2: Create Identity Matrix
    identity = []
    for x in range(len(a)):
        element = []
        for y in range(len(a)):
            if(x == y):
                element.append(1.0)
            else:
                element.append(0.0)
        identity.append(element)

    #Step 3: Print augmented matrix
    if(secretDebug):
        print("\nAugmented Matrix looks like:\n")
    printAugmentedMatrix(a,identity)
    
    """Master Plan:
        1. Switch
        2. UpperT
        3. Diag
        4. LowerT
        5. Check A-1 x I = A
    """
    #1. Switch rows
    augment = switch(a,identity)
    if(augment == None):
        return None
    a = augment[0]
    identity = augment[1]
    if(debug):
        print("\nAfter switch(), augmented matrix looks like:\n")
        printAugmentedMatrix(a,identity)

    #2. UpperT
    augment = upperT(a,identity)
    a = augment[0]
    identity = augment[1]
    if(debug):
        print("\nAfter upperT(), augmented matrix looks like:\n")
        printAugmentedMatrix(a,identity)
    
    #3. Diag
    augment = diag(a,identity)
    if(augment == None):
        return None
    a = augment[0]
    identity = augment[1]
    if(debug):
        print("\nAfter diag(), augmented matrix looks like:\n")
        printAugmentedMatrix(a,identity)
    
    #4. LowerT
    augment = lowerT(a,identity)
    a = augment[0]
    identity = augment[1]
    if(debug):
        print("\nAfter lowerT(), augmented matrix looks like:\n")
    if(secretDebug):
        printAugmentedMatrix(a,identity)
    
    #Step 5: Check A-1 x A = I
    checkInverseMatrix(identity,temp)
    identity = formatZeros(identity)
    return identity

def main(): #creates a matrix for inverse()
    global debug
    global superdebug
    response = input("Would you like to enable debug? Type ('yes' or 'y') :: ")
    if(("y" == response ) or ("yes" == response)):
        debug = True
    else:
        debug = False
    print("Debug turned to ",debug)
    correctResponse = False
    while(not correctResponse):
        response = input("Enter \'1\' for manual input, or \'2\' for auto-generated input, or \'3\' to exit :: ")
        if(not response in ("1","2","3")):
            print("Only enter 1, 2 or 3")
        else:
            correctResponse = True
    if(response == "1"):
        correctInput = True
        while(correctInput):
            try:
                rows = int(input("How many rows/columns for your matrix? :: "))
                if(rows > 0):
                    correctInput = False
                else:
                    print("You did not enter a positive natural number, try again!")
            except ValueError:
                print("You did not enter a number, try again!")      
        matrix = []
        for x in range(rows):
            row = []
            for y in range(rows):
                correctInput = True
                while(correctInput):
                    try:
                        row.append(float(input("Enter row "+str(x)+" column "+str(y)+" :: ")))
                        correctInput = False
                    except ValueError:
                        print("You did not enter a number, try again!")
            matrix.append(row)
        inverse(matrix)
    elif(response == "2"):
        correctInput = True
        while(correctInput):
            try:
                runNumber = int(input("How many trials would you like to run this? :: "))
                if(runNumber > 0):
                    correctInput = False
                else:
                    print("You did not enter a positive natural number, try again!")
            except ValueError:
                print("You did not enter a number, try again!")
        correctInput = True
        while(correctInput):
            try:
                rows = int(input("How many rows/columns for your matrix? :: "))
                if(rows > 0):
                    correctInput = False
                else:
                    print("You did not enter a positive natural number, try again!")
            except ValueError:
                print("You did not enter a number, try again!")
        for iteration in range(runNumber):
            matrix = []
            for x in range(rows):
                row = []
                for y in range(rows):
                    row.append(abs(round(random.random()*2-random.random()*10,0)))
                matrix.append(row)
            inverse(matrix)
    elif(response == "3"):
        pass
    else:
        exit("Error in main(): This is unreachable code")

if __name__ == "__main__": #calls main() when program starts
    main()
