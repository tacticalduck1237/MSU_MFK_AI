import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
from sklearn.metrics import confusion_matrix
# Load datasets
data_files = ["/home/doomer/Downloads/drive-download-20241214T192835Z-001/1.csv","/home/doomer/Downloads/drive-download-20241214T192835Z-001/2.csv","/home/doomer/Downloads/drive-download-20241214T192835Z-001/3.csv","/home/doomer/Downloads/drive-download-20241214T192835Z-001/4.csv","/home/doomer/Downloads/drive-download-20241214T192835Z-001/5.csv","/home/doomer/Downloads/drive-download-20241214T192835Z-001/6.csv"]  # Example filenames
def load_data(file):
    data = pd.read_csv(file, index_col=None)
    return data

def evaluate_kmeans(data, n_clusters):
    X = data.iloc[:, :2].values
    y_true = data.iloc[:, 2].values

    # Fit KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    y_pred = kmeans.fit_predict(X)

    # Visualize
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', s=50, label='Predicted Clusters')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroids')
    plt.title(f'Dataset with {n_clusters} Clusters')
    plt.legend()
    plt.show()

    # Match predicted labels to true labels
    cm = confusion_matrix(y_true, y_pred)
    row_ind, col_ind = linear_sum_assignment(-cm)
    accuracy = cm[row_ind, col_ind].sum() / y_true.size

    return accuracy >= 0.9

# Process each dataset and determine if KMeans is suitable
suitable_datasets = ''
for idx, file in enumerate(data_files, start=1):
    data = load_data(file)
    n_clusters = len(data.iloc[:, 2].unique())
    is_suitable = evaluate_kmeans(data, n_clusters)

    if is_suitable:
        suitable_datasets += str(idx)

print("Suitable datasets for KMeans:", suitable_datasets)