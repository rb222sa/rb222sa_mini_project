import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time
import math
from random import uniform


small_lawn_map = [[1,1,0,1,1],
                [1,1,0,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1]]

big_lawn_map =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

current_lawn_map = small_lawn_map
rows = len(current_lawn_map)
cols = len(current_lawn_map[0])

fig = plt.figure()
color_map = ListedColormap(['red', 'green', 'yellow'], 'indexed')
current_lawn_map.reverse()  # Turn plot upside-down
plt.pcolormesh(current_lawn_map, edgecolors='k', linewidth=0.5, cmap=color_map)
ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")

angle = 2*math.pi
pos_x = 0.0
pos_y = 0.0
v_x = 0.3
v_y = 0.3
start = time.time()
previous_time = start
print(rows, cols)


#   Compute new position by using given equation in assignment pdf,
#   "x^i+1 = x^i + vx∆t" 
def update_pos(current_time, pos_x, pos_y, v_x, v_y):
    global previous_time
    elapsed_time = current_time - previous_time
    new_x = pos_x + (v_x * (elapsed_time))     
    new_y = pos_y + (v_y * (elapsed_time))
    previous_time = current_time
    return new_x, new_y


def check_collision(pos_x, pos_y, v_x, v_y):
    if int(pos_x) >= 5:
        v_x = math.cos(uniform(0.0,-1.0))
        v_y = math.sin(uniform(0.0, 1.0))
    if int(pos_x) < 0:
        v_x = math.cos(uniform(0.0, 1.0))
        v_y = math.sin(uniform(0.0, 1.0))
    if int(pos_y) > 4:
        v_x = math.cos(uniform(0.0, 1.0))
        v_y = math.sin(uniform(0.0, -1.0))
    if int(pos_y) < 0:
        v_x = math.cos(uniform(0.0, 1.0))
        v_y = math.sin(uniform(0.0, 1.0))
    return v_x, v_y


# Starting the lawnmower
for i in range(0, 20):
    pos_x, pos_y = update_pos(time.time(), pos_x, pos_y, v_x, v_y)
    v_x, v_y = check_collision(pos_x, pos_y, v_x, v_y)
    print(f"x: {pos_x}\t y:{pos_y}")
    time.sleep(1)


computingtime = time.time() - previous_time
print(computingtime)



# https://www.geeksforgeeks.org/python-time-module/
# 