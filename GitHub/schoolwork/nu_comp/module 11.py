# import numpy as np
# x=np.array([0, 1.8, 5, 6, 8.2, 9.2])
# y=np.array([2.6, 16.415, 5.375, 3.5, 2.015, 2.54])
# pFit = np.polyfit(x,y,5)
# print(pFit)

import numpy as np
from scipy.interpolate import CubicSpline
import pylab

x = np.array([1,2,2.5,3,4,5])
y = np.array([1,5,7,8,2,1])

cs=CubicSpline(x,y)
# nota=CubicSpline(x,y)

xx = np.linspace(1,5,50)
yr = cs(xx)


pylab.scatter(x,y,c='r',marker='s')
pylab.plot(xx,yr,c='k')
pylab.grid()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('Cubic Spline - Not-a-knot')
pylab.show()
