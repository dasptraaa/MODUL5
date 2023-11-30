import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

# Creating a plot for y1 and y2
plt.plot(y1, label="Garis 1")
plt.plot(y2, label="Garis 2")

# Adding title and axis labels
plt.title("Plot Dua Garis")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
