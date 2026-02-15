import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Create simple dataset
X = np.array([[10], [20], [30], [40], [50], [60], [70], [80]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")
