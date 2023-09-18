# import numpy as np

# method_a = np.array([18.0, 18.0, 19.0, 20.0, 21.0, 22.0, 22.5, 23.3, 24.0, 24.0, 24.5, 25.0, 25.0, 25.4, 26.2, 26.4])
# method_b = np.array([18.6, 18.9, 19.2, 19.6, 20.1, 20.3, 20.4, 20.4, 20.5, 20.6, 21.2, 22.0, 22.0, 22.3, 22.5, 23.6])

# a = np.mean(method_a)
# b = np.mean(method_b)

# m_a = np.median(method_a)
# m_b = np.median(method_b)

# q1_a = np.percentile(method_a, 25)
# q3_a = np.percentile(method_a, 75)
# q1_b = np.percentile(method_b, 25)
# q3_b = np.percentile(method_b, 75)

# std_a = np.std(method_a, ddof=1)
# std_b = np.std(method_b, ddof=1)

# print("Mean A:", a)
# print("Mean B:", b)
# print("Median A:", m_a)
# print("Median B:", m_b)
# print("First Quartile A:", q1_a)
# print("Third Quartile A:", q3_a)
# print("First Quartile B:", q1_b)
# print("Third Quartile B:", q3_b)
# print("Standard Deviation A:", std_a)
# print("Standard Deviation B:", std_b)
import numpy as np
import matplotlib.pyplot as plt

data = [2099, 528, 2030, 1350, 1018, 384, 1499, 1265, 375, 424, 789, 810, 522, 513, 488, 200, 215, 486, 257, 557, 260, 461, 500]
# Boxplot
plt.boxplot(data)
plt.show()

# Identifying outliers
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower_bound or x > upper_bound]
print("Outliers:", outliers)

# Histogram
plt.hist(data, bins='sqrt')
plt.show()

# Normalized histogram
plt.hist(data, bins='sqrt', density=True)
plt.show()