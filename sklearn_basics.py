from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Example data
# X = study hours, y = test scores
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([40, 50, 60, 65, 70, 75, 85])

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Display results
print("Predictions:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict a new value
new_hours = np.array([[8]])
predicted_score = model.predict(new_hours)
print(f"Predicted score for 8 study hours: {predicted_score[0]:.2f}")
