import numpy as np
from scipy import integrate
import math

def func1(x):
    return (1+math.sin(math.exp(3*x)))

def simpson(a, b, func):
    h=(b-a)/2
    m = (a+b)/2
    fa = func(a)
    fm = func(m)
    fb = func(b)
    return (fa+4*fm+fb)*h/3

def area(a, b, func, TOL):
    #calculate S1 and S2 using Simpson 1/3:
    m = (a+b)/2
    S1 = simpson(a, b, func)
    S2 = simpson(a, m, func) + simpson(m, b, func)

    if (abs(S1-S2)/15 < TOL):
        return S2 + (S2-S1)/15
    else:
        return area(a, m, func, TOL/2) + area(m, b, func, TOL/2)


def main():
    print(area(0, 1, func1, 0.000005))
    1.2020414911399042

main()
