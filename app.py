from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/")
def home():
    return "Taxi Price Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Convert input to dataframe
    df = pd.DataFrame([data])

    # Convert to same format as training
    df = pd.get_dummies(df)

    # Add missing columns
    for col in columns:
        if col not in df:
            df[col] = 0

    df = df[columns]

    prediction = model.predict(df)

    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)