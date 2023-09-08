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
    z = np.empty(c.shape, dtype=np.complex128)
    z[:] = c[:]
    nv = np.zeros(c.shape, dtype=np.int32)
    # True if the point is in set, False otherwise
    mask = np.empty(c.shape, dtype=np.bool_)
    for i in range(MAX_ITERS):
        mask[:] = (abs(z) <= 2)
        if (all(mask == False)): break
        z[mask] *= z[mask]
        z[mask] += c[mask]
        nv[mask] += 1
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

output = np.empty((height,width), dtype=np.int32)

x = np.empty((simd_width), dtype=np.complex128)
for h in range(height):
    cy = min_y + h * scale_y
    for w0 in range(width // simd_width):
        w = np.arange(w0*simd_width, (w0+1)*simd_width, dtype=np.int32)
        cx = min_x + w * scale_x
        x[:] = cx + 1j*cy
        # Works:
        #output[h,w] = mandelbrot_kernel(x[0])
        # Does not work:
        output[h,w] = mandelbrot_kernel2(x)

print(output)
