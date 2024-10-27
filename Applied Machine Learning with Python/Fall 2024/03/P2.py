#ссылка на ноутбук https://colab.research.google.com/drive/1ZD6UuuUmUKIyF0lTES0-nL6RpCZD8htf?usp=sharing

#ПРОРЕШАННЫЙ НОУТБУК
with open('input.txt') as file:
    for s in file:
        g = s.split()
import sklearn
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
random_seed = 4238

np.random.seed(random_seed)
n_splits = 3

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

k_values = range(1, 51)
mean_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k, p=1)
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring="accuracy")
    mean_scores.append(scores.mean())
    pass
plt.figure(figsize=(10, 7))
plt.plot(k_values, mean_scores)
plt.title('KNN Cross Validation Scores')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Average Score')
plt.grid(True)
plt.show()

optimal_k = k_values[np.argmax(mean_scores)]
print(optimal_k)
#Ответ:евклидово расстояние