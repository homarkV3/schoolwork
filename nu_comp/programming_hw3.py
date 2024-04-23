
import math

def reduceArg(x):
    x = x % (2 * math.pi)
    if x > math.pi:
        x = x - 2 * math.pi
    if x < -math.pi:
        x = x + 2 * math.pi
    if x > math.pi / 2:
        x = math.pi - x
    if x < -math.pi / 2:
        x = -math.pi - x
    return x


def mySine(x):

    if x > 10**9:
        return float('nan')
    elif x < -10**9:
        return float('nan')
    elif x > math.pi/2:
        return mySine(reduceArg(x))
    elif x < -math.pi/2:
        return mySine(reduceArg(x))
    elif x < 0:
        return -mySine(-x)
    elif x < 1e-8:
        return x
    else:
        result = 0
        term = x
        n = 1
        while term != 0:
            result += term
            term *= -x**2 / ((2*n+1)*(2*n))
            n += 1

        return float(result)
    
def main():
    print(mySine(1.0e-08)) #1e-08 
    print(mySine(0.00001)) #9.999999999833334e-06 
    print(mySine(0)) #0 
    print(mySine(math.pi/2)) #1.0000000000000002 
    print(mySine(math.pi)) #-0.0 
    print(mySine(100)) #-0.5063656411097555 
    print(mySine(-1000)) #-0.8268795405320125 
    print(mySine(999999999)) #-0.4101372630100049 
    print(mySine(-1000000001)) #nan 

if __name__ == "__main__":
    main()