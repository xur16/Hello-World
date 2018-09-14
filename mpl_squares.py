import matplotlib.pyplot as plt

x_axis=[1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(x_axis, squares, linewidth=5)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()