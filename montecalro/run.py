#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(1)
fig, ax = plt.subplots()
xdata, ydata = [], []
xdata2, ydata2 = [], []
ln, = plt.plot([], [], 'ro', animated=True)
ln1, = plt.plot([], [], 'ro', animated=True)
#text = plt.text(0, 1.1, 'None', animated=True)

num_total_frames = 5000

an = np.linspace(0, 2 * np.pi, 100)
ax.plot(np.cos(an), np.sin(an))
x_cords = 2*np.random.rand(num_total_frames) - 1
y_cords = 2*np.random.rand(num_total_frames) - 1

def init():
    ax.set_aspect('equal', 'box')    
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ln.set_c('red')
    ln1.set_c('green')
    return ln, ln1

_num, = np.where((x_cords**2 + y_cords**2) <=1 )
inner_num = []
def update(frame):
    if x_cords[frame]**2 + y_cords[frame]**2 <= 1:
        xdata.append(x_cords[frame])                
        ydata.append(y_cords[frame])
        inner_num.append(1)
    else:
        xdata2.append(x_cords[frame])
        ydata2.append(y_cords[frame])
    #text.set_text("4*{}/{} = {}".format(len(inner_num), frame+1, 4*len(inner_num)/ (frame+1)))
    plt.title("4*{:>5d}(in)/{:5d}(total) = {:>6.4} $\simeq$ $\pi$".format(len(inner_num), frame+1, 4*len(inner_num)/ (frame+1)))
    ln.set_data(xdata, ydata)
    ln1.set_data(xdata2, ydata2)
    return ln, ln1

#text.set_text("{}/{}".format(len(_num), 1000))

anim = FuncAnimation(fig, update, frames=np.arange(0, num_total_frames),
                    init_func=init, blit=True)

anim.save('basic_animation.mp4', fps=60, dpi=300)# extra_args=['-vcodec', 'libx264'])
#ax.text(0, 0, "{}/{}".format(len(_num), num_total_frames))
plt.show()
