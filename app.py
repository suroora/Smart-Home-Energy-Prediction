from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "energy_model.pkl")

# Load model
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expected features in this demo: T1, RH_1, T_out, Windspeed, lights
        features = [
            float(request.form.get("T1", 0)),
            float(request.form.get("RH_1", 0)),
            float(request.form.get("T_out", 0)),
            float(request.form.get("Windspeed", 0)),
            float(request.form.get("lights", 0))
        ]
        arr = np.array([features])
        pred = model.predict(arr)[0]
        return render_template("index.html", prediction_text=f"Predicted Appliances Energy (Wh): {pred:.2f}", values=request.form)
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    # For local debugging; in Docker we'll run via flask command or gunicorn
    app.run(host="0.0.0.0", port=5000, debug=True)
