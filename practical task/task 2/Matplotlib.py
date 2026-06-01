import matplotlib.pyplot as plt
import numpy as np

# график 1
plt.figure()
x1 = [1.5, 5, 10, 15, 20]
y1 = [1.0, 7, 3, 5, 11]

x2 = [1.5, 5, 10, 15, 20]
y2 = [4, 3, 1, 8, 12]

plt.plot(x1, y1, color="red", marker="o", label="line 1")
plt.plot(x2, y2, linestyle="-.", color="green", marker="o", label="line 2")

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("1.png")
plt.close()

# график 2
x = [1.0, 2.0, 3.0, 4.0, 5.0]
y1 = [0.5, 7, 6, 3, 5]
y2 = [9.0, 4, 2, 4, 9]
y3 = [-7, -4, 2, -4, -7]

ax1 = plt.subplot(2, 2, (1, 2))
ax2 = plt.subplot(2, 2, 3)
ax3 = plt.subplot(2, 2, 4)

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y3)

plt.tight_layout()
plt.savefig("2.png")
plt.close()

# график 3
x = np.linspace(-5, 5, 11)
y = x ** 2

plt.plot(x, y, color="blue")

plt.arrow(0, 10, 0, -10,
          width=0.15,
          head_length=2,
          length_includes_head=True,
          fc="green",
          ec="black",
          linewidth=2)
plt.text(0, 10, "min",
         fontsize=18,
         color="black",
         ha="center",
         va="bottom")
plt.tight_layout()
plt.savefig("3.png")
plt.close()

# график 4
plt.figure()
x = np.linspace(0, 7, 7)
y = np.linspace(0, 7, 7)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y) + np.sin(2*X) * np.cos(2*Y)

plt.imshow(Z, extent=[0, 7, 0, 7], cmap="viridis")
plt.colorbar(shrink=0.5)
plt.tight_layout()
plt.savefig("4.png")
plt.close()

# график 5
plt.figure()
x = np.linspace(0, 5, 100)
y = np.sin(np.pi*x+np.pi/2)

plt.plot(x, y, color="red", linestyle="-", linewidth=2)
plt.fill_between(x, y, 0, alpha=0.5, color="blue")
plt.tight_layout()
plt.savefig("5.png")
plt.close()

# график 6
x = np.linspace(0, 5, 1000)
y = np.cos(np.pi * x)
y[y < -0.5] = np.nan

plt.figure(figsize=(8, 5))
plt.plot(x, y, linewidth=3)
plt.ylim(-1.0, 1.0)
plt.tight_layout()
plt.savefig("6.png")
plt.close()

# график 7
plt.figure(figsize=(12, 4))

ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 1, 2, 3, 4, 5, 6])

ax1.step(x, y, where='pre', color='green', marker="o")
ax1.grid(True)
ax2.step(x, y, where='post', color='green', marker="o")
ax2.grid(True)
ax3.step(x, y, where='mid', color='green', marker="o")
ax3.grid(True)

plt.tight_layout()
plt.savefig("7.png")
plt.close()

# график 8
plt.figure(figsize=(12, 6))

x = np.linspace(0, 10, 100)
y1 = -x**2 + 12*x
y2 = -0.6*x**2 + 6*x
y3 = -0.2*x**2 + 2*x

plt.fill_between(x, y1, y2, label='y1', color='green')
plt.fill_between(x, y2, y3, label='y2', color='orange')
plt.fill_between(x, y3, 0, label='y3', color='blue')

plt.plot(x, y1, linewidth=2, color='green')
plt.plot(x, y2, linewidth=2, color='orange')
plt.plot(x, y3, linewidth=2, color='blue')

plt.legend(loc='upper left')
plt.ylim(0, max(y1) + 5)
plt.tight_layout()
plt.savefig("8.png")
plt.close()

# график 9
plt.figure()
plt.pie([15, 10, 40, 15, 20],
        labels=['Ford','Toyota','BMW','AUDI','Jaguar'],
        explode=(0, 0, 0.1, 0, 0))
plt.tight_layout()
plt.savefig("9.png")
plt.close()

# график 10
plt.figure()
plt.pie([15, 10, 40, 15, 20],
        labels=['Ford','Toyota','BMW','AUDI','Jaguar'],
        wedgeprops={'width': 0.5})
plt.tight_layout()
plt.savefig("10.png")
plt.close()