# 🏦 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a bank customer is likely to churn. This project uses a trained Machine Learning model, a FastAPI backend, and a Streamlit frontend to provide real-time predictions.

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by banks. This application predicts whether a customer is likely to leave the bank based on customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Member Status
- Estimated Salary

The prediction is displayed with:

- Churn Probability
- Risk Level
- Customer Analytics
- AI Recommendation

---

## 🚀 Features

- Machine Learning Churn Prediction
- FastAPI REST API
- Streamlit Interactive Dashboard
- Customer Analytics Charts
- AI-Based Recommendations
- Real-time Prediction
- Professional Banking Dashboard

---

## 🛠 Technologies Used

- Python
- Scikit-learn
- FastAPI
- Streamlit
- Plotly
- Pandas
- NumPy
- Joblib
- Requests

---

## 📂 Project Structure

```
PROJECT 1
│
├── app
│   └── main.py
│
├── frontend
│   └── streamlit_app.py
│
├── model
│   ├── churn_model.pkl
│   ├── churn_pipeline.pkl
│   └── scaler.pkl
│
├── data
│   └── Churn.csv
│
├── Dockerfile
├── requirements.txt
├── README.md
└── train_model.py
```

---

## ▶️ Running the Project

### Clone the Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

### Start Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🌐 API Endpoints

### Health Check

```
GET /health
```

Returns the server status.

### Predict Customer Churn

```
POST /predict
```

Returns:

- Prediction
- Churn Probability
- Risk Level

---

## 📊 Dashboard

The Streamlit dashboard provides:

- Customer Input Form
- Prediction Summary
- Churn Probability
- Customer Analytics
- AI Recommendation
- Customer Information

---

## 🎯 Future Improvements

- Deploy using Docker
- Deploy on Render
- Add User Authentication
- Store Prediction History
- Improve Model Accuracy

---

## 👨‍💻 Author

**Harshith Kotra**

Machine Learning | Python | FastAPI | Streamlit

---

## 📜 License

This project is developed for educational purposes.