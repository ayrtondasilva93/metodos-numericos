# Importamos las librerias que vamos a usar
import numpy
import matplotlib.pyplot as plt

# Momento de Inercia respecto de IYY en [m^4]
Ir = 7.84e-7

# Modulo de Young en [Pa]
E = 2e+11

# Fuerza en [N]
F = -1000

# Longitud  en [m]
l = 1.5

# Momento flector [Nm]
M = F * l

# Distancia al eje neutro [m]
y = 0.04

# Maximó desplazamiento en [mm], por eso se multiplica x1000
Md = (F * l ** 3) / (3 * E * Ir) * 1000

# Maxima tensión en [MPa], por eso multiplica x1e-6
Me = ((M * y) / Ir) * 1e-6

# Creamos un vector equidistante en 100 tramos (definicion por defecto) de [0,l]
x = numpy.linspace(0, l, 100)

# Calculamos el desplazamiento para todos los puntos definidos anteriormente
dis = (F * x ** 2) * (3 * l - x) * (1 / (6 * E * Ir)) * 1000

# imprimo los resultados
print('Maximó desplazamiento',round(Md,2),'mm')
print('Maxima tensión',round(Me,2),'Mpa')

# Graficamos los puntos con sus respectivos desplazamientos
plt.plot(x, dis)
plt.show()