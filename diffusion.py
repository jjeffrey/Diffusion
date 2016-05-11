import math
import numpy as np
from scipy import integrate
from scipy.special import erfc
import matplotlib.pyplot as plt

R = 8.3144598

def main():
    a_t = np.arange(0, 25.0, 0.01)
    asol = integrate.odeint(solvr, [1, 0], a_t)
    print(asol)
    plt.plot(asol, a_t)

def solvr(Y, t):
    return [Y[1], -2 * Y[0]-Y[1]]

#Units: Q: J mol^-1
#		R: J mol^-1 K^-1
#		T: K
def D(D0, Q, T):
	return D0 * math.exp(-Q / (R * T))


class DiffusionSystem(object):
	def __init__(self, D0, Q, C0, C1):
		self.D0 = D0
		self.Q = Q
		self.C0 = C0
		self.C1 = C1

	def concentrationAtTime(self, time, temperature=298):
		D_actual = D(self.D0, self.Q, temperature)
		return lambda x: ((self.C0 - self.C1) / 2) * erfc(x/(2 * math.sqrt(D_actual * time)))
	def concentrationAtPoint(self, x, temperature=298):
		D_actual = D(self.D0, self.Q, temperature)
		return lambda time: ((self.C0 - self.C1) / 2) * erfc(x/(2 * math.sqrt(D_actual * time)))
#if __name__ == "__main__":
#	x2 = lambda x: x**2
#	print(integrate.quad(x2, 0, 4))

if __name__ == '__main__':
    #main()
    ds = DiffusionSystem(0.006, 329, 1.0, 0.0)
    concs = ds.concentrationAtTime(100, 1000)

    t = np.arange(-5.0, 5.0, 0.001)
    vconcs = np.vectorize(concs, otypes=[np.float])
    results = vconcs(t)
    inverse = np.vectorize(lambda x: 1 - x)(results)
    print(results);
    plt.plot(t, results)
    plt.plot(t, inverse)
    plt.show()
