import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

colorpoints = [(1-(1-q)**4, c) for q, c in zip(np.linspace(0, 1, 20), 
                                               cycle(['#77afff', '#000000', 
                                                      '#7400ca',]))]

cmap = clr.LinearSegmentedColormap.from_list('mycmap', colorpoints, N=2048)

ppoints, qpoints = 1000, 1000
max_iterations = 500
infinity_border = 2

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations, infinity_border):
    image = np.zeros((ppoints, qpoints)) 
    p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)] 
    c = p + 1j * q
    z = np.zeros_like(c)
    for k in range(max_iterations): 
        z = z ** 2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k 
        z[mask] = np.nan
    return -image.T 

pmin, pmax, qmin, qmax = -2.0, 1.0, -1.5, 1.5  
image1 = mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints, max_iterations, infinity_border)
plt.figure(figsize=(10, 10))
plt.xticks([])
plt.yticks([])
plt.imshow(image1, cmap=cmap, interpolation='none')
plt.axis('off')
plt.savefig("mandelbrot.png", format="png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.close() 

p_center, q_center = -0.7435, 0.1314 
zoom_factor = 0.005  
zoom_pmin, zoom_pmax = p_center - zoom_factor, p_center + zoom_factor
zoom_qmin, zoom_qmax = q_center - zoom_factor, q_center + zoom_factor

image2 = mandelbrot(zoom_pmin, zoom_pmax, ppoints, zoom_qmin, zoom_qmax, qpoints, max_iterations, infinity_border)
plt.figure(figsize=(10, 10))
plt.xticks([])
plt.yticks([])
plt.imshow(image2, cmap=cmap, interpolation='none')
plt.axis('off')
plt.savefig("mandelbrot_zoomed.png", format="png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.close()  