#ссылка на ноутбук https://colab.research.google.com/drive/1QvQVLjJsmyXplhHGyYo50FWr4ZPs73Wo?usp=sharing

#ПРОРЕШАННЫЙ НОУТЮУК
import numpy as np

np.random.seed(42)

class LinearRegression:
    def __init__(self, **kwargs):
        # Initialize the coefficients as None, will be set in the fit method
        self.coef_ = None

    def fit(self, x: np.array, y: np.array):
        """
        Fit the linear regression model to the training data.
        x: 2D numpy array (num_samples, num_features) - feature matrix
        y: 1D numpy array (num_samples,) - target values
        """
        # Add bias term to x by appending a column of 1s
        x_bias = np.hstack([np.ones((x.shape[0], 1)), x])
        
        # Calculate the coefficients using the Normal Equation
        self.coef_ = np.linalg.inv(x_bias.T @ x_bias) @ x_bias.T @ y

    def predict(self, x: np.array):
        """
        Predict using the linear regression model.
        x: 2D numpy array (num_samples, num_features) - feature matrix
        Returns: 1D numpy array - predicted values
        """
        # Add bias term to x by appending a column of 1s
        x_bias = np.hstack([np.ones((x.shape[0], 1)), x])
        
        # Return the dot product of the input features with the coefficients
        return x_bias @ self.coef_
