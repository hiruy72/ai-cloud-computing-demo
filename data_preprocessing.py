# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


data = {
    'Name': ['Hiruy', 'Abiy', 'Ameha', 'Beakal', None],
    'Age': [20, 22, 21, None, 23],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'Score': [88, 76, 95, 65, 70]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


df['Age'].fillna(df['Age'].mean(), inplace=True)


df['Name'].fillna('Unknown', inplace=True)
print("\nAfter Handling Missing Values:\n", df)



X = df[['Name', 'Age', 'Gender']]  
y = df['Score']                     
print("\nFeatures:\n", X)
print("\nTarget:\n", y)

categorical_features = ['Name', 'Gender']
numerical_features = ['Age']


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),     
        ('cat', OneHotEncoder(), categorical_features)     
    ]
)


pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])


X_processed = pipeline.fit_transform(X)
print("\nProcessed Features (NumPy array):\n", X_processed)

X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.3, random_state=42
)
print("\nTraining features shape:", X_train.shape)
print("Test features shape:", X_test.shape)
