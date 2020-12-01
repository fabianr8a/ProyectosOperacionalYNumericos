'''
Caso practico de aplicacion de Runge-Kutta de O(h)=4
	Usando la ley de enfriamiento de Newton, se puede predecir la temperatura de un cuerpo
	al ser enfriado por convección para sistemas con Bi<0.1 (Número de Biot)
	T(t)		pCpV[dT/dt] = -hA(T-Tinf)		T(0) = Tinc
	Los datos son para una pieza metalica de acero del tamaño de una moneda enfriada con aire
'''

import numpy as np
import matplotlib.pyplot as plt


# Datos
Tinf = 298.		# Temperatura del entorno °K
Cp = 500.		# Capacidad Calorifica especifica [J/kg*°K]
rho = 7800.		# Densidad del objeto [kg/cm^3]
h = 100.		# Coeficiente de tranferencia de energia [W/m^2*°k]
A = 1e-4		# Area Superficial [m^2]
V = 1e-7		# Volumen [m^3]

# Condicion Inicial
t = 0.			# Tiempo	
Tinc = 1000.	# Temperatura Inicial
u = Tinc		# Cambio de variable, o variable a resolver

'''
Despeje de la derivada: 
	u(t)=T(t)
	[du/dt] = -[hA/pCpV](u - Tinf)
	f(u,t) = -[hA/pCpV](u - Tinf)
	u(0) = uinc = T(0) = Tinc

'''


# Campo de direcciones
def f(u, t):
	return -h*A*(u-Tinf)/(rho*Cp*V)


# Solucion
tsol = [t]		# Solucion del tiempo
Tsol = [u]		# Solucion de la Temperatura
dt = 0.001
tfin = 1000		# Tiempo Final en sg

while t < tfin:
	k1 = f(u,t)
	k2 = f(u+dt*k1/2, t+dt/2)
	k3 = f(u+dt*k2/2, t+dt/2)
	k4 = f(u+dt*k3, t+dt)
	u = u + (k1 + 2*k2 + 2*k3 + k4)*dt/6
	t = t + dt
	Tsol.append(u)
	tsol.append(t)


plt.plot(tsol, Tsol)
plt.show()
