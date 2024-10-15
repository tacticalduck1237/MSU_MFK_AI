#Ссылка на ноутбук: https://colab.research.google.com/drive/1iD2KQYvWwE5mtDttIuG-zqfc8Dm7otLE?usp=sharing


#Прорешанный ноутбук
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загрузка датасета
X, y = load_breast_cancer(return_X_y=True)

# Разбиение датасета на train и test
X_train, x_test, y_train, y_test =train_test_split(X, y, test_size=0.3, shuffle=True, random_state=42)

# Задание классификатора и его обучение
clf = LogisticRegression()

# Предобработка датасета при помощи StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
x_test = sc.transform(x_test)

# Обучеение модели
# TODO: вызовите функцию обучения модели на тренировочной выборке X_train с вектором ответов y_train
clf.fit(X_train, y_train)

# Оценка качества получившегося решения
print(clf.score(x_test, y_test))

#Ответ 0.98
