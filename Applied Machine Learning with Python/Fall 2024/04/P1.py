#ссылка на ноутбук https://colab.research.google.com/drive/1aacy0NIewvsFfa91n251ar5RzmCz3vDe?usp=sharing

#ПРОРЕШАННЫЙ НОУТБУК

import numpy as np

np.random.seed(42)

# Функция подсчета градиента
def gradient(y_true: int, y_pred: float, x: np.array) -> np.array:
    """
    Вычисляет градиент по параметрам модели для одного объекта x.
    y_true - истинное значение ответа для объекта x
    y_pred - предсказанное значение модели для класса 1
    x - вектор признаков объекта, без добавления bias
    """
    # Concatenate x with a 1 for the bias at the end, matching alpha structure
    x_with_bias = np.append(x, 1)  # Add bias as the last element of x
    grad = (y_pred - y_true) * x_with_bias
    return grad


# Функция обновления весов
def update(alpha: np.array, gradient: np.array, lr: float):
    """
    Обновляет вектор параметров alpha с использованием градиента и learning rate.
    """
    alpha_new = alpha - lr * gradient  # Standard gradient descent update
    return alpha_new


# функция тренировки модели
def train(
    alpha0: np.array, x_train: np.array, y_train: np.array, lr: float, num_epoch: int
):
    """
    Тренирует модель с помощью градиентного спуска.
    alpha0 - начальное приближение параметров модели
    x_train - матрица объект-признак обучающей выборки
    y_train - верные ответы для обучающей выборки
    lr - learning rate
    num_epoch - количество эпох обучения
    """
    alpha = alpha0.copy()
    for epo in range(num_epoch):
        for i, x in enumerate(x_train):
            # Use the logistic (sigmoid) function for prediction
            linear_combination = np.dot(alpha[:-1], x) + alpha[-1]  # Separate bias term
            y_pred = 1 / (1 + np.exp(-linear_combination))
            
            # Calculate gradient
            grad = gradient(y_train[i], y_pred, x)
			# Update model parameters
            alpha = update(alpha, grad, lr)
    return alpha