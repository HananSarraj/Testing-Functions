# testing graphing function

import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3]
# corresponding y axis values
y = [2, 4, 1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - Total')
# naming the y axis
plt.ylabel('y - Heads')

# giving a title to my graph
plt.title('coin counter')

# function to show the plot
plt.show()