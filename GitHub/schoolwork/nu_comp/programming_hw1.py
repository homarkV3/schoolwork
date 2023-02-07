import sys
import math
base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig

def ulps(x , y):
    if x == math.inf or y == math.inf or x == 0 or y == 0:
        return math.inf

    if (x > 0 and y < 0) or (x < 0 and y > 0):
        return math.inf
    if x < 0 and y < 0:
        x = abs(x)
        y = abs(y)
    if x > y:
        temp = y
        y = x
        x = temp
    # while (1 < x):
    #     lub *= base
    #     xexp += 1
    # while (1 < y):
    #     lub *= base
    #     yexp += 1
    counter = 0
    while x < y:
        counter += 1
        x += eps
    return counter
    # elif x > 1: 
    #     while(x >= 1):

    # return int((base**(xexp+1)-x)/eps*(base**xexp))

def main():
    print(ulps(-1.0, -1.0000000000000003))  #1 
    print(ulps(1.0, 1.0000000000000003))    #1 
    print(ulps(1.0, 1.0000000000000004))    #2 
    print(ulps(1.0, 1.0000000000000005))    #2 
    print(ulps(1.0, 1.0000000000000006))    #3 
    print(ulps(0.9999999999999999, 1.0))    #1 
    # print(ulps(0.4999999999999995, 2.0))    #9007199254741001 
    # print(ulps(0.5000000000000005, 2.0))    #9007199254740987 
    # print(ulps(0.5, 2.0))                   #9007199254740992 
    # print(ulps(1.0, 2.0))                   #4503599627370496 
    # print(2.0**52)                          #4503599627370496.0 
    print(ulps(-1.0, 1.0))                  #inf 
    print(ulps(-1.0, 0.0))                  #inf 
    print(ulps(0.0, 1.0))                   #inf 
    print(ulps(5.0, math.inf))              #inf 
    print(ulps(15.0, 100.0))                #12103423998558208 

if __name__ == "__main__":
    main()