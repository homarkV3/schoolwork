import math

def main():
    a = 3.000
    x = 2
    i = 0
    while abs(x**3 - a) > 1e-12:
        y = x - (((x**3)-3)/(3*(x**2)))
        print(y)
        i += 1
        x = y

if __name__ == "__main__":
    main()