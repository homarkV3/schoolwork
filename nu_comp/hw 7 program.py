import numpy as np
import math
import sys

i = 0 

def f(x):
    global i 
    i += 1
    return ((x**2)/10) - (2*math.sin(x))
def golden(f, xl, xu, Ea = sys.float_info.epsilon, maxit = 100):
    phi = (1+np.sqrt(5))/2
    d = (phi - 1)*(xu-xl)
    x1 = xl + d 
    f1 = f(x1)
    x2 = xu - d 
    f2 = f(x2)
    for i in range(maxit):
        xint = xu - xl
        if f1 < f2:
            xopt = x1
            xl = x2
            x2 = x1
            f2 = f1
            x1 = xu - (x2-xl)
            f1 = f(x1)
        else:
            xopt = x2
            xu = x1
            x1 = x2
            f1 = f2
            x2 = xl + (xu-x1)
            f2 = f(x2)
        if xopt != 0:
            ea = (2-phi)*(xu-xl)
            if ea <= Ea: break
    return xopt, f(xopt), ea, i+1

def main():
    pass

if __name__ == "__main__":
    ans = golden(f, 0, 4)
    print(f"{ans[0]} {ans[1]} {ans[2]} {ans[3]}")
    print(i)