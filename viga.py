# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
Ir = 7.84e-7   # Momento de Inercia respecto de IYY [m^4]
E = 2e11       # Módulo de Young [Pa]
F = -1000      # Fuerza [N]
l = 1.5        # Longitud [m]
y = 0.04       # Distancia al eje neutro [m]

# Cálculos predefinidos
M = F * l      # Momento flector [Nm]

# Factor para evitar recalcular múltiples veces
inv_EIr = 1 / (E * Ir)

# Cálculos de máximos
Md = (F * l ** 3) * inv_EIr / 3 * 1000    # Máximo desplazamiento [mm]
Me = (M * y / Ir) * 1e-6                  # Máxima tensión [MPa]

# Vector equidistante de posiciones en la viga
x = np.linspace(0, l, 100)

# Desplazamiento para todos los puntos
dis = F * x**2 * (3 * l - x) * inv_EIr / 6 * 1000

# Imprimir resultados
print(f'Máximo desplazamiento: {Md:.2f} mm')
print(f'Máxima tensión: {Me:.2f} MPa')

# Graficar el desplazamiento a lo largo de la viga
plt.plot(x, dis)
plt.xlabel('Posición a lo largo de la viga [m]')
plt.ylabel('Desplazamiento [mm]')
plt.title('Desplazamiento a lo largo de la viga')
plt.grid(True)
plt.show()
