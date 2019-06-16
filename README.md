# Inverts a square matrix

Run the program and follow its directions<br/>

If you're too dumb to not know how to run a python script, just copy everything from invertMatrix.py and paste it here: https://www.onlinegdb.com/online_python_compiler

[ [ a , b ] , [ c , d ] ]

        | a b |
        | c d |

[ [ a , b , c ] , [ d , e , f ] , [ g , h , i ] ]

        | a b c |
        | d e f |
        | g h i |


Not all matricies can be inverted cause my code sux or you have too many zeros<br/>
It uses the dumb Gauss-Jordan methods of switching rows, adding rows, and multiplying rows<br/>
This is how my algorithm works for a 4x4 matrix, where x is a random number:

        
        1. UpperT():
        x x x x     x x x x     x x x x     x x x x     x x x x     x x x x
        x x x x --> x x x x --> 0 x x x --> 0 x x x --> 0 x x x --> 0 x x x
        x x x x     0 x x x     0 x x x     0 x x x     0 0 x x     0 0 x x 
        0 x x x     0 x x x     0 x x x     0 0 x x     0 0 x x     0 0 0 x
        
        2. Diag():
        1 x x x     1 x x x     1 x x x     1 x x x 
        0 x x x --> 0 1 x x --> 0 1 x x --> 0 1 x x
        0 0 x x     0 0 x x     0 0 1 x     0 0 1 x
        0 0 0 x     0 0 0 x     0 0 0 x     0 0 0 1
        
        3. LowerT():
        1xx0    1xx0    1xx0    1x00    1x00    1000
        01xx  > 01x0  > 01x0  > 01x0  > 0100  > 0100
        001x    001x    0010    0010    0010    0010
        0001    0001    0001    0001    0001    0001
