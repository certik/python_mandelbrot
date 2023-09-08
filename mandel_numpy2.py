import numpy as np

ITERATIONS = 100
n = 4
DENSITY = 4096 // n
x_min, x_max = -2.0, 0.47
y_min, y_max = -1.12, 1.12

x, y = np.meshgrid(np.linspace(x_min, x_max, DENSITY, endpoint=False),
                   np.linspace(y_min, y_max, DENSITY, endpoint=False))
print(x.shape)
c = x + 1j*y
z = c.copy()
fractal = np.zeros(z.shape, dtype=np.uint8) + 100
#print(z.shape)

for n in range(ITERATIONS):
#    print("Iteration %d" % n)
    mask = abs(z) <= 2
    z[mask] *= z[mask]
    z[mask] += c[mask]
    fractal[(fractal == 100) & (~mask)] = n

print(fractal)
#print("Saving...")
#np.savetxt("fractal.dat", np.log(fractal))
#np.savetxt("coord.dat", [x_min, x_max, y_min, y_max])
