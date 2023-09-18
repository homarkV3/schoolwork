# import matplotlib.pyplot as plt

# # Given data
# X = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

# # Histogram
# plt.hist(X, bins=[0, 1, 2], align='left', rwidth=0.5)
# plt.xlabel('X')
# plt.ylabel('Count')
# plt.title('Histogram of Data')
# plt.xticks([0, 1])
# plt.show()

# # Normalized Histogram
# plt.hist(X, bins=[0, 1, 2], align='left', rwidth=0.5, density=True)
# plt.xlabel('X')
# plt.ylabel('Probability')
# plt.title('Normalized Histogram of Data')
# plt.xticks([0, 1])
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data
X = [0, 0, 0.1, 0.5, 0.9, 0.2, 0.1]

# Calculate sample mean and sample variance
n = len(X)
mean = np.mean(X)
variance = np.var(X, ddof=1)

# Gaussian distribution parameters
mu = mean
sigma = np.sqrt(variance)

# Create x values for the plot
x = np.linspace(min(X) - 0.5, max(X) + 0.5, 1000)

# Calculate the Gaussian distribution values for each x
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.plot(x, y, label=f'N({mu:.4f}, {sigma**2:.4f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gaussian Distribution')
plt.legend()

# Plot the data points

plt.legend()
plt.show()