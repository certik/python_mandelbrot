import numpy as np

MAX_ITERS = 1000
def mandelbrot_kernel(c):
    z = c
    nv = 0
    for i in range(MAX_ITERS):
        if abs(z) > 2:
            break
        z = z*z + c  # z**2 + c is slower
        nv += 1
    return nv

n = 8
height = 4096 // n
width = 4096 // n
min_x = -2.0
max_x = 0.47
min_y = -1.12
max_y = 1.12
scale_x = (max_x - min_x) / width
scale_y = (max_y - min_y) / height

output = np.empty((height,width), dtype=np.float64)

for h in range(height):
    cy = min_y + h * scale_y
    for w in range(width):
        cx = min_x + w * scale_x
        output[h,w] = mandelbrot_kernel(cx + 1j*cy)

print(output)
