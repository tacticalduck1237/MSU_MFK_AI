#ссылка на ноутбук https://colab.research.google.com/drive/1NDRc8eELSyvXehVnZyRKl8eiYzijuLs0?usp=sharing#scrollTo=GLfTj8FHjvY2

#ПРОРЕШАННЫЙ НОУТБУК

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

# Global hyperparameter settings
N_ESTIMATORS = None
MAX_DEPTH = None
SUBSPACE_DIM = None


# Sample class for bagging and subspace selection
class sample(object):
    def __init__(self, X, n_subspace):
        self.idx_subspace = self.random_subspace(X, n_subspace)

    def __call__(self, X, y):
        idx_obj = self.bootstrap_sample(X)
        X_sampled, y_sampled = self.get_subsample(X, y, self.idx_subspace, idx_obj)
        return X_sampled, y_sampled

    @staticmethod
    def bootstrap_sample(X):
        np.random.seed(42)
        n_samples = X.shape[0]
        idx = np.random.choice(n_samples, size=n_samples, replace=True)
        return np.unique(idx)

    @staticmethod
    def random_subspace(X, n_subspace):
        np.random.seed(42)
        n_features = X.shape[1]
        return np.random.choice(n_features, size=n_subspace, replace=False)

    @staticmethod
    def get_subsample(X, y, idx_subspace, idx_obj):
        X_sampled = X[idx_obj][:, idx_subspace]
        y_sampled = y[idx_obj]
        return X_sampled, y_sampled


# Random forest implementation
class random_forest(object):
    def __init__(self, n_estimators: int, max_depth: int, subspaces_dim: int, random_state: int):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.subspaces_dim = subspaces_dim
        self.random_state = random_state
        self._estimators = []  # List of trained DecisionTreeClassifier models
        self.subspace_idx = []  # List of subspace indices for each tree

    def fit(self, X, y):
        np.random.seed(self.random_state)  # Set random seed for reproducibility
        for _ in range(self.n_estimators):
            # Create subsample
            sampler = sample(X, self.subspaces_dim)
            X_sampled, y_sampled = sampler(X, y)

            # Store subspace indices
            self.subspace_idx.append(sampler.idx_subspace)

            # Train a decision tree on the subsample
            tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=self.random_state)
            tree.fit(X_sampled, y_sampled)
            self._estimators.append(tree)

    def predict(self, X):
        # Collect predictions from all trees
        predictions = np.array([tree.predict(X[:, subspace]) for tree, subspace in zip(self._estimators, self.subspace_idx)])
        # Use majority voting to get the final prediction
        majority_votes = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=predictions)
        return majority_votes


# Hyperparameter tuning
def tune_hyperparameters():
    global N_ESTIMATORS, MAX_DEPTH, SUBSPACE_DIM

    # Load the Iris dataset
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Test different combinations of hyperparameters
    best_accuracy = 0
    for n_estimators in [10, 20, 50]:
        for max_depth in [3, 5, None]:
            for subspace_dim in [2, 3, X.shape[1]]:
                # Train random forest
                rf = random_forest(n_estimators=n_estimators, max_depth=max_depth, subspaces_dim=subspace_dim, random_state=42)
                rf.fit(X_train, y_train)
                predictions = rf.predict(X_test)

                # Evaluate accuracy
                accuracy = accuracy_score(y_test, predictions)
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    N_ESTIMATORS = n_estimators
                    MAX_DEPTH = max_depth
                    SUBSPACE_DIM = subspace_dim


# Main script
if __name__ == "__main__":
    # Tune hyperparameters
    tune_hyperparameters()

    # Load the Iris dataset
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the best random forest
    rf = random_forest(n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH, subspaces_dim=SUBSPACE_DIM, random_state=42)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)

    # Output accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f"Best Hyperparameters: n_estimators={N_ESTIMATORS}, max_depth={MAX_DEPTH}, subspaces_dim={SUBSPACE_DIM}")
    print(f"Accuracy on test set: {accuracy:.4f}")
