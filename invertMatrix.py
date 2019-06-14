from sys import exit

def matrixMult(a,b): #returns [a[]xb[]]
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
def multiply(a,b): #returns: [a x b[]]
    if(a == 0):
        exit("Error in multiply(): You can't multiply matrix by 0")
    result = []
    for element in b:
        result.append(element * a)
    return result
def add(a,b): #returns [a[]+b[]]
    result = []
    if(len(a) != len(b)):
        exit("Error in add(a,b): length of a[] not equal to length of b[]")
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result


#prints a[[]]
def printMatrix(a):
    for x in a:
        string = "|\t"
        for y in x:
            string += str(round(y,2))+"\t"
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
        exit("Error in inverse(a): You need to input a matrix")
    if(len(a) != len(a[0])):
        exit("Error in inverse(a): You need to input a square matrix")
    for x in a:
        for y in x:
            if(y == None):
                exit("Error in inverse(a): Matrix is missing values")

def upperT(a,identity): #returns [a,identity] updated
    """Plan:
        xxxx    xxxx    xxxx    xxxx    xxxx    xxxx
        xxxx  > xxxx  > xxxx  > 0xxx  > 0xxx  > 0xxx
        xxxx    0xxx    0xxx    0xxx    00xx    00xx
        0xxx    0xxx    00xx    00xx    00xx    000x
        
        if it's not 0:
            row := row + (-1 * current/above) * (above_row)
                Issue: 'above' could be 0
    """
    for columns in range(len(a)-1):
        for rows in range(len(a)-1,columns,-1):
            if(a[rows][columns] != 0):
                if(a[rows-1][columns] == 0):
                    exit("Error in upperT() There's a 0 above a number")
                multiplier = (-1.0 * a[rows][columns])/a[rows-1][columns]
                a[rows] = add(multiply(multiplier,a[rows-1]) , a[rows])
                identity[rows] = add(multiply(multiplier,identity[rows-1]) , identity[rows])
    return [a,identity]

def diag(a,identity): #turns diagonal into 1
    """Plan:        
        1xxx    1xxx    1xxx    1xxx
        0xxx  > 01xx  > 01xx  > 01xx
        00xx    00xx    001x    001x
        000x    000x    000x    0001
        
        row := (1/current) * row
        if current = 1, do nothing
    """
    for row_index in range(len(a)):
        for column_index in range(len(a[0])):
            if(row_index == column_index and a[row_index][column_index] != 1):
                multiplier = 1.0/a[row_index][column_index]
                a[row_index] = multiply(multiplier,a[row_index])
                identity[row_index] = multiply(multiplier,identity[row_index])
    return [a,identity]
    

def lowerT(a,identity): #returns [a,identity] updated
    """Plan:
        1xx0    1xx0    1x00    1x00    1x00    1000
        01xx  > 01x0  > 01x0  > 01x0  > 0100  > 0100
        001x    001x    001x    0010    0010    0010
        0001    0001    0001    0001    0001    0001

        if it's not 0:
            row := row - (current/below) * (below_row)
            Issue: 'below' could be 0

    """
    for columns in range(len(a)-1,0,-1):
        for rows in range(0,columns,1):
            if(a[rows][columns] != 0 and (rows != columns)):
                multiplier = (-1.0 * a[rows][columns])/a[rows+1][columns]
                a[rows] = add(multiply(multiplier,a[rows+1]) , a[rows])
                identity[rows] = add(multiply(multiplier,identity[rows+1]) , identity[rows])
    return [a,identity]


def checkInverseMatrix(A_inverse,A): #checks if A-1 x A = I
    """ A_inverse = identity, A = temp
        1. Create identity matrix
        2. Multiply a_inverse by A
        3. Check if the result is identity
    """
    printMatrix(A_inverse)
    printMatrix(A)
    #1
    identity = []
    for x in range(len(A_inverse)):
        row = []
        for y in range(len(A_inverse)):
            if(x == y):
                row.append(1)
            else:
                row.append(0)
        identity.append(row)
                
    #2
    A_inverse = matrixMult(A_inverse,A)
    
    #3
    print("A-1 x A becomes:\n")
    printMatrix(A_inverse)
    if(A_inverse == identity):
        print("\n Inverted successfully")
    else:
        print("Error: Inverted wrongly")

#switches rows so that 0 is in bottom left or top right
def switch(a,identity):
    """Plan:
        For each step, start from the bottom-up
        1. Check if an entire row has 0s, then it's un-invertible
        
        2. Check if an entire row has n-1 0s, position it at the right row, and lock the row
            If there are 2 rows that need to get in the same row, it's un-invertible
        2.1 Check if an entire row has n-2 0s, place it not on diagonal, starting from bottom, lock the row
            If the the row needs to place in a locked row, check above
            If it's on a diagonal, check the row above
            If you get to the top-most row, and it's locked, it's un-invertible
        2.2 Check if an entire row has n-3 0s, lock the row
            If it's on a diagonal, check the row above
            If the row needs to be place in a locked row, check above
            If you get to the top-most row, and it's locked, it's un-invertible
        ...
            
        3. Check the matrix if there's a number below a 0 below the diagonal
            if there is, then it's un-invertible
        4. Check the matrix if there's a number above a 0 above the diagonal
            if there is, then it's un-invertible
        5. Check if there's a 0 in the diagonal
            if there is, you screwed up, since this should not be possible, and it's un-invertible
    """
    lockedRows = []
    
    #1
    for x in a:
        all_zeros = True
        for y in x:
            if(y != 0):
                all_zeros = False
                break
        if(all_zeros):
            exit("Error in switch(): Your matrix has a row full of 0s")
    #2
    for zeros in range(len(a)-1,0,-1): # 4...3...2...1 (zeros)
        for row_index in range(len(a)):  #row1...row2...row3...row4
            row_zeros = 0
            
            #Set row_zeros
            for element_index in range(row_index):
                if(a[row_index][element_index] == 0):
                    row_zeros += 1
            
            #Swap rows if needed
            if(row_zeros == zeros):
                #try to put it in the bottom-most row, if not, go up, if at the top, un-invertible
                for row_to_check_index in range(len(a),-2,-1):
                    print(row_index,row_to_check_index)
                    if(row_to_check_index == -1):
                        exit("The way 0s are positioned in row "+str(row_index)+" make it un-invertible")
                    elif(a[row_index][row_to_check_index] != 0 and (row_to_check_index not in lockedRows)):
                        temp = a[row_to_check_index]
                        a[row_to_check_index] = a[row_index]
                        a[row_index] = temp
                        lockedRows.append(row_to_check_index)
                        break
    
    for row_index in range(len(a)):
        for column_index in range(len(a[0])):
            #3. if above diag, check if element above 0 is 0 or non-existent, if not, then exit()
            if (row_index < column_index):
                if((not row_index - 1 < 0)):
                    if(a[row_index][column_index] == 0 and a[row_index-1][column_index] != 0):
                        printAugmentedMatrix(a,identity)
                        exit("Error in switch(): There's a 1-9 above 0 aboved diagonal in row "+str(row_index))
            
            #4. if below diag, check if element below 0 is 0 or non-existent, if not then exit()
            elif(row_index > column_index):
                if(not row_index + 1 > len(a) - 1):
                    if(a[row_index][column_index] == 0 and a[row_index+1][column_index] != 0):
                        printAugmentedMatrix(a,identity)
                        exit("Error in switch(): There's a 1-9 below 0 below diagonal in row "+str(row_index))
            
            #5. if diag, check if there's 0, if there is then exit()
            elif(row_index == column_index):
                if(a[row_index][column_index] == 0):
                    printAugmentedMatrix(a,identity)
                    exit("Error in switch(): There's a 0 in a diagonal in row "+ str(row_index))
            else:
                exit("Error in switch(): This statement is impossible to occur.")
    
    #6
    return[a,identity]
    

def inverse(a):
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
        5. Check A-1 x I = A
    """
    #1. Switch rows
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
    
    #Step 5: Check A-1 x I = A
    checkInverseMatrix(identity,temp)
    return identity


def main():
    if(not input("Do you want to input a matrix with our guide? (Type \'yes\') :: ").lower() in ("yes","y")):
        print("\nFine then, call the inverse() function yourself.")
    else :
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
                        row.append(int(input("Enter row "+str(x)+" column "+str(y)+" :: ")))
                        correctInput = False
                    except ValueError:
                        print("You did not enter a number, try again!")
            matrix.append(row)
        inverse(matrix)

if __name__ == "__main__":
    main()
