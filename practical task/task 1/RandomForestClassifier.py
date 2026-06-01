import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

# Выбираем только два класса: 0 (Setosa) и 1 (Versicolor)
mask = y != 2
X = X[mask]
y = y[mask]

# Используем только первые два признака (длина и ширина чашелистика)
X_2d = X[:, :2]

# Обучаем случайный лес
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_2d, y)

# Строим сетку для отображения решающей границы
xx, yy = np.meshgrid(np.linspace(X_2d[:, 0].min() - 0.5, X_2d[:, 0].max() + 0.5, 200),
                     np.linspace(X_2d[:, 1].min() - 0.5, X_2d[:, 1].max() + 0.5, 200))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# График
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, levels=[-0.5, 0.5, 1.5], colors=['red', 'blue'])
colors = ['red', 'blue']
labels = ['Setosa', 'Versicolor']
for label, color in zip(np.unique(y), colors):
    idx = y == label
    plt.scatter(X_2d[idx, 0], X_2d[idx, 1], c=color, label=labels[label], edgecolor='k', s=50)

plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.title('RandomForestClassifier: граница между двумя классами')
plt.legend()
plt.grid(True)
plt.show()