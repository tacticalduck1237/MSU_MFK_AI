import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.utils import shuffle
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Step 1: Load the dataset
# Replace 'your_dataset_url' with the actual URL to the dataset
df = pd.read_csv('TRAIN.csv')

# Step 2: Preprocess the data
# Remove the redundant index column
df = df.drop(columns=["ccccc"])  # Replace 'index_column_name' with the actual name of the index column

# Label encoding for categorical columns ("cut", "color", "clarity")
categorical_columns = ["cut", "color", "clarity"]
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# One-hot encoding for the categorical features
df = pd.get_dummies(df, columns=categorical_columns)

# Shuffle the dataset
df = shuffle(df, random_state=42)

# Separate features and target variable
X = df.drop(columns=['price'])  # Replace 'price' with the actual target column name
y = df['price']                 # Target column (price)

# Step 3: Define hyperparameters for the Decision Tree
param_grid = [
    {"criterion": "squared_error", "max_depth": 12},
    {"criterion": "friedman_mse", "max_depth": 16},
    {"criterion": "poisson", "max_depth": 22},
    {"criterion": "squared_error", "max_depth": 45},
    {"criterion": "friedman_mse", "max_depth": 95},
    {"criterion": "poisson", "max_depth": 33}
]

# Step 4: Train and evaluate using cross-validation
best_score = -float("inf")
best_params = None

for params in param_grid:
    regressor = DecisionTreeRegressor(random_state=42, **params)
    scores = cross_val_score(regressor, X, y, cv=10, scoring="r2")
    mean_score = scores.mean()
    
    if mean_score > best_score:
        best_score = mean_score
        best_params = params

print("Best hyperparameters:", best_params)
print("Best R^2 score:", best_score)

#Best hyperparameters: {'criterion': 'squared_error', 'max_depth': 12}
#Best R^2 score: 0.9720803345599475