import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.metrics import accuracy_score 
from sklearn.preprocessing import LabelEncoder 

file_names = [f"datasets/1.csv", f"datasets/2.csv", f"datasets/3.csv", f"datasets/4.csv", f"datasets/5.csv", f"datasets/6.csv"] 

datasets = [pd.read_csv(file_name, index_col=None) for file_name in file_names] 

def evaluate_kmeans(dataset, n_clusters): 
    if 'a0' in dataset.columns and 'a1' in dataset.columns: 
        X = dataset[['a0', 'a1']].values 
    elif 'x' in dataset.columns and 'y' in dataset.columns: 
        X = dataset[['x', 'y']].values 
    else: 
        raise ValueError("Не удалось найти столбцы с координатами 'x', 'y', 'a0', 'a1' в датасете.") 

    y_true = dataset.get('class') 
    if y_true is None: 
        y_true = dataset.get('label') or dataset.get('target') 

    if y_true is None: 
        raise ValueError("Не удалось найти столбец с метками классов.") 

    y_true = y_true.values 

    kmeans = KMeans(n_clusters=n_clusters, random_state=42) 
    kmeans.fit(X) 

    y_pred = kmeans.labels_ 

    le = LabelEncoder() 
    y_true_encoded = le.fit_transform(y_true) 

    cluster_mapping = {} 
    for cluster in np.unique(y_pred): 
        matching_class = np.bincount(y_true_encoded[y_pred == cluster]).argmax() 
        cluster_mapping[cluster] = matching_class 

    y_pred_corrected = np.array([cluster_mapping[cluster] for cluster in y_pred]) 

    accuracy = accuracy_score(y_true_encoded, y_pred_corrected) 

    plt.figure(figsize=(8, 6)) 
    plt.scatter(X[:, 0], X[:, 1], c=y_pred_corrected, cmap='viridis') 
    plt.title(f"K-Means Clustering (Accuracy: {accuracy:.2f})") 
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.show() 

    return accuracy 

results = [] 
for i, dataset in enumerate(datasets, start=1): 
    print(f"Датасет {i} содержит столбцы: {dataset.columns.tolist()}") 

    try: 
        n_clusters = len(dataset['class'].unique()) 
    except KeyError: 
        print(f"В датасете {i} отсутствует столбец с метками классов (например, 'class').") 
        continue 

    accuracy = evaluate_kmeans(dataset, n_clusters) 

    if accuracy > 0.9: 
        results.append(str(i)) 

print("Датасеты, для которых KMeans подходит:", ''.join(results))

#ОТВЕТ 246