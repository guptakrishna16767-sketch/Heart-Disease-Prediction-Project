# ❤️ Heart Disease AI

A Machine Learning web application that predicts the risk of **heart disease** based on various health-related parameters. The application is built using **Python, Pandas, Scikit-learn, Joblib, and Streamlit**.

---

## 🚀 Live Project

**🌐 Streamlit App:**  
Add your deployed Streamlit application link here

**💻 GitHub Repository:**  
Add your GitHub repository link here

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. This project uses Machine Learning to analyze patient health information and predict the possibility of heart disease.

The trained **Logistic Regression** model is integrated into an interactive Streamlit web application. Users can enter health-related information and receive a heart disease risk prediction along with the predicted probability.

> ⚠️ This application is intended for educational and demonstration purposes only and should not be used as a medical diagnosis tool.

---

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Scikit-learn** – Machine Learning
- **Joblib** – Saving and loading trained ML models
- **Streamlit** – Interactive web application
- **Jupyter Notebook** – Model development and experimentation

---

## 📊 Dataset

The project uses a heart disease dataset containing **918 records and 12 columns**.

### Dataset Features

| Feature | Description |
|---|---|
| `Age` | Age of the patient |
| `Sex` | Gender of the patient |
| `ChestPainType` | Type of chest pain |
| `RestingBP` | Resting blood pressure |
| `Cholesterol` | Cholesterol level |
| `FastingBS` | Fasting blood sugar |
| `RestingECG` | Resting ECG results |
| `MaxHR` | Maximum heart rate |
| `ExerciseAngina` | Exercise-induced angina |
| `Oldpeak` | ST depression |
| `ST_Slope` | Slope of the ST segment |
| `HeartDisease` | Target variable |

### Target Variable

- `0` → No Heart Disease
- `1` → Heart Disease

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Encoding Categorical Features
   ↓
Feature Scaling
   ↓
Train-Test Split
   ↓
Logistic Regression Model
   ↓
Model Evaluation
   ↓
Save Model using Joblib
   ↓
Streamlit Application
   ↓
Heart Disease Risk Prediction
