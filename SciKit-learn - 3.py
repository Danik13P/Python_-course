import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

iris = sns.load_dataset("iris")

print (iris.head())

species_int = []
for row in iris.values:
    match row[4]:
    case "zetosa":
    species_int.append(1)
    case _

species_int = []
for row in iris.values:
    match row[4]:
    case "setosa":
    species_int.append(1)
    case "versicolor":
    species_int.append(2)
    case "virginica":
    species_int.append(3)

# species_int_df = pd.DataFrame(species_int)
# print(species_int_df.head())

data = iris[["sepal_length", "petal_length"]]
data["species"] = species_int

print(data.head())
print (data.shape)

data_df = data[(data["species"] == 1) | (data["species"] == 2)]
print (data_df.shape)

data_of_setosa = data[data["species"] == 1]
data_of_versicolor = data[data["species"] == 2]

plt.scatter(data_of_setosa["sepal_length"], data_of_setosa["petal_length"])
plt.scatter(data_of_versicolor["sepal_length"], data_of_versicolor["petal_length"])

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X, y)

x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

print(X1_p.shape)

X_p = pd.DataFrame(np.vstack([X1_p.reval(), X2_p.reval()]).T, columns=["sepal_length", "petal_length"])

print (X_p.head())

y_p = model.predict(X_p)

print (y_p)

plt.contourf(
    X1_p,
    X2_p,
    y_p.reshape(X1_p.shape),
    alpha=0.3,
    levels=[0, 2.5, 3.5]
)

plt.show()

from sklearn.tree import DecisionTreeClassifier

max_depth = [[1, 2, 3, 4], [5, 6, 7, 8]]

fig, ax = plt.subplots(2, 4, sharex="col", sharey="row")

for i in range(2):
    j = 0
    for md in max_depth[i]:
    model = DecisionTreeClassifier(max_depth=md)
    model.fit(X, y)
    y_p = model.predict(X_p)

print(y_p)

plt.contour(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 2.5, 3.5])

X = data_df_A[["sepal_length", "petal_length"]]
y = data_df_A["species"]

j = 0
for md in max_depth:

    model = DecisionTreeClassifier(max_depth=md)
    model.fit(X, y)

    y_p = model.predict(X_p)

    ax[0,j].scatter(data_of_virginica_A["sepal_length"], data_of_virginica_A["petal_length"])
    ax[0,j].scatter(data_of_versicolor_A["sepal_length"], data_of_versicolor_A["petal_length"])

    ax[0,j].contourf(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 2.5, 3.5])
    j += 1

plt.show()

X = data_df_B[["sepal_length", "petal_length"]]
y = data_df_B["species"]

j = 0
for md in max_depth:

    model = DecisionTreeClassifier(max_depth=md)
    model.fit(X, y)
    I

    y_p = model.predict(X_p)

    ax[1,j].scatter(data_of_virginica_B["sepal_length"], data_of_virginica_B["petal_length"])
    ax[1,j].scatter(data_of_versicolor_B["sepal_length"], data_of_versicolor_B["petal_length"])

ax[1,j].contourf(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 2.5, 3.5])
j += 1

plt.show()

# + простые модели + быстро решаются + параллелизм
# + голосование
# + непараметрическа - эффективная работа с данные
# - осмысленные выводы сложно сделать