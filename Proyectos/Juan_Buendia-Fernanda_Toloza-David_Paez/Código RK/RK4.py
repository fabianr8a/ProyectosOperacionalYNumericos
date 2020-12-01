#Implementación del método RK4 y algunos casos de salida


from math import *


def test1(t, y):		#dy/dt = y - t^2 +1
	return y-t**2+1


def test2(t, y):		#dy/dt = 2 - e^-4t -2y
	return 2.0-exp(-4*t)-2*y


def RK4(a, b, y0, f, N):
	h = (b-a)/float(N)
	t = a
	w = y0
	print (t, '--->', w)

	for i in range(1, N+1):
		k1 = h*f(t, w)
		k2 = h*f(t+h/2.0, w+k1/2.0)
		k3 = h*f(t+h/2.0, w+k2/2.0)
		k4 = h*f(t+h, w+k3)
		w = w+(k1+2.0*k2+2.0*k3+k4)/6.0
		t = a+i*h
		print (t, '--->', w)


#dy/dt= y - t^2 +1, 	a=0, b=2, y0=0.5, N=10
print ('\n'+r'Método RK4'+'\n')
RK4(0, 2, 0.5, test1, 10)


#dy/dt= 2 - e^-4t -2y, 	a=0, b=1, y0=1, N=20
print ('\n'+r'Método RK4'+'\n')
RK4(0, 1, 1, test2, 20)


