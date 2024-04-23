import math
import sys
import numpy as np
import pylab

def main():
    # W=np.array([70, 75, 77, 80, 82, 84, 87, 90])
    # A=np.array([2.1, 2.12, 2.15, 2.2, 2.22, 2.23, 2.26, 2.3])
    # lnW = np.log(W)
    # lnA = np.log(A)
    # lFit = np.polyfit(lnW, lnA, 1)
    # a=math.exp(lFit[1])
    # b=lFit[0]
    # A95 = a*math.pow(95,b)
    # print(a, b, A95)

    # x=np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3])
    # y=np.array([800, 985, 1490, 1950,2850, 3600])
    # lnY = np.log(y)
    # matA=np.vstack((x, np.power(x,0))).transpose()
    # RHS=np.matmul(matA.transpose(),lnY)
    # lFit = np.matmul(np.linalg.inv(np.matmul(matA.transpose(),matA)),RHS)
    # a=math.exp(lFit[1])
    # b=lFit[0]
    # y2 = a*math.exp(b*2)
    # print(a, b, y2)

    x=np.array([3,4,5,7,8,9,11,12])
    y=np.array([1.6,3.6,4.4,3.4,2.2,2.8,3.8,4.6])
    nDeg = 3
    c = np.polyfit(x,y,nDeg)
    print('c=',c)

if __name__ == "__main__":
    main()

