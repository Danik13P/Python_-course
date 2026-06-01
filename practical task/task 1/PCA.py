import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

# Выбираем только два класса: 0 (Setosa) и 1 (Versicolor)
mask = y != 2
X = X[mask]
y = y[mask]

# Применяем PCA с 2 компонентами
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# График
plt.figure(figsize=(8, 6))
colors = ['red', 'blue']
labels = ['Setosa', 'Versicolor']
for label, color in zip(np.unique(y), colors):
    idx = y == label
    plt.scatter(X_pca[idx, 0], X_pca[idx, 1], c=color, label=labels[label], alpha=0.7)

plt.xlabel('Первая главная компонента')
plt.ylabel('Вторая главная компонента')
plt.title('PCA двух сортов Iris')
plt.legend()
plt.grid(True)
plt.show()