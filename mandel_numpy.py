import numpy as np

MAX_ITERS = 1000


n = 512
height = 4096 // n
width = 4096 // n
min_x = -2.0
max_x = 0.47
min_y = -1.12
max_y = 1.12
scale_x = (max_x - min_x) / width
scale_y = (max_y - min_y) / height

#output = np.empty((height,width), dtype=np.float64)

cs = np.zeros((height, width), dtype=complex)
cs[:,:] = 1
zs = np.zeros((height, width), dtype=complex)
mask = np.full((height, width), True, dtype=bool)
for i in range(MAX_ITERS):
    zs[mask] = zs[mask] * zs[mask] + cs[mask]
    mask[np.abs(Z) > 2] = False

#for h in range(height):
#    cy = min_y + h * scale_y
#    for w in range(width):
#        cx = min_x + w * scale_x
#        output[h,w] = mandelbrot_kernel(cx + 1j*cy)

#print(output)
print(zs)
print(mask)
