
import matplotlib.pyplot as plt

x=[200,400,600,800,1000 ]
y=[2.48,1.92,4.32,7.68,6.0]
plt.plot(x,y)
plt.xlabel('Tamaño de la matriz')
plt.ylabel('Tiempo (s)')
plt.title('Rendimiento de la CPU')
#plt.grid()
plt.savefig('mpl_performance.png')
#plt.show()

