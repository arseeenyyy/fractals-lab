import numpy as np
import matplotlib.pyplot as plt

n_points = 100000
x, y = 0, 0
x_points = []
y_points = []
probabilities = [0.01, 0.85, 0.07, 0.07]

# "original", "thelypteris"
variation = ""

if variation == "original":
    transforms = [
        (0, 0, 0, 0.16, 0, 0),            
        (0.85, 0.04, -0.04, 0.85, 0, 1.6), 
        (0.2, -0.26, 0.23, 0.22, 0, 1.6),  
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44) 
    ]

elif variation == "thelypteris":
    transforms = [
        (0, 0, 0, 0.25, 0, -0.4),          
        (0.85, 0.05, -0.05, 0.85, 0, 1.6), 
        (0.3, -0.15, 0.3, 0.3, 0, 1.3),    
        (-0.25, 0.2, 0.2, 0.25, 0, 0.5)    
    ]

def next_point(x, y):
    rand = np.random.rand()
    if rand < probabilities[0]:
        a, b, c, d, e, f = transforms[0]
    elif rand < probabilities[0] + probabilities[1]:
        a, b, c, d, e, f = transforms[1]
    elif rand < probabilities[0] + probabilities[1] + probabilities[2]:
        a, b, c, d, e, f = transforms[2]
    else:
        a, b, c, d, e, f = transforms[3]
    
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new

for _ in range(n_points):
    x, y = next_point(x, y)
    x_points.append(x)
    y_points.append(y)

plt.figure(figsize=(6, 10))
plt.scatter(x_points, y_points, s=0.1, color='green')
plt.axis("equal")
plt.axis("off")
plt.show()
