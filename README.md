# ✈️ FlightIQ: AI-Powered Flight Price Intelligence Platform

Predict flight ticket prices using Machine Learning and access predictions through a FastAPI-powered REST API.

---

## 📌 Overview

FlightIQ is an end-to-end Machine Learning project designed to estimate airline ticket prices based on flight details such as airline, source, destination, journey date, duration, and number of stops.

The project demonstrates the complete ML workflow—from data preprocessing and feature engineering to model training and API deployment—making it suitable for real-world prediction services.

---

## 🚀 Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Random Forest Regression Model
- Model Serialization using Pickle
- REST API using FastAPI
- Interactive API Documentation (Swagger UI)
- Modular Project Structure
- Version Controlled using Git & GitHub

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API Framework | FastAPI |
| Notebook | Jupyter Notebook |
| Model Storage | Pickle |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
FlightIQ-AI-Price-Intelligence/
│
├── api/
│   └── main.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── flights_processed.csv
│
├── models/
│   └── flight_price_model.pkl
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   └── 02_Model_Training.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Machine Learning Workflow

### Step 1
Data Collection

- Flight Fare Dataset

### Step 2
Data Cleaning

- Missing value handling
- Duplicate removal
- Data formatting

### Step 3
Feature Engineering

Examples include:

- Journey Day
- Journey Month
- Departure Hour
- Arrival Hour
- Total Stops
- Duration

### Step 4
Model Training

Model Used:

- Random Forest Regressor

### Step 5
Model Saving

The trained model is serialized using Pickle for deployment.

### Step 6
API Deployment

Predictions are served through a FastAPI REST API.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/femin6666/FlightIQ-AI-Price-Intelligence.git
```

Navigate to the project

```bash
cd FlightIQ-AI-Price-Intelligence
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn api.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Model Pipeline

```
Flight Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
Random Forest Model
      │
      ▼
Model Evaluation
      │
      ▼
Pickle Model
      │
      ▼
FastAPI
      │
      ▼
Price Prediction
```

---

## 💡 Future Enhancements

- Compare multiple ML algorithms
- Hyperparameter tuning
- Streamlit web application
- Explainable AI (Feature Importance)
- Interactive analytics dashboard
- Cloud deployment
- Real-time flight fare integration

---

## 📚 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Regression Modeling
- REST API Development
- Model Deployment
- Git & GitHub
- Python Programming

---

## 👩‍💻 Author

**Femina**

Aspiring Machine Learning Engineer passionate about building intelligent, data-driven applications that solve real-world problems.

---

## ⭐ If you found this project useful, consider giving it a star!
