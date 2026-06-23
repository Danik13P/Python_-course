# фильтрация спама
# бинарная классификация
# Векторизация

# столбцы = слова (в тексте)
# строки = образцы текста
# ячейка = кол-во данных слов в данном тексте

# очистка: строчные, удаляют знаки препинания, (стоп-слова),

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("digital_python-25-26/data/spam.csv")
print(data.head())
print(data.columns)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Message"])
w = vectorizer.get_feature_names_out()
print(w)
print(w[1000])
print(X)

X_tr, X_ts, y_tr, y_ts = train_test_split(
    data["Message"], data["Spam"], test_size=0.25
)

md = Pipeline([("vectorizer", CountVectorizer()), ("nb", MultinomialNB())])
md.fit(X_tr, y_tr)

texts = [
    "Hi! How are you?", "I'm # 0",
    "Win the lottery", "# 0",
    "Free subscription", "# 1",
    "Black Friday", "# 0",
    "Nice to meet you", "# 0"
]
print(md.predict(texts))

data = pd.read_csv("digital_python-25-26/data/phishing.csv")
print(data.head())
print(data.columns)

X = data.drop(columns=["class"])
print(X.columns)
y = pd.DataFrame({"class"})

X_tr, X_tst, y_tr, y_tst = train_test_split(
    X, y, test_size=0.25
)

dt = DecisionTreeClassifier()
model = dt.fit(X_tr, y_tr)
predict =

print(accuracy_score())

print(accuracy_score(predict, y_test))

# Классификации: бинарные(двоичные), мультиклассовые, многометочные
# - точность (precision)
# - полнота (recall)
# - специфичность (specificity)
# - чувствительность (sensitivity)
# - F1-мера

# Метрики: - процент ошибок, процент правильных ответов (accuracy)
# Типы ошибочных ответов: ложноположительные, ложноотрицательные
# Типы правильных ответов: истиноположительные, истиноотрицательные

predict = model.predict(X_ts)

print(accuracy_score(predict, y_ts))