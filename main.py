"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
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

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def add_vec(a_vec, b_vec):
    a=binary2int(a_vec).decimal_val
    b=binary2int(b_vec).decimal_val
    return BinaryNumber(a + b).binary_vec

def sub_vec(a_vec, b_vec):
    a =binary2int(a_vec).decimal_val
    b = binary2int(b_vec).decimal_val
    return BinaryNumber(a - b).binary_vec
    
def quadratic_multiply(x, y):
    if x.decimal_val == 0 or y.decimal_val== 0:
        return ['0']
    if x.decimal_val< 2 and y.decimal_val < 2:  
        if (x.decimal_val== 1 and y.decimal_val == 1): 
            return ['1'] 
        else: 
            return ['0']
    
    vx, vy = pad(x.binary_vec, y.binary_vec)
    n = len(vx)

    if n == 1:
        if vx[0]== '1' and vy[0] =='1':
            return ['1']
        else:
            return ['0']
        


    xl, xr = split_number(vx) 
    yl, yr = split_number(vy)
    P1 = quadratic_multiply(xl, yl)
    P2 = quadratic_multiply(xr, yr)
    P3 = quadratic_multiply(xl, yr)
    P4 = quadratic_multiply(xr, yl)
    term1 = bit_shift(binary2int(P1),n).binary_vec
    cross = add_vec(P3, P4)
    term2 = bit_shift(binary2int(cross), n //2).binary_vec
    s = add_vec(term1, term2)
    s = add_vec(s, P2)
    return s


def subquadratic_multiply(x, y):
    if x.decimal_val == 0 or y.decimal_val== 0:
        return ['0']
    if x.decimal_val<2 and y.decimal_val < 2:  
        if (x.decimal_val== 1 and y.decimal_val == 1): 
            return ['1'] 
        else: 
            return ['0']
    vx, vy = pad(x.binary_vec, y.binary_vec)
    n = len(vx)
    if n == 1:
        if vx[0]== '1' and vy[0] =='1':
            return ['1']
        else:
            return ['0']
    xl, xr = split_number(vx)
    yl, yr = split_number(vy)
    P1 = subquadratic_multiply(xl, yl)
    P2 = subquadratic_multiply(xr, yr)
    sum_x = add_vec(xl.binary_vec, xr.binary_vec)
    sum_y = add_vec(yl.binary_vec, yr.binary_vec)
    P3 = subquadratic_multiply(binary2int(sum_x), binary2int(sum_y))
    mid = sub_vec(P3, P1)
    mid = sub_vec(mid, P2)
    term1 = bit_shift(binary2int(P1), n).binary_vec  
    term2 = bit_shift(binary2int(mid), n//2).binary_vec
    s = add_vec(term1, term2)
    s = add_vec(s, P2)
    return s


## Feel free to add your own tests here.
def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))).decimal_val == 2*2

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    

