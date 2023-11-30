import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 4, 2, 9])
y4 = np.array([1, 7, 3, 8])

# Creating a plot for y1, y2, y3, and y4 with different colors and styles
plt.plot(y1, label="Garis 1", color='blue', linestyle='-', marker='o')
plt.plot(y2, label="Garis 2", color='green', linestyle='--', marker='s')
plt.plot(y3, label="Garis 3", color='red', linestyle='-.', marker='^')
plt.plot(y4, label="Garis 4", color='purple', linestyle=':', marker='d')

# Adding title and axis labels
plt.title("Plot Empat Garis dengan Corak Berbeda")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
