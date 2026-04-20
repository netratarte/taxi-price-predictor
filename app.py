from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_form", methods=["POST"])
def predict_form():
    distance = float(request.form["distance"])
    duration = float(request.form["duration"])

    data = {
        "distance": distance,
        "duration": duration
    }

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    for col in columns:
        if col not in df:
            df[col] = 0

    df = df[columns]

    prediction = model.predict(df)[0]

    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)