import numpy as np
import matplotlib.pyplot as plt

# Create the time grid
T = 100.0
dt = 0.02
N = int(T/dt)
t = np.linspace(0.0,T,N)

# Solving the ODE
# Initial conditions

z0 = 100.0
b0 = 10.0
zt = 100.0
g = 9.81

# Initialize the vector u

u = np.array([z0,b0])

# Initialize the vector that will contain the solution
U = [u]

# Soving using the Euler method

for i in range(1,N):
    u = np.array([u[0]+dt*u[1],
                  u[1]+dt*g*(1-u[0]/zt)])
    U.append(u)

# Visualising the results
z_values = [u[0] for u in U]

plt.figure(figsize=(10,6))
plt.plot(t,z_values,label="z(t)",color="blue")
plt.title("Phugoid solution using the Euler method")
plt.xlabel("t[s]")
plt.ylabel("z[m]")
plt.grid(True)
plt.show()
