# ❤️ Heart Disease Prediction

A Machine Learning web application that predicts the possibility of **heart disease** based on various health-related parameters. The application is built using **Python, Scikit-learn, Pandas, and Streamlit**.

## 🚀 Live Project

**Streamlit App:** Add your deployed Streamlit link here

**GitHub Repository:** Add your GitHub repository link here

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. This project uses Machine Learning to analyze patient health information and predict whether a person is likely to have heart disease.

The trained Machine Learning model is integrated into an interactive **Streamlit web application**, where users can enter patient information and get a prediction instantly.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine Learning
* **Joblib** – Saving and loading the trained model
* **Streamlit** – Web application
* **Jupyter Notebook** – Model development and experimentation

---

## 📊 Dataset

The project uses a heart disease dataset containing **918 records and 12 columns**.

### Important Features

| Feature        | Description             |
| -------------- | ----------------------- |
| Age            | Age of the patient      |
| Sex            | Gender of the patient   |
| ChestPainType  | Type of chest pain      |
| RestingBP      | Resting blood pressure  |
| Cholesterol    | Cholesterol level       |
| FastingBS      | Fasting blood sugar     |
| RestingECG     | Resting ECG results     |
| MaxHR          | Maximum heart rate      |
| ExerciseAngina | Exercise-induced angina |
| Oldpeak        | ST depression           |
| ST_Slope       | Slope of the ST segment |
| HeartDisease   | Target variable         |

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
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Web App
   ↓
Heart Disease Prediction
```

---

## 🤖 Machine Learning Model

The project uses a classification-based Machine Learning approach to predict the target variable:

* `0` → No Heart Disease
* `1` → Heart Disease

The trained model is saved using **Joblib** and loaded into the Streamlit application for making predictions.

---

## 🌐 Streamlit Application

The web application provides a simple and user-friendly interface where users can enter:

* Age
* Gender
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Angina
* Oldpeak
* ST Slope

After entering the information, the application displays the predicted result.

---

## 📁 Project Structure

```text
heart_disease/
│
├── app.py
├── Healtcheakup.ipynb
├── heart.csv
├── heart_disease_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd heart_disease
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 🎯 Key Features

✅ Machine Learning based prediction
✅ Interactive Streamlit interface
✅ User-friendly input form
✅ Fast prediction
✅ Trained model saved using Joblib
✅ Responsive and attractive UI
✅ Easy to deploy online

---

## 📈 Future Improvements

* Improve model accuracy using advanced algorithms
* Add multiple Machine Learning models
* Display prediction probability
* Add data visualization
* Add model performance metrics
* Deploy the application using Streamlit Cloud
* Add more health-related features

---

## ⚠️ Disclaimer

This project is created for **educational and demonstration purposes only**. The prediction should not be considered medical advice or a medical diagnosis. Always consult a qualified healthcare professional for medical concerns.

---

## 👨‍💻 Author

**Krishna Gupta**

BCA Student | Data Analytics & Machine Learning Enthusiast

### Skills

`Python` `Pandas` `NumPy` `Scikit-learn` `SQL` `Power BI` `Excel` `Streamlit`

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a **⭐ Star** on GitHub!
