# Inverts a square matrix

1. Run the program
2. Pass a square-matrix into inverse(a[][])


inverse( [ [ a , b ] , [ c , d ] ] )

| a b |<br/>
| c d |

inverse( [ [ a , b , c ] , [ d , e , f ] , [ g , h , i ] ] )

| a b c |<br/>
| d e f |<br/>
| g h i |


It won't work if it doesn't pass the preconditions:

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
