# фильтрация спама
# бинарная классификация
# Векторизация

# столбцы = слова (в тексте)
# строки = образцы текста
# ячейка = кол-во данных слов в данном тексте

# очистка: строчные, удаляют знаки препинания, (стоп-слова),

import numpy as np
import pandas as pd

data = pd.read_csv("digital_python-25-26/data/spam.csv")
print(data.head())

print(data.columns)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Message"])
w = vectorizer.get_feature_names_out()
print(w)
print(w[1000])
print(X)

from sklearn.model_selection import train_test_split

X_tr, X_ts, y_tr, y_ts = train_test_split(
    data["Message"], data["Spam"], test_size=0.25
)

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

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