#ССЫЛКА НА НОУТБУК https://colab.research.google.com/drive/16mjEK78gJXnat66IPwBD_PPSVKJa7AD-?usp=sharing

# ПРОРЕШАННЫЙ НОУТБУК
import numpy as np
from collections import defaultdict

class KMeans(object):
    def __init__(self, K, init):
        """
        Конструктор класса KMeans.

        Параметры:
        - K: количество кластеров
        - init: начальные центры кластеров размерности K x M
        """
        self.K = K
        self.centroids = init  # Начальные центры кластеров
        self.labels_ = None  # Метки кластеров для объектов
        self.converged = False  # Флаг для проверки сходимости алгоритма

    def _euclidean_distance(self, x, y):
        """
        Вычисление евклидовой метрики между точкой и центрами кластеров.
        Параметры:
        - x: точка данных
        - y: массив центров кластеров
        Возвращает:
        - расстояния между точкой и всеми центрами кластеров
        """
        return np.sqrt(((x - y) ** 2).sum(axis=1))

    def fit(self, X):
        """
        Метод обучения модели KMeans.

        Параметры:
        - X: данные для кластеризации (n_samples x n_features)

        Выполняет итерации кластеризации до сходимости.
        """
        n_samples = X.shape[0]
        self.labels_ = np.zeros(n_samples, dtype=int)  # Инициализируем метки
        iteration = 0  # Счетчик итераций

        while not self.converged:
            # Шаг 1: Присвоение меток объектам на основе ближайшего центра кластера
            for i in range(n_samples):
                distances = self._euclidean_distance(X[i], self.centroids)  # Евклидова метрика
                self.labels_[i] = np.argmin(distances)  # Назначаем объекту ближайший кластер

            # Шаг 2: Обновление центров кластеров
            new_centroids = np.zeros_like(self.centroids)
            for k in range(self.K):
                # Получаем все объекты, принадлежащие текущему кластеру
                points_in_cluster = X[self.labels_ == k]
                if len(points_in_cluster) > 0:
                    new_centroids[k] = points_in_cluster.mean(axis=0)  # Среднее значение точек
                else:
                    # Если кластер пуст, сохраняем предыдущий центр
                    new_centroids[k] = self.centroids[k]

            # Проверяем, сходятся ли центры кластеров
            shifts = np.linalg.norm(new_centroids - self.centroids, axis=1)  # Евклидова норма изменений
            if np.max(shifts) <= 0.001:
                self.converged = True  # Сходимся, если все изменения меньше 0.001
            else:
                self.centroids = new_centroids  # Обновляем центры
            iteration += 1

        print(f"Converged after {iteration} iterations.")

    def predict(self, X):
        """
        Метод предсказания кластеров для новых данных.

        Параметры:
        - X: данные для кластеризации (n_samples x n_features)

        Возвращает:
        - Метки кластеров для каждого объекта
        """
        n_samples = X.shape[0]
        labels = np.zeros(n_samples, dtype=int)

        for i in range(n_samples):
            distances = self._euclidean_distance(X[i], self.centroids)  # Евклидова метрика
            labels[i] = np.argmin(distances)  # Назначаем объекту ближайший кластер

        return labels
