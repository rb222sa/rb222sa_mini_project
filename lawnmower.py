import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

lawn_map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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



rows = len(lawn_map)
cols = len(lawn_map[0])

plt.figure()
color_map = ListedColormap(['red', 'green', 'yellow'], 'indexed')

print("Plot origo", lawn_map[0][0])

lawn_map.reverse()  # Turn plot upside-down
plt.pcolormesh(lawn_map, edgecolors='k', linewidth=2, cmap=color_map)
ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()






# plt.grid() använd för trails?




# lawn_map = [[L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,O,O,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,L,L,L,L,L,L,L,L,L,L,L,O,O,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,L,L,L,S,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,O,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
# [L,L,L,L,L,L,L,L,O,O,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L]]