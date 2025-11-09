from sklearn.linear_model import LinearRegression
import numpy as np  

# Features and target
x = np.array([2,4,6,8,10]).reshape(-1,1)
y = np.array([1,2,3,4,5])

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predict for new data
print(model.predict([[6]]))
