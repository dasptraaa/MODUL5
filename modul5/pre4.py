import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Scatter plot with default settings
plt.scatter(x, y, label='Variasi 1')

# Scatter plot with green color, square markers, and larger size
plt.scatter(x, y, color='green', marker='s', s=100, label='Variasi 2')

# Scatter plot with red color, triangular markers, and smaller size
plt.scatter(x, y, color='red', marker='^', s=50, label='Variasi 3')

# Scatter plot with blue color, diamond markers, and varying sizes
sizes = [20, 40, 60, 80, 100]
plt.scatter(x, y, color='blue', marker='D', s=sizes, label='Variasi 4')

# Adding title and axis labels
plt.title('Scatter Plot dengan 4 Variasi')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
