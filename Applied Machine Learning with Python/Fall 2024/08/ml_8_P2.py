#ссылка на ноутбук https://colab.research.google.com/drive/1Js4hMmNQeMb0grkC3wgHS-8QZcNyEG5X#scrollTo=rjX6v8Y8uImZ

#НЕПРАВИЛЬНО ПРОРЕШАННЫЙ НОУТБУК (ДРИМ-ТИМ ИЗ КАТИ, МЕНЯ И ЧАТГПТ 4О НЕ СМОГЛИ ЗАСТАВИТЬ ЕГО ВЫВЕСТИ ПРАВИЛЬНЫЙ ОТВЕТ, ОТВЕТ ПОЛУЧЕН ПЕРЕБОРОМ)
 
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score

# Load dataset
data = fetch_openml(data_id=42608)
X, y = data['data'].drop(columns='Outcome').values, data['data']['Outcome'].astype(int).values

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit and transform on training data
X_test = scaler.transform(X_test)       # Only transform on test data

# Define models
models = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'SVC': SVC(probability=True, random_state=42)
}

# Evaluate models
roc_auc_scores = {}
pr_auc_scores = {}

for model_name, model in models.items():
    # Train model
    model.fit(X_train, y_train)
    # Predict probabilities for the positive class
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    # Calculate metrics
    roc_auc_scores[model_name] = roc_auc_score(y_test, y_pred_proba)
    pr_auc_scores[model_name] = average_precision_score(y_test, y_pred_proba)

# Find the best models for each metric
best_roc_model = max(roc_auc_scores, key=roc_auc_scores.get)
best_pr_model = max(pr_auc_scores, key=pr_auc_scores.get)

# Map model names to their indices
model_indices = {
    'Decision Tree': 1,
    'Logistic Regression': 2,
    'KNN': 3,
    'SVC': 4
}

roc_model_index = model_indices[best_roc_model]
pr_model_index = model_indices[best_pr_model]

# Generate the result
result = f"{roc_model_index}{pr_model_index}"

# Print the result and scores
print(result)
print("ROC AUC Scores:", roc_auc_scores)
print("PR AUC Scores:", pr_auc_scores)
 
#ОТВЕТ 21
