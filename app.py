from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = data["value"]

    prediction = model.predict(np.array([[value]]))[0]

    label = "High" if prediction == 1 else "Low"

    return jsonify({
        "input": value,
        "prediction": label
    })

if __name__ == "__main__":
    app.run(debug=True)
