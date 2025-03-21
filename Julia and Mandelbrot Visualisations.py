import numpy as np
import matplotlib.pyplot as plt

# Define the Mandelbrot function
def mandelbrot(c, max_iter):
    """Computes Mandelbrot iteration count for a given complex number c."""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Define the Julia function
def julia(c, z, max_iter):
    """Computes Julia set iteration count for a given complex number z."""
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Function to generate a fractal image
def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter, fractal_func, c=None):
    """Generates a fractal image (Mandelbrot or Julia set)."""
    img = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = xmin + (x / width) * (xmax - xmin)
            imag = ymin + (y / height) * (ymax - ymin)
            z = complex(real, imag)
            img[y, x] = fractal_func(c, z, max_iter) if c is not None else fractal_func(z, max_iter)
    return img

# Set parameters
width, height = 800, 800
max_iter = 300

# Generate and display Mandelbrot set
mandelbrot_img = generate_fractal(-2, 1, -1.5, 1.5, width, height, max_iter, mandelbrot)
plt.figure(figsize=(8, 8))
plt.imshow(mandelbrot_img, extent=(-2, 1, -1.5, 1.5), cmap='inferno')
plt.colorbar(label="Escape Time")
plt.title("Mandelbrot Set")
plt.show()

# Generate and display Julia set for c = 0 + 0.8i
julia_img1 = generate_fractal(-1.5, 1.5, -1.5, 1.5, width, height, max_iter, julia, complex(0, 0.8))
plt.figure(figsize=(8, 8))
plt.imshow(julia_img1, extent=(-1.5, 1.5, -1.5, 1.5), cmap='inferno')
plt.colorbar(label="Escape Time")
plt.title("Julia Set for c = 0 + 0.8i")
plt.show()

# Generate and display Julia set for c = -0.4 - 0.59i
julia_img2 = generate_fractal(-1.5, 1.5, -1.5, 1.5, width, height, max_iter, julia, complex(-0.4, -0.59))
plt.figure(figsize=(8, 8))
plt.imshow(julia_img2, extent=(-1.5, 1.5, -1.5, 1.5), cmap='inferno')
plt.colorbar(label="Escape Time")
plt.title("Julia Set for c = -0.4 - 0.59i")
plt.show()
