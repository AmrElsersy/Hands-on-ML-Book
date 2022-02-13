import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# =========== plot a line between each point ===========
# plt.plot(x, y)
# o = scatter
# plt.plot(x, y, "o")
# marker o = point, marker size, color
# plt.plot(y, marker="o", linewidth = 10, color="r")

'''
# =========== multiple lines ===========
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1, color = "g")
plt.plot(y2, color = "r")

# =========== add lable to the chart ===========
plt.title("Chart title sersy")
plt.xlabel("X label ray2")
plt.ylabel("Y label 7ray2")

# add grid to the chart
plt.grid(color="g", linestyle="--")
'''

# =========== subplots ===========
# 2 rows, 1 column, and current subplot is 1
'''
plt.subplot(2,1,1)
plt.plot(y1)
plt.title("title y1")

plt.subplot(2,1,2)
plt.plot(y2)
plt.title("title y2")

plt.suptitle("Subtitle ray2")
'''

# =========== Scatter ==========
# plt.scatter(x, y, color="r")

# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')


# ========= Pie Chart ==========
# # calculate the percentage of each in a Pie chart
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)


plt.show()
