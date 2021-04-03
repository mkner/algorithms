#
# mk
# v0.02
# 
# Karatsuba Multiplication Algorithm
#
# short and clean python implementation of Karatsuba's Fast Multiplication Algorithm
# based on Stanford Algorithms Course CS161 - Roughgarden
# includes example - multiply 64 digit representations of pi and e
#

def padzeros(numstring, nzeros, left = True):
    #return string representation of numeric value
    # padded with zero on left or right by appending
    
    for i in range(nzeros):
        if left:
            numstring = '0' + numstring
        else:
            numstring = numstring + '0'
    return numstring


def ksm(x,y, trace = False):
    
# convert to string
# if args not int specfic
    
    if (type(x) != str):
        x = str(x)
        
    if (type(y) != str):
        y = str(y)

# base case for recursion
        
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    
# if different lengths pad them with zeros so same length
        
    if len(x) < len(y):
        x = padzeros(x, len(y) - len(x))
    elif len(y) < len(x):
        y = padzeros(y, len(x) - len(y))

    n = len(x)
    
    j = n//2
    
#adjust offset for odd digit integers
    if (n % 2) != 0:
        j += 1    
    numzeropadB = n - j
    numzeropadA = numzeropadB * 2
    
# divide into quarter pieces
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])

#recursively calculate
    ac = ksm(a, c)
    bd = ksm(b, d)
    abcd = ksm(a + b, c + d)
    if (trace==True):
        print(ac,bd,abcd)
        
    A = int(padzeros(str(ac), numzeropadA, False))
    B = int(padzeros(str(abcd - ac - bd), numzeropadB, False))
    
    if (trace==True):
        print(A,B,bd) 
 
# returns whatever type bd is
        
    return A + B + bd

# test
    
    ksm(2,12)

pi="3141592653589793238462643383279502884197169399375105820974944592"
e="2718281828459045235360287471352662497757247093699959574966967627"

# z = ksm(x,y) 

z = ksm(pi,e)
sz = str(z)
len(sz)

# result
# len is 127 which is btw 2^7 - 1
result="8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184"
