# SCiKit-Learn

import seeborn as sns
from matplotlib import pyplot as plt

iris = sns.load_dataset("iris")
print(iris.head())

print(type(iris))

print(type(iris.values))

print(iris.values.shape)

print(iris.columns)

print(iris.index)
sns.pairplot(iris, hue="")

plt.show()

# Строки - образцы - отдельный объект (sample)
# Столбцы - признаки (feature)
# Матрица признаков [число образцов на число признаков] - признаки - НЕзависимая переменная
# Целевой массив {target, label} [1 на число образцов] - зависимая переменная

X_iris = iris.drop('species', axis=1)
print(X_iris)

y_iris = iris['species']
print(y_iris)

# 1. Выбирается класс модели
# 2. Выбираются гиперпараметры модели
# 3. На основе данных создается матрица признаков и целевой вектор
# 4.

# 5. Обученная модель применяется к новым данным
# 5.1. Обучение с учителем - predict()

xfit = np.linspace(0, x.max(), 1000)
yfit = model.predict(xfit[:, None])

plt.plot(xfit, yfit, "r")

plt.plot(xfit, xfit * reg.coef_ + reg.intercept_, "k")

# y = kx + b

from sklearn.pipeline import make_pipeline

model = make_pipeline(PolynomialFeatures(2), LinearRegression())
reg = model.fit(x[:, np.newaxis], y)

xfit = np.linspace(x.min(), x.max(), 1000)
yfit = model.predict(xfit[:, None])

plt.plot(xfit, yfit, "r")

plt.show()

# Классификация. Логистическая регрессия

x_0 = iris[iris["species"] == "setosa"].iloc[:, 0].to_numpy()
y_0 = iris[iris["species"] == "setosa"].iloc[:, 1].to_numpy()
x_1 = iris[iris["species"] == "versicolor"].iloc[:, 0].to_numpy()
y_1 = iris[iris["species"] == "versicolor"].iloc[:, 1].to_numpy()

plt.scatter(x_0, y_0, color="red", alpha=0.5)
plt.scatter(x_1, y_1, color="green", alpha=0.5)

x_00 = iris[iris["species"] == "setosa"].iloc[:, 0].to_numpy()
x_11 = iris[iris["species"] == "versicolor"].iloc[:, 0].to_numpy()

# plt.scatter(x_0, y_0, color="red", alpha=0.5)

plt.scatter(x_00, np.full(50, 1), color="red", alpha=0.5)
plt.scatter(x_11, np.full(50, 5), color="green", alpha=0.5)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

x = iris[iris["species"] != "virginica"].iloc[:, 0].to_numpy()
print(x.shape)
y = iris[iris["species"] != "virginica"].iloc[:, 1]
print(y.shape)

# model.fit(x[:, None], y)

# print(x)
# print(y)

tree = DecisionTreeClassifier()
tree.fit(x, y)

np.meshgrid(
    np.linspace(x[:, :0].min(), x[:, :0].max(), 1000),
    np.linspace(x[:, 1:1].min(), x[:, 1:1].max(), 1000)
)

print(np.c_[[1,2,3,4,5], [10,20,30,40,50]])

print(np.ravel([[1,2,3,4,5], [10,20,30,40,50]]))

xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min(), x[:, 0].max(), 100),
    np.linspace(x[:, 1].min(), x[:, 1].max(), 100),
)

Z = tree.predict(np.c_[xx.ravel(), yy.ravel()]) # .reshape(xx.shape)

ax = plt.gca()

ax.contourf(xx, yy, Z, alpha=0.3)

