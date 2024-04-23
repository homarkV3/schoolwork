import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
# def predict_temperature(day, coefficients):
#     a, b, c, d = coefficients
#     return a * day**3 + b * day**2 + c * day + d
def main():
    # temp = []
    # with open("avetemp.csv","r") as data:
    #     for line in data:
    #         temp.append(float(line.split("\n")[0]))
    # day = 244
    # days = np.arange(len(temp))
    # coef = np.polyfit(days, temp, 3)
    # predicted_temp = predict_temperature(day, coef)

    # print(predicted_temp)

    # mean_population = np.mean(temp)

    # # Replace the following random samples with your actual SRS and sample of convenience data
    # srs_sample = np.random.choice(temp, 30)
    # mean_srs = np.mean(srs_sample)

    # sample_convenience = temp[:30]
    # mean_sample_convenience = np.mean(sample_convenience)
                
    # fig, ax = plt.subplots()

    # # Create a line plot with the raw data
    # ax.plot(range(len(temp)), temp, label='Raw Data')

    # # Add lines to show the means
    # ax.axhline(mean_population, color='red', linestyle='--', label='Population Mean')
    # ax.axhline(mean_srs, color='blue', linestyle='--', label='SRS Mean')
    # ax.axhline(mean_sample_convenience, color='black', linestyle='--', label='Convenience Sample Mean')
    # ax.set_title("Jan2022-Dec2022")
    # ax.set_xlabel("Days")
    # ax.set_ylabel("temp")
    # # Add a legend
    # ax.legend()

    # # Display the plot
    # plt.show()

    # Input data
    x = np.array([0.43, 0.67, 0.40, 0.45, 0.80])
    y = np.array([772, 735, 774, 769, 723])

    # Create the matrix A and the vector Y
    an = np.vstack([x, np.ones(len(x))]).T
    yn = y.reshape(-1, 1)

    # Compute the matrix multiplication A^T * A and A^T * Y
    AtA = np.dot(an.T, an)
    AtY = np.dot(an.T, yn)

    # Compute the inverse of AtA
    AtA_inv = np.linalg.inv(AtA)

    # Compute the coefficients by multiplying AtA_inv with AtY
    coefficients = np.dot(AtA_inv, AtY)
    print("a:", coefficients[0])
    print("b:", coefficients[1])


if __name__ == "__main__":
    main()


