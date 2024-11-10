import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr
import mandelbrot

# colorpoints = [(1-(1-q)**4, c) for q, c in zip(np.linspace(0, 1, 20), 
#                                                cycle(['#77afff', '#000000', 
#                                                       '#7400ca',]))]

# cmap = clr.LinearSegmentedColormap.from_list('mycmap', 
#                                              colorpoints, N=2048)

p_center, q_center = -0.7435, 0.1314  
zoom_factor = 0.005  

pmin, pmax = p_center - zoom_factor, p_center + zoom_factor
qmin, qmax = q_center - zoom_factor, q_center + zoom_factor

ppoints, qpoints = 2000, 2000  
max_iterations = 500
infinity_border = 2

image = mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints, max_iterations, infinity_border) 
plt.figure(figsize=(10, 10))
plt.xticks([])
plt.yticks([])
plt.imshow(image, cmap=cmap, interpolation='none')
plt.axis('off')
plt.savefig("mandelbrot_zoomed.png", format="png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()
