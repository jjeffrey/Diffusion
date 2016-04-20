import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def main():
    a_t = np.arange(0, 25.0, 0.01)
    asol = integrate.odeint(solvr, [1, 0], a_t)
    print(asol)
    plt.plot(asol, a_t)

def solvr(Y, t):
    return [Y[1], -2 * Y[0]-Y[1]]

if __name__ == "__main__":
	x2 = lambda x: x**2
	print integrate.quad(x2, 0, 4)

if __name__ == '__main__':
    main()
