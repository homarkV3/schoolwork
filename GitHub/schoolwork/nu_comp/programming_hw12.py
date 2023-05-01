# import numpy as np
# from scipy import integrate
# import math

# def func1(x):
#     return (1+math.sin(math.exp(3*x)))

# def simpson(func, a, b, fa, fb, fab):
#     c = (a + b) / 2
#     fc = func(c)
#     fbc = func((b + c) / 2)
#     return (b - a) / 6 * (fa + 4 * fc + fb), (b - a) / 12 * (fa + 4 * fab + 2 * fc + 4 * fbc + fb), fc

# def area(func, a, b, tol=5.0e-6):
#     fa, fb = func(a), func(b)
#     fab = func((a + b) / 2)
#     area, _, _ = simpson(func, a, b, fa, fb, fab)
#     stack = [(a, b, fa, fb, fab, area)]
#     neval = 0
#     while stack:
#         a, b, fa, fb, fab, A = stack.pop()
#         c = (a + b) / 2
#         fa, fab, fbc = func(a), func((a + b) / 2), func(b)
#         L, R, fc = simpson(func, a, b, fa, fb, fab)
#         AR = L + R
#         if np.isclose(AR, A, atol=tol):
#             area += AR
#             neval += 1
#         else:
#             stack.append((c, b, fbc, fb, fab, R))
#             stack.append((a, c, fa, fbc, fab, L))
#             neval += 1
#     return neval

# def main():
#     f1 = lambda x: np.exp(x ** 2)
#     f2 = lambda x: np.sin(x) / x
#     f3 = lambda x: np.sin(x) / x if x > 0 else 1
#     print("tol = 5e-06")
#     for f, a, b in [(f1, -1, 1), (f2, -1, 10), (f3, 0, 1)]:
#         exact, _ = integrate.quad(f, a, b)
#         neval = area(f, a, b)
#         print(f"(nevals = {neval}) e^x^2 [{a},{b}] = {exact}")
# main()

# import numpy as np
# import math

# def findIntegral(n):
#     x = np.zeros(n)
#     y = np.zeros(n)
#     cnt = -1
#     x1 = np.random.uniform(-1, 1, n)
#     y1 = np.random.uniform(-1, 1, n)
#     while (1):
#         for i in range(n):
#             if x1[i]*x1[i]+y1[i]*y1[i] < 1:
#                 cnt += 1
#                 x[cnt] = x1[i]
#                 y[cnt] = y1[i]
#                 if cnt == (n-1):
#                     break
#         if cnt == (n-1):
#             break
#     x1 = np.random.uniform(-1, 1, n)
#     y1 = np.random.uniform(-1, 1, n)
#     funcSum = 0.
#     for i in range(n):
#         funcSum += math.exp(x[i]*x[i]*y[i]*y[i])
#     integral = funcSum*math.pi/n
#     return integral

# print(findIntegral(1000000))

# import numpy as np
# import math
# def findVol(n):
#     x=np.random.uniform(0,1,n)
#     y=np.random.uniform(0,1,n)
#     z=np.random.uniform(0,1,n)
#     count = 0.
#     for i in range(n):
#         if x[i]*x[i]+math.pow(math.sin(y[i]),2) <= z[i] and x[i]-z[i]+math.exp(y[i])<=1:
#             count +=1
#     xx = (float)(count)/n
#     return (float)(count)/n

# print(findVol(1000000))

import random
import math

N = 1000000
count = 0

for i in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    z = random.uniform(0, 1)

    if x**2 + math.sin(y)**2 <= z and x - z + math.exp(y) <= 1:
        count += 1

V_rec = 1  # volume of the rectangular box enclosing the region
V = (V_rec * count) / N
print("Volume estimate:", V)