#ссылка на ноутбук: https://colab.research.google.com/drive/11I_gwSaEkG-qGdp8J8vpH9ELSnKtHeJJ?usp=sharing

#ПРОРЕШАННЫЙ НОУТБУК

import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = datasets.load_breast_cancer()
X, y = data.data, data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

def compare_svm_kernels(X_train, X_test, y_train, y_test):
    """
    This function trains SVM models with different kernels and evaluates them on the test set
    to determine the best performing kernel.
    """
    kernels = ['linear', 'poly', 'rbf', 'sigmoid']
    best_kernel = None
    best_score = 0
    
    for kernel in kernels:
        # Train an SVM model with the specified kernel
        model = SVC(kernel=kernel, random_state=42)
        model.fit(X_train, y_train)
        
        # Predict on the test set
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        score = accuracy_score(y_test, y_pred)
        print(f"Kernel: {kernel}, Accuracy: {score}")
        
        # Update best kernel if the current one has a higher score
        if score > best_score:
            best_score = score
            best_kernel = kernel
    
    print(f"\nBest Kernel: {best_kernel}, Best Accuracy: {best_score}")

# Run the function to compare kernels
compare_svm_kernels(X_train, X_test, y_train, y_test)

#ответ: rbf (МАЛЕНЬКИМИ БУКВАМИ)