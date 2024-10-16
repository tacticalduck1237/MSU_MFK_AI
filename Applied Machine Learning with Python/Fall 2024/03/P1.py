#ссылка на ноутбук https://colab.research.google.com/drive/1m-RSQa9tzRcOv_x3DGf9-PFqXg-NYxO2?usp=sharing

#прорешанный ноутбук

import sklearn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

random_seed = 4238
np.random.seed(random_seed)

X, y = load_breast_cancer(return_X_y=True)
X_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True, random_state=42
)

clf = KNeighborsClassifier(n_neighbors=8, p=1)
clf.fit(X_train, y_train)

predictions = clf.predict(x_test)
acc = accuracy_score(y_test, predictions)

print(acc)

#ответ:0.97