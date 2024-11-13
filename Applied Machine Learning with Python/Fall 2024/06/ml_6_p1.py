#Ссылка на ноутбук: https://colab.research.google.com/drive/10jsLTrZqP16zn0w8H71JoFIoRVnxMJzC?usp=sharing

#ПРОРЕШАННЫЙ НОУТБУК

import pandas as pd
import numpy as np

np.random.seed(42)

# Импортируйте необходимые классы и функции из соответствующих модулей sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
clf_tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42,
)

clf_tree.fit(X_train, y_train)
preds = clf_tree.predict(x_test)

acc = accuracy_score(y_test, preds)
import math
acc=math.floor(acc * 100)/100.0
print(acc)

#ответ: 0.98 (РАЗДЕЛИТЕЛЬ-ТОЧКА)