import matplotlib.pyplot as plt

print("=" * 50)
print("PLOT GRAPHS USING MATPLOTLIB")
print("=" * 50)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o', color='blue')
plt.title('Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.bar(x, y, color='green')
plt.title('Bar Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.subplot(2, 2, 3)
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.subplot(2, 2, 4)
plt.scatter(x, y, color='red', s=100)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.tight_layout()
plt.savefig('graphs.png')
print("\nGraphs saved as 'graphs.png'")
plt.show()

print("=" * 50)