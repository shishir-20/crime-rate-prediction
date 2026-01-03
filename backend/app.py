from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model/crime_model.pkl")
le_city = joblib.load("model/le_city.pkl")
le_crime = joblib.load("model/le_crime.pkl")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/CrimesOnWomenData.csv")
df = df.drop(columns=["Unnamed: 0"])

crime_types = ["Rape", "Theft", "Assault", "Robbery", "Fraud"]
cities = sorted(df["State"].unique().tolist())
years = sorted(df["Year"].unique().tolist())

# ---------------- META API ----------------
@app.route("/api/meta", methods=["GET"])
def meta():
    return jsonify({
        "cities": cities,
        "years": years,
        "crime_types": crime_types
    })

# ---------------- PREDICT API ----------------
@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.json

    city = data.get("city")
    year = int(data.get("year"))
    crime = data.get("crime_type")

    city_enc = le_city.transform([city])[0]
    crime_enc = le_crime.transform([crime])[0]

    pred = model.predict([[city_enc, year, crime_enc]])
    prediction = max(0, int(pred[0]))

    if prediction <= 200:
        risk = "Low Risk"
    elif prediction <= 500:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    return jsonify({
        "prediction": prediction,
        "risk_level": risk
    })

# ---------------- RANKING API ----------------
@app.route("/api/ranking", methods=["GET"])
def ranking():
    crime = request.args.get("crime_type")
    year = int(request.args.get("year"))

    filtered = df[df["Year"] == year][["State", crime]]

    grouped = (
        filtered.groupby("State")[crime]
        .sum()
        .reset_index()
        .rename(columns={crime: "Count"})
        .sort_values(by="Count", ascending=False)
    )

    return jsonify(grouped.to_dict("records"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
