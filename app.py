import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   APP BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(6, 182, 212, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 95% 5%,
            rgba(139, 92, 246, 0.20),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #0f172a 50%,
            #111827 100%
        );
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.block-container {
    max-width: 900px;
    padding-top: 35px;
    padding-bottom: 50px;
}


/* =====================================================
   HEADINGS
   ===================================================== */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #ffffff !important;
}


/* =====================================================
   HEADER
   ===================================================== */

.title {
    text-align: center;
    font-size: 46px;
    font-weight: 900;
    color: #ffffff !important;
    margin-bottom: 5px;

    text-shadow:
        0 0 15px rgba(34, 211, 238, 0.45);
}


.subtitle {
    text-align: center;
    color: #cbd5e1 !important;
    font-size: 17px;
    margin-bottom: 32px;
}


/* =====================================================
   CARD
   ===================================================== */

.card {
    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 42, 0.97),
            rgba(30, 41, 59, 0.90)
        );

    padding: 30px;

    border-radius: 22px;

    border: 1px solid rgba(56, 189, 248, 0.28);

    box-shadow:
        0 20px 50px rgba(0, 0, 0, 0.45);

    backdrop-filter: blur(15px);
}


/* =====================================================
   LABELS
   ===================================================== */

.stNumberInput label,
.stSelectbox label {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}


/* =====================================================
   NUMBER INPUT
   ===================================================== */

div[data-testid="stNumberInput"] {
    color: #ffffff !important;
}


/* Input box */

div[data-baseweb="input"] {
    background-color: #1e293b !important;

    border: 1px solid #475569 !important;

    border-radius: 12px !important;
}


/* Input text */

div[data-baseweb="input"] input {
    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;

    background-color: #1e293b !important;

    font-size: 15px !important;

    font-weight: 600 !important;

    caret-color: #22d3ee !important;
}


/* Input focus */

div[data-baseweb="input"]:focus-within {
    border-color: #22d3ee !important;

    box-shadow:
        0 0 12px rgba(34, 211, 238, 0.25) !important;
}


/* =====================================================
   NUMBER INPUT BUTTONS
   ===================================================== */

div[data-testid="stNumberInput"] button {
    background-color: #1e293b !important;

    color: #ffffff !important;

    border: none !important;
}


div[data-testid="stNumberInput"] button svg {
    fill: #ffffff !important;

    color: #ffffff !important;
}


div[data-testid="stNumberInput"] button:hover {
    background-color: #334155 !important;
}


/* =====================================================
   SELECTBOX
   ===================================================== */

/* Selectbox label */

div[data-testid="stSelectbox"] label {
    color: #ffffff !important;
    font-weight: 700 !important;
}


/* Main selectbox */

div[data-testid="stSelectbox"]
div[data-baseweb="select"] {

    color: #ffffff !important;

    background-color: #1e293b !important;

    border-radius: 12px !important;
}


/* Selectbox inner container */

div[data-testid="stSelectbox"]
div[data-baseweb="select"] > div {

    background-color: #1e293b !important;

    border: 1px solid #475569 !important;

    border-radius: 12px !important;

    color: #ffffff !important;
}


/* =====================================================
   SELECTED VALUE - IMPORTANT
   ===================================================== */

div[data-testid="stSelectbox"]
div[data-baseweb="select"]
span {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;

    font-weight: 600 !important;
}


/* Combobox text */

div[data-testid="stSelectbox"]
[role="combobox"] {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


/* Everything inside selectbox */

div[data-testid="stSelectbox"]
div[data-baseweb="select"] * {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


/* Selectbox arrow */

div[data-testid="stSelectbox"]
div[data-baseweb="select"] svg {

    fill: #ffffff !important;

    color: #ffffff !important;
}


/* =====================================================
   DROPDOWN MENU
   ===================================================== */

div[data-baseweb="popover"] {

    background-color: #1e293b !important;
}


div[data-baseweb="popover"] * {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


div[data-baseweb="popover"] ul {

    background-color: #1e293b !important;
}


div[data-baseweb="popover"] li {

    background-color: #1e293b !important;

    color: #ffffff !important;
}


div[data-baseweb="popover"] li span {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


/* Dropdown hover */

div[data-baseweb="popover"] li:hover {

    background-color: #334155 !important;
}


/* Selected dropdown option */

div[data-baseweb="popover"]
li[aria-selected="true"] {

    background-color: #2563eb !important;

    color: #ffffff !important;
}


div[data-baseweb="popover"]
li[aria-selected="true"] span {

    color: #ffffff !important;
}


/* =====================================================
   PREDICT BUTTON
   ===================================================== */

.stButton > button {

    width: 100%;

    height: 58px;

    border: none;

    border-radius: 15px;

    background:
        linear-gradient(
            90deg,
            #06b6d4,
            #2563eb,
            #7c3aed
        ) !important;

    color: #ffffff !important;

    font-size: 18px;

    font-weight: 800;

    box-shadow:
        0 8px 25px rgba(37, 99, 235, 0.35);

    transition: all 0.3s ease;
}


.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 35px rgba(56, 189, 248, 0.40);
}


.stButton > button p,
.stButton > button span {

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


/* =====================================================
   METRIC
   ===================================================== */

[data-testid="stMetric"] {

    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.95)
        ) !important;

    padding: 20px;

    border-radius: 16px;

    border: 1px solid rgba(56, 189, 248, 0.25);

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.25);
}


[data-testid="stMetricLabel"] {

    color: #cbd5e1 !important;
}


[data-testid="stMetricValue"] {

    color: #22d3ee !important;

    font-weight: 800 !important;
}


/* =====================================================
   ALERTS
   ===================================================== */

div[data-testid="stAlert"] {

    border-radius: 15px;
}


div[data-testid="stAlert"] p {

    color: #ffffff !important;
}


/* =====================================================
   PROGRESS BAR
   ===================================================== */

div[data-testid="stProgress"] > div {

    background-color: #1e293b !important;

    border-radius: 20px;
}


/* =====================================================
   DIVIDER
   ===================================================== */

hr {

    border-color:
        rgba(148, 163, 184, 0.20) !important;
}


/* =====================================================
   SCROLLBAR
   ===================================================== */

::-webkit-scrollbar {
    width: 8px;
}


::-webkit-scrollbar-track {
    background: #020617;
}


::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 10px;
}


::-webkit-scrollbar-thumb:hover {
    background: #22d3ee;
}


/* =====================================================
   HIDE MENU
   ===================================================== */

#MainMenu {
    visibility: hidden;
}


footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">❤️ Heart Disease AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Heart Disease Risk Prediction'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL
# =========================================================

try:

    model = joblib.load(
        "LogisticRegression_heart.pkl"
    )

    scaler = joblib.load(
        "scaler.pkl"
    )

    expected_columns = joblib.load(
        "columns.pkl"
    )

except Exception:

    st.error(
        "❌ Model files could not be loaded."
    )

    st.info(
        """
        Make sure these files are in the same folder
        as app.py:

        • LogisticRegression_heart.pkl
        • scaler.pkl
        • columns.pkl
        """
    )

    st.stop()


# =========================================================
# PATIENT INFORMATION CARD
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    "### 👤 Patient Information"
)

st.markdown(
    "Enter the patient's medical information below."
)

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


# =========================================================
# INPUTS
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=40,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["M", "F"],
        key="sex"
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"],
        key="chest_pain"
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        min_value=80,
        max_value=200,
        value=120,
        step=1
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=100,
        max_value=600,
        value=200,
        step=1
    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120",
        [0, 1],
        key="fasting_bs"
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"],
        key="resting_ecg"
    )

    max_hr = st.number_input(
        "Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150,
        step=1
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        ["Y", "N"],
        key="exercise_angina"
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=6.0,
        value=1.0,
        step=0.1
    )


# =========================================================
# ST SLOPE
# =========================================================

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"],
    key="st_slope"
)


st.markdown(
    "<br>",
    unsafe_allow_html=True
)


# =========================================================
# PREDICT BUTTON
# =========================================================

predict = st.button(
    "🔍  Predict Heart Disease"
)


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    # =====================================================
    # CREATE INPUT DATA
    # =====================================================

    data = {

        "Age": age,

        "RestingBP": resting_bp,

        "Cholesterol": cholesterol,

        "FastingBS": fasting_bs,

        "MaxHR": max_hr,

        "Oldpeak": oldpeak,

        "Sex_" + sex: 1,

        "ChestPainType_" + chest_pain: 1,

        "RestingECG_" + resting_ecg: 1,

        "ExerciseAngina_" + exercise_angina: 1,

        "ST_Slope_" + st_slope: 1
    }


    # =====================================================
    # DATAFRAME
    # =====================================================

    df = pd.DataFrame([data])


    # =====================================================
    # ADD MISSING COLUMNS
    # =====================================================

    for column in expected_columns:

        if column not in df.columns:

            df[column] = 0


    # =====================================================
    # CORRECT COLUMN ORDER
    # =====================================================

    df = df[expected_columns]


    # =====================================================
    # SCALE DATA
    # =====================================================

    try:

        df_scaled = scaler.transform(df)

    except Exception as e:

        st.error(
            "❌ Error while scaling the input data."
        )

        st.exception(e)

        st.stop()


    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(
        df_scaled
    )[0]


    probability = (
        model.predict_proba(
            df_scaled
        )[0][1] * 100
    )


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
        <h2 style="
            text-align:center;
            color:#ffffff !important;
            margin-bottom:5px;
        ">
            📊 Prediction Result
        </h2>

        <p style="
            text-align:center;
            color:#94a3b8 !important;
            margin-bottom:25px;
        ">
            AI-based heart disease risk analysis
        </p>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # RESULT STATUS
    # =====================================================

    if prediction == 1:

        st.error(
            "⚠️ High Risk of Heart Disease"
        )

    else:

        st.success(
            "✅ Low Risk of Heart Disease"
        )


    # =====================================================
    # PROBABILITY
    # =====================================================

    st.metric(
        "❤️ Heart Disease Risk Probability",
        f"{probability:.2f}%"
    )


    # =====================================================
    # PROGRESS BAR
    # =====================================================

    st.markdown(
        """
        <p style="
            color:#cbd5e1 !important;
            font-weight:700;
            margin-top:20px;
            margin-bottom:5px;
        ">
            Risk Probability
        </p>
        """,
        unsafe_allow_html=True
    )


    st.progress(
        min(max(probability / 100, 0.0), 1.0)
    )


    # =====================================================
    # PATIENT SUMMARY
    # =====================================================

    st.markdown(
        """
        <h3 style="
            color:#ffffff !important;
            margin-top:30px;
        ">
            👤 Patient Summary
        </h3>
        """,
        unsafe_allow_html=True
    )


    summary1, summary2, summary3 = st.columns(3)


    with summary1:

        st.metric(
            "Age",
            f"{age}"
        )

        st.metric(
            "Blood Pressure",
            f"{resting_bp}"
        )


    with summary2:

        st.metric(
            "Cholesterol",
            f"{cholesterol}"
        )

        st.metric(
            "Maximum HR",
            f"{max_hr}"
        )


    with summary3:

        st.metric(
            "Oldpeak",
            f"{oldpeak:.1f}"
        )

        st.metric(
            "Fasting BS",
            f"{fasting_bs}"
        )


    # =====================================================
    # MODEL INFORMATION
    # =====================================================

    st.info(
        """
        🤖 **About This Prediction**

        This application uses a Logistic Regression machine
        learning model to estimate heart disease risk from
        the information provided.
        """
    )


    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.warning(
        "⚠️ This application is for educational purposes only "
        "and should not replace professional medical advice."
    )
