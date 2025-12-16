from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Model ve feature kolonlarını yükle
rf_model = joblib.load("rf_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df_input = pd.DataFrame([data])
    
    # One-hot encoding
    df_input = pd.get_dummies(df_input)
    for col in feature_columns:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[feature_columns]
    
    prediction = rf_model.predict(df_input)[0]
    probabilities = rf_model.predict_proba(df_input)[0].tolist()
    
    return jsonify({
        "risk_prediction": prediction,
        "probabilities": probabilities
    })

if __name__ == "__main__":
    app.run(debug=True)
