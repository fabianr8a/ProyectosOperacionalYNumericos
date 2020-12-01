#Implementación del método RK4 y algunos casos de salida


import numpy as np
import matplotlib.pyplot as plt


def test1(x, y):				# dy/dx = x^2 - 3y
	return x**2 - 3*y


def f(x, y):		#dy/dx = y - x^2 +1
	return y-x**2+10


def RK4(f, a, b, y0, h):
	x = np.arange(a, b+h, h)
	n = len(x)
	y = np.zeros(n)
	y[0] = y0
	for i in range(0, n-1):
		k1 = f(x[i], y[i])
		k2 = f(x[i]+h/2, y[i]+k1*h/2)
		k3 = f(x[i]+h/2, y[i]+k2*h/2)
		k4 = f(x[i]+h, y[i]+k3*h)
		w = y[i+1] = y[i]+(h/6)*(k1+2*k2+2*k3+k4)
	plt.plot(x, y)
	plt.show()


# dy/dx= y - x^2 +1, 	a=0, b=5, y0=1, h=0.01
RK4(f, 0, 5, 1, 0.01)

