# Аномалии
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

data = pd.read_csv("digital_python-25-26/data/creditcard.csv")
print(data.head())

legit = data[data["Class"] == 0]
fraud = data[data["Class"] == 1]

X = data.drop(["Time", "Class"], axis=1)
y = data["Class"]

X_tr, X_tst, y_tr, y_tst = train_test_split(
    X, y, test_size=0.25
)

model1 = LogisticRegression()
model1.fit(X_tr, y_tr)

ConfusionMatrixDisplay.from_estimator(
    model1,
    X_tst,
    y_tst,
    display_labels=["Легитимная", "Мошенническая"],
)
plt.show()

model2 = RandomForestClassifier()
model2.fit(X_tr, y_tr)
ConfusionMatrixDisplay.from_estimator(
    model2,
    X_tst,
    y_tst,
    display_labels=["Легитимная", "Мошенническая"],
)
plt.show()  # 14

model3 = RandomForestClassifier()
model3.fit(X_tr, y_tr)
ConfusionMatrixDisplay.from_estimator(
    model3,
    X_tst,
    y_tst,
    display_labels=["Легитимная", "Мошенническая"],
)
plt.show()