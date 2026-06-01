import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
x = iris.data
y = iris.target

# Выбираем два класса: 0 (Setosa) и 1 (Versicolor)
x = x[y != 2][:, 0:2]  # берём первые два признака
y = y[y != 2]

# KMeans
model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(x)

# Сетка
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min(), x[:, 0].max(), 100),
    np.linspace(x[:, 1].min(), x[:, 1].max(), 100),
)

# Разделяем точки по истинным классам
x_0 = x[y == 0][:, 0]
y_0 = x[y == 0][:, 1]
x_1 = x[y == 1][:, 0]
y_1 = x[y == 1][:, 1]

# Предсказания кластеров на всей сетке
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# График
plt.scatter(x_0, y_0, color="red", alpha=0.5, label="Setosa")
plt.scatter(x_1, y_1, color="blue", alpha=0.5, label="Versicolor")

ax = plt.gca()
ax.contourf(xx, yy, Z, alpha=0.3, levels=[-0.5, 0.5, 1.5])

# Добавляем центры кластеров
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            marker='X', s=200, c='black', label='Центры кластеров')

plt.legend()
plt.show()