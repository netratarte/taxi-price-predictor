import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("taxi_trip_pricing.csv")

print("Columns are:", df.columns)

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 🔥 IMPORTANT: automatically select last column as target
target = df.columns[-1]
print("Using target column:", target)

X = df.drop(target, axis=1)
y = df[target]

# Convert categorical columns
X = pd.get_dummies(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ SUCCESS: model.pkl created")
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))