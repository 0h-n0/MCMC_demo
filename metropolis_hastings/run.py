#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(1)
fig, ax = plt.subplots()
mean = [0, 0]
cov = [[1, 0.5,],
       [0.5, 1,]]
b_mean = [0, 0]
b_cov = [[1, 0],
       [0 ,1]]
_xlim = 5
_ylim = 5

pos = np.array([4, 4])
_x = np.arange(-_xlim, _xlim, 0.01)
_y = np.arange(-_ylim, _ylim, 0.01)

x, y = np.meshgrid(_x, _y)
num_total_frames = 1000

a = np.random.multivariate_normal(mean, cov, (1000))

sc = ax.scatter([], [], animated=True)
ln, = ax.plot([], [], animated=True, lw=3)

z = x**2 - x*y + y**2
def P(x1, x2):
    return np.exp(-0.5*(x1**2 - x1*x2 + x2**2))
    
plt.contour(x, y, z, 20, alpha=0.2)

def init():
    ax.set_aspect('equal', 'box')    
    ax.set_xlim(-_xlim, _xlim)
    ax.set_ylim(-_ylim, _ylim)

xdata, ydata = [], []
xldata, yldata = [], []

xldata.append(pos[0])
yldata.append(pos[1])

def update(frame):
    t_pos = np.zeros(2)
    _b = 0.5
    t_pos[0] = pos[0] + np.random.normal(0, _b)
    t_pos[1] = pos[1] + np.random.normal(0, _b)
    a = P(t_pos[0], t_pos[1]) / P(pos[0], pos[1])
    xldata.append(t_pos[0])
    yldata.append(t_pos[1])        
    pl = ax.plot([xldata[frame], xldata[frame+1]], [yldata[frame], yldata[frame+1]], lw=0.5, alpha=0.4, c='k')
    tmp_p = np.random.uniform(0, 1)
    
    if a > 1 or a > tmp_p:
        xdata.append(t_pos[0])
        ydata.append(t_pos[1])        
        sc = ax.scatter(xdata[frame], ydata[frame], c='b', alpha=0.3)
        pos[0] = t_pos[0]
        pos[1] = t_pos[1]        
    else:
        xdata.append(t_pos[0])
        ydata.append(t_pos[1])    
        sc = ax.scatter(xdata[frame], ydata[frame], c='r', alpha=0.3, marker='x')        
    return sc, pl

init()

anim = FuncAnimation(fig, update, frames=np.arange(0, num_total_frames))
#plt.show()
anim.save('anim_metropolis_b05.mp4', fps=60, dpi=600)

