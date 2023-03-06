"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):

    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return x.decimal_val * y.decimal_val

    x.binary_vec, y.binary_vec = pad(x.binary_vec,y.binary_vec)

    n = len(x.binary_vec)

    xl, xr = split_number(x.binary_vec)
    yl, yr = split_number(y.binary_vec)
    
    xlyl = BinaryNumber(subquadratic_multiply(xl,yl))
    xryr = BinaryNumber(subquadratic_multiply(xr,yr))
    
    m = bit_shift(BinaryNumber(subquadratic_multiply(BinaryNumber(xl.decimal_val + xr.decimal_val), BinaryNumber(yl.decimal_val + yr.decimal_val)) ), n//2).decimal_val
    l = bit_shift(xlyl ,n).decimal_val - bit_shift(xlyl ,n//2).decimal_val
    r = xryr.decimal_val - bit_shift(xryr ,n//2).decimal_val
    
    return l + m + r

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert subquadratic_multiply(BinaryNumber(15), BinaryNumber(5)) == 15*5
    assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 20*20

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
