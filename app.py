from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ML API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    value = data.get("value", 0)
    
    if value > 50:
        result = "High"
    else:
        result = "Low"
        
    return jsonify({
        "input": value,
        "prediction": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
