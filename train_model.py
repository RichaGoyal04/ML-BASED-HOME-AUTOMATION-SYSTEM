import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# dataset load
data = pd.read_csv("dataset.csv")

# features and labels
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestClassifier()

# training
model.fit(X_train, y_train)

# accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# save model
with open("gesture_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as gesture_model.pkl")