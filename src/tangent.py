#########
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*(np.pi),100)
y = np.tan(x)

plt.plot(x,y)
plt.title("Tangent Curve")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()