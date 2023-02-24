import math
import sys
def main(xl,xu,func): 
    flag = 0 
    ite = 0 
    if func(xl) == 0:
        root = xl 
        return xl, flag, ite
    if func(xu) == 0:
        root = xl 
        return xl, flag, ite
    if func(xl)*func(xu)>0: 
        flag = -1
        return flag
    root = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
    while abs(root) > sys.float_info.epsilon: 
        valv = func(root)
        if ite >= 100000:
            return root, flag, valv, ite
        ite += 1
        if func(root)*func(xl)>0: 
            if math.ulp(root) > (root - xl):
                return root, flag, valv, ite 
            xl = root 
        else: 
            if math.ulp(root) > (xu - root):
                return root, flag, valv, ite 
            xu = root 
        root = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
    return root, flag, valv, ite

def f1(x):
    return x**4-6*x**3+12*x**2-10*x+3

def f2(x):
    return x**3-7*x**2+15*x-9

if __name__ == "__main__":
    print(main(1.5, 2.5, f1))
    print(main(1.5, 2.5, f2))
    print(main(0, 1.5, f1))
    print(main(0, 1.5, f2))