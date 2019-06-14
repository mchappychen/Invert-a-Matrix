# Inverts a square matrix

Run the program and follow its directions<br/>
Or pass a square-matrix into inverse(a[][])


inverse( [ [ a , b ] , [ c , d ] ] )

        | a b |
        | c d |

inverse( [ [ a , b , c ] , [ d , e , f ] , [ g , h , i ] ] )

        | a b c |
        | d e f |
        | g h i |


Not all matricies can be inverted.<br/>
It uses the Gauss-Jordan methods<br/>
This is how my algorithm works for a 4x4 matrix, where x is a random number:

        
        1. UpperT():
        xxxx    xxxx    xxxx    xxxx    xxxx    xxxx
        xxxx  > xxxx  > 0xxx  > 0xxx  > 0xxx  > 0xxx
        xxxx    0xxx    0xxx    0xxx    00xx    00xx
        0xxx    0xxx    0xxx    00xx    00xx    000x
        
        2. Diag():
        1xxx    1xxx    1xxx    1xxx
        0xxx  > 01xx  > 01xx  > 01xx
        00xx    00xx    001x    001x
        000x    000x    000x    0001
        
        3. LowerT():
        1xx0    1xx0    1xx0    1x00    1x00    1000
        01xx  > 01x0  > 01x0  > 01x0  > 0100  > 0100
        001x    001x    0010    0010    0010    0010
        0001    0001    0001    0001    0001    0001
