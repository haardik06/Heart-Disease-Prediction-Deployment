from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

# -------------------------------
# Initialize Flask Application
# -------------------------------

app = Flask(__name__)

# -------------------------------
# Load Trained Model
# -------------------------------

model = joblib.load("model.pkl")

# -------------------------------
# Home Route
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Prediction Route
# -------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        features = np.array([[
            float(data["age"]),
            float(data["sex"]),
            float(data["cp"]),
            float(data["trestbps"]),
            float(data["chol"]),
            float(data["fbs"]),
            float(data["restecg"]),
            float(data["thalach"]),
            float(data["exang"]),
            float(data["oldpeak"]),
            float(data["slope"]),
            float(data["ca"]),
            float(data["thal"])
        ]])

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0]

        confidence = round(max(probability) * 100, 2)

        if prediction == 1:

            result = "Heart Disease Detected"

        else:

            result = "No Heart Disease"

        return jsonify({

            "prediction": result,

            "confidence": confidence

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 400


# -------------------------------
# Run Flask App
# -------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )