import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

grid_size = 50
Z = np.random.choice([0, 1], size=(grid_size, grid_size))

def count_neighbors(Z):
    return sum(np.roll(np.roll(Z, i, 0), j, 1)
               for i in (-1, 0, 1) for j in (-1, 0, 1)
               if (i != 0 or j != 0))

def evolve(frame_num, Z, mat):
    count = count_neighbors(Z)
    Z_next = (count == 3) | (Z & (count == 2))
    mat.set_data(Z_next)
    Z[:] = Z_next[:]
    return mat,

fig, ax = plt.subplots()
mat = ax.matshow(Z)
ani = animation.FuncAnimation(fig, evolve, frames=100, fargs=(Z, mat), interval=50)
plt.show()