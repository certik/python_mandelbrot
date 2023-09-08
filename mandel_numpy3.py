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

# c: Annotated[c64[:], SIMD]
def mandelbrot_kernel2(c):
    z = c
    nv = np.zeros(c.shape, dtype=np.float32)
    in_set_mask = np.empty(c.shape, dtype=np.bool8)
    in_set_mask[:] = True
    for i in range(MAX_ITERS):
        if (all(in_set_mask == False)): break
        in_set_mask[:] = (abs(z) <= 2)
        nv[in_set_mask] += 1
        z[in_set_mask] = z[in_set_mask]*z[in_set_mask] + c[in_set_mask]  # z**2 + c is slower
    return nv

n = 512
height = 4096 // n
width = 4096 // n
min_x = -2.0
max_x = 0.47
min_y = -1.12
max_y = 1.12
scale_x = (max_x - min_x) / width
scale_y = (max_y - min_y) / height
simd_width = 1

output = np.empty((height,width), dtype=np.float64)

for h in range(height):
    cy = min_y + h * scale_y
    for w0 in range(width // simd_width):
        w = np.arange(w0*simd_width, (w0+1)*simd_width)
        cx = min_x + w * scale_x
        x = cx + 1j*cy
        # Works:
        output[h,w] = mandelbrot_kernel(x[0])
        # Does not work:
        #output[h,w] = mandelbrot_kernel2(x)

print(output)
