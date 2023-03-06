import math
import sys
import numpy as np

ite = 0

def bisec(xl, xu, func):
    global ite
    ite = 0
    if func(xl)*func(xu)>0: 
        return 'initial estimates do not bracket solution' 
    d = 1
    while abs(func(d)) > math.ulp(d): 
        while abs(func(d)) > math.ulp(d): 
            c = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
            if c <= xl or c >= xu:
                break
            if np.sign(func(xl)) == np.sign(func(c)):
                d = xl - (c-xl)*func(xl)/( func(c) - func(xl))
                if d <= xl or abs(d-c) > abs(xu-xl)/2:
                    break
                xl = c
                c = d
            elif np.sign(func(xu)) == np.sign(func(xu)):
                d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
                if d >= xl or abs(d-c) > abs(xu-xl)/2:
                    break
                xu = c
                c = d
        xm = (xl+xu)/2 
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm      
    return xm,func(xm), ite

def bisecOp(xl, xu, func):
    global ite
    ite = 0
    es = sys.float_info.epsilon
    if func(xl)*func(xu)>0: 
        return 'initial estimates do not bracket solution' 
    xmold = xl 
    d = 1
    while abs(func(d)) > math.ulp(d): 
        while abs(func(d)) > math.ulp(d): 
            c = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
            if (c <= xl):
                c = xl + es*abs(xl)
            elif (c >= xu):
                c = xu - es*abs(xu)
            if (c == xl or c == xu):
                break
            if np.sign(func(xl)) == np.sign(func(c)):
                d = xl - (c-xl)*func(xl)/( func(c) - func(xl))
                if d <= xl or abs(d-c) > abs(xu-xl)/2:
                    break
                d = xl - func(xl)*((c-xl)/( func(c) - func(xl)))
                xl = c
                c = d
            elif np.sign(func(xu)) == np.sign(func(xu)):
                d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
                if d >= xl or abs(d-c) > abs(xu-xl)/2:
                    break
                d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
                xu = c
                c = d
        xm = (xl+xu)/2 
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm         
    return xm,func(xm), ite

def f1(x):
    global ite
    ite += 1
    return x*math.cos(x)+math.sin(x)
def f2(x):
    global ite
    ite += 1
    return (math.e**(-x))-x

def main():
    print(bisec(2,3,f1))
    print(bisec(4,5,f1))
    print(bisecOp(2,3,f1))
    print(bisecOp(4,5,f1))
    print(bisec(0,1,f2))
    print(bisecOp(0,1,f2))


if __name__ == "__main__":
    main()