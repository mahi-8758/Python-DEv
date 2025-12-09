import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o', color='blue')
plt.title('Line Graph')
plt.savefig('graphs.png')
print("Graphs saved as 'graphs.png'")
plt.show()