'''
Caso practico de aplicacion de Runge-Kutta de O(h)=4 para un sistema de ecuaciones
	Oscilador Amortiguado:
	Para una masa en un resorte con un amortiguador se tiene la siguiente ecuacion
	utilizando las leyes de Newton
	x(t) 			v(t)=[dx/dt](t)
	m[d^2x/dt^2] + c[dx/dt] + kx = 0		
	-> ma+cv+kx = 0 (masa*aceleracion + fuerza de amortiguamiento + ley de Hooke)
	x(0)=xinc		v(0)=vinc
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Datos
m = 1. 			# Masa
c = 0.1			# Constante de Amortiguamiento
k = 1. 			# Constante del resorte


# Condicion Inicial
t = 0.			# Tiempo	
xinc = 2.		# Posicion Inicial
vinc = 0.		# Velocidad Inicial
u = np.array([xinc, vinc])		# Cambio de variable, o variable a resolver

'''
Despeje de la derivada: 
	x(t)=| x(t)		  |
		 | [dx/dt](t) |

	u(t)=| u0 | = | x(t) |
		 | u1 | = | v(t) |

	[d^2x/dt^2] = -[c/m][dx/dt] - [k/m]x
	f(x,t) = -[c/m][dx/dt] - [k/m]x
	[du/dt] = F(u,t) = |		 u1		   |
					   | -[c/m]u1 -[k/m]u0 |
	u(0)=| xinc |
	     | vinc |
'''


# Campo de direcciones
def F(u, t):
	return np.array([
		u[1],						# u[1] = Velocidad
		-c*u[1]/m - k*u[0]/m 		# u[0] = Desplazamiento
		])


# Solucion
tsol = [t]			# Solucion del tiempo
xsol = [u[0]]		# Solucion de la posicion
vsol = [u[1]]		# Solucion de la velocidad
dt = 0.1			# Tiempo a grafica
tfin = 100		# Tiempo Final en sg

while t < tfin:
	k1 = F(u,t)
	k2 = F(u+dt*k1/2, t+dt/2)
	k3 = F(u+dt*k2/2, t+dt/2)
	k4 = F(u+dt*k3, t+dt)
	u = u + (k1 + 2*k2 + 2*k3 + k4)*dt/6
	t = t + dt
	xsol.append(u[0])
	vsol.append(u[1])
	tsol.append(t)


# Graficas comparativas
plt.subplot(311)
plt.plot(tsol, xsol)
plt.title('T * X')
plt.xlabel('Tiempo')
plt.ylabel('Desplazamiento')
plt.grid()

plt.subplot(312)
plt.plot(tsol, vsol)
plt.title('T * V')
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.grid()

plt.subplot(313)
plt.plot(xsol, vsol)
plt.title('X * V')
plt.xlabel('Desplazamiento')
plt.ylabel('Velocidad')
plt.grid()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xsol, vsol, tsol)
ax.set_xlabel('Desplazamiento')
ax.set_ylabel('Velocidad')
ax.set_zlabel('Tiempo')
plt.show()
