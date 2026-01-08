🚔 Crime Rate Prediction System using Machine Learning
📌 Project Overview

The Crime Rate Prediction System is a Machine Learning–based project that analyzes historical crime data to predict future crime trends.
This system helps understand crime patterns across different locations and crime types, which can support decision-making for safety planning and awareness.

The project demonstrates how data preprocessing, model training, and deployment using Flask API work together in a real-world ML application.

🎯 Objectives

Analyze historical crime data

Predict crime rates based on past trends

Build a trained Machine Learning model

Deploy the model using a Flask REST API

Enable predictions through API requests

🛠️ Technologies Used

Programming Language: Python

Machine Learning: Scikit-learn

Data Handling: Pandas, NumPy

Model Saving: Joblib

Backend API: Flask

API Testing: Postman / Browser

Deployment Ready: Render / Localhost

📂 Project Structure
Crime-Rate-Prediction/
│
├── dataset/
│   └── crime_data.csv
│
├── model/
│   ├── crime_model.pkl
│   ├── le_city.pkl
│   └── le_crime.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

⚙️ How the System Works

Historical crime data is collected and cleaned

Categorical data (city, crime type) is encoded

A Machine Learning model is trained

The trained model is saved using Joblib

Flask API loads the model

User sends input data through API

System predicts the crime rate

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/crime-rate-prediction.git
cd crime-rate-prediction

2️⃣ Install Required Libraries
pip install -r requirements.txt

3️⃣ Train the Model (Optional)
python train_model.py

4️⃣ Run the Flask Application
python app.py


Server will start at:

http://127.0.0.1:5000

🔍 API Usage Example
Endpoint
POST /predict

Sample JSON Input
{
  "city": "Assam",
  "crime_type": "Theft",
  "year": 2024
}

Sample Output
{
  "predicted_crime_rate": 742
}

📊 Dataset Description

City – Name of the city/state

Crime Type – Type of crime (Theft, Robbery, Assault, etc.)

Year – Crime occurrence year

Crime Count – Number of crimes reported

The dataset is used only for educational and learning purposes.

✅ Key Features

✔ Simple and beginner-friendly
✔ Machine Learning based prediction
✔ Flask REST API integration
✔ Scalable for future enhancements
✔ Suitable for academic mini/major projects

🔮 Future Enhancements

Add frontend UI (HTML/CSS/JavaScript)

Use real-time crime datasets

Improve accuracy with advanced ML models

Add location-based crime visualization

Deploy with database integration
