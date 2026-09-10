❤️ Heart Disease AI – Machine Learning Prediction

A Machine Learning web application that predicts the risk of heart disease based on patient health-related parameters. The application is built using Python, Scikit-learn, Pandas, Joblib, and Streamlit with a custom CSS-based user interface.

🚀 Live Project

🌐 Streamlit App: https://heart-disease-prediction-project-al0r.onrender.com

💻 GitHub Repository: https://github.com/guptakrishna16767-sketch/Heart-Disease-Prediction-Project

📌 Project Overview

Heart disease is one of the major health concerns worldwide. This project uses Machine Learning to analyze different patient health parameters and predict the possibility of heart disease.

The trained Logistic Regression model is integrated with an interactive Streamlit web application. Users can enter patient information and receive a heart disease risk prediction along with the predicted probability.

⚠️ This application is developed for educational and demonstration purposes and should not be used as a medical diagnosis tool.

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data manipulation and preprocessing
NumPy	Numerical operations
Scikit-learn	Machine Learning model
Joblib	Saving and loading trained models
Streamlit	Web application development
CSS	Custom application styling
Jupyter Notebook	Data analysis and model development
📊 Dataset

The project uses a heart disease dataset containing 918 records and 12 columns.

Dataset Features
Feature	Description
Age	Age of the patient
Sex	Gender of the patient
ChestPainType	Type of chest pain
RestingBP	Resting blood pressure
Cholesterol	Cholesterol level
FastingBS	Fasting blood sugar
RestingECG	Resting ECG results
MaxHR	Maximum heart rate
ExerciseAngina	Exercise-induced angina
Oldpeak	ST depression
ST_Slope	Slope of the ST segment
HeartDisease	Target variable
Target Variable
0 → No Heart Disease
1 → Heart Disease
🔄 Machine Learning Workflow
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
Save Model & Preprocessing Files
   ↓
Streamlit Web Application
   ↓
Patient Input
   ↓
Heart Disease Risk Prediction
   ↓
Prediction Probability
🤖 Machine Learning Model

The project uses Logistic Regression, a classification algorithm suitable for binary classification problems.

The model predicts two possible outcomes:

0 → Low Risk / No Heart Disease
1 → High Risk / Heart Disease

The trained model and preprocessing components are saved using Joblib.

Saved Model Files
LogisticRegression_heart.pkl – Trained Logistic Regression model
scaler.pkl – Feature scaling object
columns.pkl – Expected feature columns
🌐 Streamlit Application

The application provides an interactive interface where users can enter the following information:

👤 Age
⚧️ Gender
❤️ Chest Pain Type
🩸 Resting Blood Pressure
🧪 Cholesterol
🩸 Fasting Blood Sugar
📈 Resting ECG
❤️ Maximum Heart Rate
🏃 Exercise Angina
📉 Oldpeak
📊 ST Slope

After clicking Predict Heart Disease, the application displays:

Prediction result
Heart disease risk probability
Risk progress indicator
Patient information summary
Prediction explanation
Educational disclaimer
🎨 User Interface

The application uses a custom dark-themed UI with a separate CSS stylesheet.

UI Features

✅ Dark modern interface
✅ Custom CSS styling
✅ Patient input card
✅ Interactive form controls
✅ Prediction result popup
✅ Risk probability display
✅ Low-risk / High-risk indication
✅ Patient summary
✅ Responsive Streamlit layout

The application separates the Python/Streamlit logic from the CSS styling, making the project easier to maintain and modify.

📁 Project Structure
Heart-Disease-ML-Project/
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
File Description
File	Description
app.py	Main Streamlit application
style.css	Custom CSS styling
Healtcheakup.ipynb	Data analysis and ML model development
heart.csv	Heart disease dataset
LogisticRegression_heart.pkl	Trained ML model
scaler.pkl	Feature scaler
columns.pkl	Expected model columns
requirements.txt	Required Python libraries
README.md	Project documentation
.gitignore	Git ignored files
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/guptakrishna16767-sketch/Heart-Disease-ML-Project.git
2. Navigate to the Project Folder
cd Heart-Disease-ML-Project
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Streamlit Application
streamlit run app.py

The application will open automatically in your web browser.

If Streamlit is not recognized in PowerShell, use:

python -m streamlit run app.py
📦 Requirements

The project requires the following Python libraries:

streamlit
pandas
numpy
scikit-learn
joblib
🎯 Key Features
✅ Machine Learning based heart disease prediction
✅ Logistic Regression classification model
✅ Prediction probability
✅ Interactive Streamlit interface
✅ Custom CSS-based UI
✅ Patient health information form
✅ Risk prediction popup
✅ Patient summary
✅ Model and scaler saved using Joblib
✅ Easy local setup
✅ Ready for online deployment
✅ Separate Streamlit and CSS files
📈 Future Improvements

The project can be improved further by adding:

🔹 Multiple Machine Learning algorithms
🔹 Model accuracy comparison
🔹 Random Forest and XGBoost models
🔹 ROC-AUC and confusion matrix
🔹 Feature importance visualization
🔹 Interactive analytics dashboard
🔹 More advanced health-related features
🔹 Improved model performance
🔹 Cloud deployment
🔹 User authentication
🔹 Prediction history
⚠️ Disclaimer

This project is created for educational and demonstration purposes only.

The prediction generated by this application is not medical advice and should not be considered a medical diagnosis. Machine Learning predictions can contain errors and should not replace professional medical consultation.

If you have health concerns, please consult a qualified healthcare professional.

👨‍💻 Author

Krishna Gupta

BCA Student | Data Analytics & Machine Learning Enthusiast

Skills
Python
Pandas
NumPy
Scikit-learn
SQL
Power BI
Excel
Streamlit
Machine Learning
Data Analysis
⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ Star on GitHub.

Your support is appreciated! ❤️

🔗 Project Links

GitHub:
https://github.com/guptakrishna16767-sketch/Heart-Disease-ML-Project

Live Demo:
https://heart-disease-prediction-project-al0r.onrender.com

Author:
Krishna Gupta
