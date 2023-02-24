import sys
import math
import struct
import numpy as np

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1

def exponent(x):
    neg = 0 
    packed = struct.pack('d', x)
    unpacked = struct.unpack('Q',packed)
    binary = bin(unpacked[0])
    exponent = binary[2:]
    if len(binary) == 65:
        exponent = exponent[:11]
    elif len(binary) == 66:
        exponent = exponent[1:12]
        neg += 1
    exponent = int(exponent, 2)
    exponent = exponent - 1023
    if exponent == 1024:
        if neg == 1:
            return -exponent
        return exponent
    if exponent == -1023:
        return 0
    return exponent

def fraction(x):
    expo = exponent(x)
    if expo == 0:
        return x
    packed = struct.pack('d', x)
    unpacked = struct.unpack('Q',packed)
    binary = bin(unpacked[0])
    fraction = binary[13:]
    fraction = "0b"+fraction
    test = int(fraction, 2)
    fraction = int(fraction, 2)/(2**52)
    return fraction

def mantissa(x):
    subtest = exponent(x)
    frac = fraction(x)
    if subtest == 0:
        return x
    if subtest != -1022:
        frac += 1
    return frac

def is_posinfinity(x):
    if exponent(x) == 1024:
        return True
    else:
        return False

def is_neginfinity(x):
    if exponent(x) == -1024:
        return True
    else:
        return False

def ulp(x):
    base = -52
    neg = 0 
    packed = struct.pack('d', x)
    unpacked = struct.unpack('Q',packed)
    binary = bin(unpacked[0])
    expo = binary[2:]
    if len(binary) == 65:
        expo = expo[:11]
        expo = int("0b"+expo, 2)
    elif len(binary) == 66:
        expo = expo[1:12]
        neg += 1
        expo = int("0b"+expo, 2)
    elif len(binary) == 64:
        expo = "0"+expo[:10]
        expo = int("0b"+expo, 2)
    elif expo == "0" or "1":
        expo = -1023
    remainder = expo - 1023
    base = base + remainder
    if 2**base ==0:
        return np.nextafter(0,1)
    return 2**base
    
def ulps(x,y):
    pass

def main():
    # print(exponent(math.inf))
    y = 6.5
    subMin = np.nextafter(0,1) #subMin = 5e-324
    # print(sign(y)) #1
    # print(sign(0.0)) # 0
    # print(sign(-y)) # -1
    # print(sign(-0.0)) #0
    # print(exponent(y)) # 2
    # print(exponent(16.6)) # 4
    # print(fraction(0.0)) #0.0
    # print(mantissa(y)) #1.625
    # print(mantissa(0.0)) #0.0
    var1 = float("nan")
    # print(exponent(var1)) # 1024
    # print(exponent(0.0)) # 0
    # print(exponent(subMin)) # -1022
    # print(is_posinfinity(math.inf)) # True
    # print(is_neginfinity(math.inf)) # False
    # print(not is_posinfinity(-math.inf)) #True
    # print(is_neginfinity(-math.inf)) #True
    # print(ulp(y)) # 8.881784197001252e-16
    # print(ulp(1.0)) # 2.220446049250313e-16
    # print(ulp(0.0)) # 5e-324
    print(ulp(subMin)) # 5e-324
    print(ulp(1.0e15)) # 0.125
    # print(ulps(1,2)) # 4503599627370496
    pass


if __name__ == "__main__":
    main()