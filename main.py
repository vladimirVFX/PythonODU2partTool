#Lib
from scipy.integrate import odeint  #CalculateODU
import numpy as np                  #MassiveAndMathematics
import matplotlib.pyplot as plt     #Graphics

#RightPartIntegration
def f(y, x):
    return np.sqrt(5.0 - 4.0 * y ** 2)

def analytical(x):
    return np.cos(2.0 * x) + 0.5 * np.sin(2.0 * x)

x = np.arange(0.0, 1.0, 0.01)   #MassiveIntegrationPoints
y0 = [1.0, 1.0]                 #ListStartValues

solution = odeint(f,y0,x)
print(solution[0])              #SolutionInPointZero
print('numerical:')

plt.plot(x, solution)           #GraphicsNumericalSolution
plt.show()                      #CreateGraphics
print('analytical:')

plt.plot(x, analytical(x))      #CreateGraphics
plt.show()
