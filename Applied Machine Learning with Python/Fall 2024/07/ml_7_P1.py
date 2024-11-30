import numpy as np

class sample(object):
    def __init__(self, X, n_subspace):
        # Select random subspace (features) during initialization
        self.idx_subspace = self.random_subspace(X, n_subspace)

    def __call__(self, X, y):
        # Perform bagging to get indices of objects
        idx_obj = self.bootstrap_sample(X)
        # Use indices to get the subsample
        X_sampled, y_sampled = self.get_subsample(X, y, self.idx_subspace, idx_obj)
        return X_sampled, y_sampled

    @staticmethod
    def bootstrap_sample(X):
        """
        Generate a random sub-sample of object indices using bagging.
        Each object can be selected multiple times (with replacement).
        Duplicate removal ensures unique indices in the final output.
        """
        np.random.seed(42)  # For reproducibility
        n_samples = X.shape[0]
        idx = np.random.choice(n_samples, size=n_samples, replace=True)
        return np.unique(idx)  # Remove duplicates to meet task requirements

    @staticmethod
    def random_subspace(X, n_subspace):
        """
        Select a random subspace (subset of features) without replacement.
        """
        np.random.seed(42)  # For reproducibility
        n_features = X.shape[1]
        return np.random.choice(n_features, size=n_subspace, replace=False)

    @staticmethod
    def get_subsample(X, y, idx_subspace, idx_obj):
        """
        Create a subsample of X and y using the selected features (idx_subspace)
        and objects (idx_obj).
        """
        X_sampled = X[idx_obj][:, idx_subspace]  # Subset rows and columns
        y_sampled = y[idx_obj]  # Subset corresponding targets
        return X_sampled, y_sampled
