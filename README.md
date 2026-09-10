# ❤️ Heart Disease AI – Machine Learning Prediction

A Machine Learning web application that predicts the **risk of heart disease** based on various health-related parameters. The application is built using **Python, Scikit-learn, Pandas, NumPy, Joblib, and Streamlit**, with a custom CSS-based user interface.

---

## 🚀 Live Project

🌐 **Live Streamlit App:**  
https://heart-disease-prediction-project-al0r.onrender.com

💻 **GitHub Repository:**  
https://github.com/guptakrishna16767-sketch/Heart-Disease-Prediction-Project

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. This project uses **Machine Learning** to analyze patient health information and predict whether a person is likely to have heart disease.

The trained **Logistic Regression** model is integrated into an interactive **Streamlit web application**, where users can enter patient information and receive a heart disease risk prediction instantly.

The application also displays the **prediction probability**, risk status, patient summary, and prediction explanation through a customized user interface.

> ⚠️ This project is created for educational and demonstration purposes only and should not be used as a medical diagnosis tool.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical operations |
| **Scikit-learn** | Machine Learning |
| **Joblib** | Saving and loading trained models |
| **Streamlit** | Web application development |
| **CSS** | Custom user interface styling |
| **Jupyter Notebook** | Model development and experimentation |

---

## 📊 Dataset

The project uses a heart disease dataset containing **918 records and 12 columns**.

### Important Features

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


## 🔄 Machine Learning Workflow

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
Categorical Encoding
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Logistic Regression Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Web Application
   ↓
Patient Input
   ↓
Heart Disease Prediction
   ↓
Prediction Probability

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
Heart-Disease-Prediction-Project/
│
├── app.py
├── style.css
├── Healtcheakup.ipynb
├── heart.csv
│
├── LogisticRegression_heart.pkl
├── scaler.pkl
├── columns.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/guptakrishna16767-sketch/Heart-Disease-Prediction-Project.git
```

### 2. Navigate to the Project Folder

```bash
cd Heart-Disease-Prediction-Project
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

✅ Machine Learning based heart disease prediction
✅ Logistic Regression classification model
✅ Prediction probability
✅ Interactive Streamlit interface
✅ Custom CSS-based UI
✅ Patient health information form
✅ Prediction result popup
✅ Low-risk and high-risk indication
✅ Patient summary
✅ Risk progress indicator
✅ Model and scaler saved using Joblib
✅ Custom SVG assets
✅ Easy local setup
✅ Ready for online deployment
✅ Separate Streamlit and CSS files
---

## 📈 Future Improvements

The project can be improved further by adding:

🔹 Multiple Machine Learning algorithms
🔹 Model accuracy comparison
🔹 Random Forest and XGBoost models
🔹 ROC-AUC score
🔹 Confusion Matrix
🔹 Feature importance visualization
🔹 Interactive analytics dashboard
🔹 More health-related features
🔹 Improved model performance
🔹 Prediction history
🔹 User authentication
🔹 Cloud deployment improvements

---

## ⚠️ Disclaimer

This project is created for educational and demonstration purposes only.

The prediction generated by this application is not medical advice and should not be considered a medical diagnosis. Machine Learning predictions can contain errors and should not replace professional medical consultation.

If you have health concerns, please consult a qualified healthcare professional.

---

## 👨‍💻 Author

**Krishna Gupta**

BCA Student | Data Analytics & Machine Learning Enthusiast

### Skills

`Python` `Pandas` `NumPy` `Scikit-learn` `SQL` `Power BI` `Excel` `Streamlit`

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a **⭐ Star** on GitHub!
