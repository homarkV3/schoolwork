import math
import sys
import numpy as np

ite = 0

def bisec(func, xl, xu, ite):
    es = sys.float_info.epsilon
    if func(xl)*func(xu)>0: 
        return 'initial estimates do not bracket solution' 
    xmold = xl 
    while abs(func(xmold)) >= es : 
        xm = (xl+xu)/2 
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm 
        xmold = xm 
        
    return xm,func(xm), ite

# regular falsi
def RF(xl,xu,func, ite): 
    if func(xl) == 0:
        c = xl 
        return xl, flag, ite
    if func(xu) == 0:
        c = xu 
        return xu, flag, ite
    if func(xl)*func(xu)>0: 
        flag = -1
        return flag
    c = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
    return c

def SC(xl, xu, func):
    global ite
    ite = 0
    cl = RF(xl, xu, func, ite)
    if cl == -1:
        return -1
    c = cl
    if c <= xl or c >= xu:
        return bisec(func, xl, xu, ite)
    if np.sign(func(xl)) == np.sign(func(c)):
        d = xl - (c-xl)*func(xl)/( func(c) - func(xl))
        if d <= xl or abs(d-c) > abs(xu-xl)/2:
            return bisec(func, xl, xu, ite)
        while abs(func(d)) > math.ulp(d):
            d = xl - func(xl)*((c-xl)/( func(c) - func(xl)))
            xl = c
            c = d
            
        return d, ite
    elif np.sign(func(xu)) == np.sign(func(xu)):
        d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
        if d >= xl or abs(d-c) > abs(xu-xl)/2:
            return bisec(func, xl, xu, ite)
        while abs(func(d)) > math.ulp(d):
            d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
            xu = c
            c = d
            
        return d, ite
    else:
        return bisec(func, xl, xu, ite)

def SCop(xl, xu, func):
    global ite
    ite = 0
    tol = sys.float_info.epsilon
    cl = RF(xl, xu, func, ite)
    if cl == -1:
        return -1
    c = cl
    if (c <= xl):
        c = xl + tol*abs(xl)
    elif (c >= xu):
        c = xu - tol*abs(xu)
    if (c == xl or c == xu):
        return
    if np.sign(func(xl)) == np.sign(func(c)):
        d = xl - (c-xl)*func(xl)/( func(c) - func(xl))
        if d <= xl or abs(d-c) > abs(xu-xl)/2:
            return bisec(func, xl, xu, ite)
        while abs(func(d)) > math.ulp(d):
            d = xl - func(xl)*((c-xl)/( func(c) - func(xl)))
            xl = c
            c = d
            
        return d, ite
    elif np.sign(func(xu)) == np.sign(func(xu)):
        d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
        if d >= xl or abs(d-c) > abs(xu-xl)/2:
            return bisec(func, xl, xu, ite)
        while abs(func(d)) > math.ulp(d):
            d = xu - (c-xu)*func(xu)/( func(c) - func(xu) ) 
            xu = c
            c = d
            
        return d, ite
    else:
        return bisec(func, xl, xu, ite)

def f1(x):
    global ite
    ite += 1
    return x*math.cos(x)+math.sin(x)
def f2(x):
    global ite
    ite += 1
    return (math.e**(-x))-x
def main():
    print(SC(2,3,f1))
    print(SC(4,5,f1))
    print(SCop(2,3,f1))
    print(SCop(4,5,f1))
    print(SC(0,1,f2))
    print(SCop(0,1,f2))


if __name__ == "__main__":
    main()