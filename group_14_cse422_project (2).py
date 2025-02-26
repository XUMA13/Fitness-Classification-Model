# -*- coding: utf-8 -*-
"""Group-14_CSE422-Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Djwc_uF_MUrxpKTUNxKfb-VU66gszIJo
"""

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE
# from sklearn.impute import SimpleImputer

## Loading dataset
df = pd.read_csv('/content/health_fitness_dataset.csv')
df_sampled = df.sample(n=10000, random_state=42)
df_sampled.to_csv('downsampled_dataset.csv', index=False)
data = pd.read_csv('downsampled_dataset.csv')
data.shape
data['health_condition'] = data['health_condition'].replace([None], "NoDisease")



sns.set_theme(style="whitegrid")


## 1. Dataset Overview
data.shape
overview_info = data.info()
# overview_head = data.head()



## 2. Bar Chart of N classes from target

target_counts = data['health_condition'].value_counts()
print(target_counts)

plt.figure(figsize=(10, 6))
sns.countplot(x='health_condition', data= data, palette="viridis")
plt.title('Target Column Distribution (Health Condition)', fontsize=16)
plt.xlabel('Health Condition', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()


## Step 1: Handle Missing or Faulty Data

missing_values = data.isnull().sum()
# print(missing_values)                         # no relevant missing values (since target has renamed the class "None ")


data = data.dropna(subset=['health_condition'])  # dropping 'health_condition' (target variable)

## Step 2: Encode Categorical Variables

categorical_columns = ['gender', 'activity_type', 'intensity', 'smoking_status']    #Label Encoder
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le


## Step 3: Feature Selection

features = data.drop(columns=['participant_id', 'date', 'health_condition'])  #target and non-numeric and irrelevant in predicting the target
target = data['health_condition']

# Encoding the target variable
target_encoder = LabelEncoder()
target = target_encoder.fit_transform(target)

overview_head = data.head()
print(overview_head)

# Step 4: Correlation Analysis
plt.figure(figsize=(12, 8))
correlation_matrix = features.corr()
sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm")
plt.title("Feature Correlation Heatmap", fontsize=16)
plt.show()

# Step 5: Addressing Imbalance in Target Variable

smote = SMOTE(random_state=42)                # Applying SMOTE to balance the dataset to avoid biasness towards majority
X_resampled, y_resampled = smote.fit_resample(features, target)

# Step 6: Dataset Splitting (stratified 70:30)
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled ,test_size=0.3, random_state= 42, stratify= y_resampled)

# Step 7: Feature Scaling (using standard scaler)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 8: Model Training and Testing

models = {
    'Decision Tree': DecisionTreeClassifier(random_state= 42),
    'Random Forest': RandomForestClassifier(random_state= 42),
    'K-Nearest Neighbors': KNeighborsClassifier()
}

results = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_encoder.classes_)
    results[model_name] = {
        'accuracy': accuracy,
        'classification_report': report,
        'confusion_matrix': confusion_matrix(y_test, y_pred)
    }

# Step 9: Displaying Results
for model_name, result in results.items():
    print(f"\nModel: {model_name}")
    print(f"Accuracy: {result['accuracy']:.2f}")
    print("Classification Report:\n", result['classification_report'])
    print("Confusion Matrix:\n", result['confusion_matrix'])

# Visualizing Model Accuracy
model_accuracies = {model_name: result['accuracy'] for model_name, result in results.items()}
plt.figure(figsize=(10, 6))
sns.barplot(x=list(model_accuracies.keys()), y=list(model_accuracies.values()), palette="viridis")
plt.title("Model Accuracy Comparison", fontsize=16)
plt.xlabel("Model", fontsize=14)
plt.ylabel("Accuracy", fontsize=14)
plt.ylim(0, 1)
plt.show()