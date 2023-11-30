import matplotlib.pyplot as plt
import numpy as np

# Set the points for the line
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Plot the line with red color, solid line style, and circle markers
plt.plot(xpoints, ypoints, marker='o', linestyle='-', color='red', label='Line from (1,3) to (8,10)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')

# Add grid lines
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()
