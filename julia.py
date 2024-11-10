import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

colorpoints = [(1-(1-q)**4, c) for q, c in zip(np.linspace(0, 1, 20), 
                                               cycle(['#77afff', '#000000', 
                                                      '#f21818',]))]

cmap = clr.LinearSegmentedColormap.from_list('mycmap', colorpoints, N=2048)


ppoints, qpoints = 1000, 1000
max_iterations = 300  
infinity_border = 2

c = complex(-0.2, 0.75)

def julia(pmin, pmax, ppoints, qmin, qmax, qpoints, c, max_iterations, infinity_border):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]
    z = p + 1j * q  

    for k in range(max_iterations):
        z = z ** 2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

pmin, pmax, qmin, qmax = -1.5, 1.5, -1.5, 1.5

image = julia(pmin, pmax, ppoints, qmin, qmax, qpoints, c, max_iterations, infinity_border)
plt.figure(figsize=(10, 10))
plt.xticks([])
plt.yticks([])
plt.imshow(image, cmap=cmap, interpolation='none')
plt.axis('off')
plt.savefig("julia.png", format="png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()
