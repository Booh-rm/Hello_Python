import numpy as np
import matplotlib.pyplot as plt

datos = np.random.randint(1, 11, size=100)

plt.hist(datos, bins=range(1,12), align='left', edgecolor='black', alpha=0.75)

plt.xticks(range(1,11))
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos aleatorios entre 1 y 10')

plt.show()
