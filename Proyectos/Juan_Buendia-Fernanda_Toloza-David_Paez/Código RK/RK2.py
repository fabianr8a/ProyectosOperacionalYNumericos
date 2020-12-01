# Implementación del método Runge-Kutta de orfen 2 y algunos casos de salida

import numpy as np


def RK2(d1y, x0, y0, h, muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano, 2), dtype=float)
    estimado[0] = [x0, y0]
    xi = x0
    yi = y0
    for i in range(1, tamano, 1):
        K1 = h * d1y(xi, yi)
        K2 = h * d1y(xi+h, yi+K1)
        yi = yi + (K1+K2)/2
        xi = xi + h
        estimado[i] = [xi, yi]
    return(estimado)

