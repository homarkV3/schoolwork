import numpy as np
A=np.matrix('15, -3, -1;-3, 18, -6;-4,-1,12')
AInv = np.linalg.inv(A)
print(AInv)