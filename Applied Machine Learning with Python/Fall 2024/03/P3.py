import numpy as np

class KNN_classifier:
    def __init__(self, n_neighbors: int, **kwargs):
        self.K = n_neighbors

    def fit(self, x: np.array, y: np.array):
        self.x_train = x
        self.y_train = y

    def predict(self, x: np.array):
        predictions = []
        for x_test in x:
            distances = np.linalg.norm(self.x_train - x_test, axis=1)
            k_indices = np.argsort(distances)[:self.K]
            k_nearest_labels = self.y_train[k_indices]
            most_common = np.bincount(k_nearest_labels).argmax()
            predictions.append(most_common)
        predictions = np.array(predictions)
        return predictions
        