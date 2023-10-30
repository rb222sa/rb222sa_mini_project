import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation



x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 205)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)


def animation_frames(frame):
    x_data.append(frame * 10)
    y_data.append(frame)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,


animation = matplotlib.animation.FuncAnimation(fig, func=animation_frames, frames=np.arange(0, 5, 0.1), interval=10)

plt.show()


# https://www.youtube.com/watch?v=dOKHY_PUvqU