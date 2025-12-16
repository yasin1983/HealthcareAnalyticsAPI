# Healthcare Analytics API

## 📌 Overview
A prototype healthcare analytics system built with Python and Flask.  
The API loads a trained Random Forest model and provides predictions on patient risk levels.  
This project is part of a larger Big Data pipeline concept using Apache Spark, Hadoop, and Hive.

## 🛠 Tech Stack
- Python (Flask, Pandas, scikit-learn, Joblib)
- REST API for predictions
- Big Data (Apache Spark, Hadoop, Hive) [conceptual extension]

## 🚀 How to Run
```bash
pip install -r requirements.txt
python app.py

```

##📤 Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "Age": 60,
  "Billing_Amount": 25000,
  "Length_of_Stay": 7,
  "Gender": "Male",
  "Medical_Condition": "ConditionA",
  "Admission_Type": "Emergency",
  "Test_Results": "Test1"
}'

```

##📥 Example Response

```bash
{
  "risk_prediction": "Diabetes",
  "probabilities": [0.14, 0.16, 0.23, 0.24, 0.12, 0.11]
}
```
## 📂 Project Structure

HealthcareAPI/
│
├── app.py                # Flask API entry point
├── requirements.txt      # Python dependencies
├── models/               # ML models (excluded via .gitignore if large)
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates for dashboard
└── README.md             # Project documentation


## 📈 Future Work
- Integrate with Apache Spark for distributed data processing

- Store patient records in Hadoop/Hive for scalable analytics

- Extend model with clustering + classification for risk stratification

## 📜 License
This project is licensed under the MIT License.






