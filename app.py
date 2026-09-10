import streamlit as st
import pandas as pd
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
# LOAD CSS FROM style.css
# =========================================================

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


load_css()


# =========================================================
# POPUP FUNCTION
# =========================================================

@st.dialog("❤️ Heart Disease Prediction Result")
def show_prediction_popup(prediction, probability):

    # =====================================================
    # RISK RESULT
    # =====================================================

    if prediction == 1:

        st.markdown(
            """
            <div class="risk-result-box high-risk-box">
                ⚠️ HIGH RISK OF HEART DISEASE
            </div>
            """,
            unsafe_allow_html=True
        )

        description = (
            "The model predicts a higher risk based on "
            "the information provided."
        )

    else:

        st.markdown(
            """
            <div class="risk-result-box low-risk-box">
                ✅ LOW RISK OF HEART DISEASE
            </div>
            """,
            unsafe_allow_html=True
        )

        description = (
            "The model predicts a lower risk based on "
            "the information provided."
        )


    # =====================================================
    # DESCRIPTION BOX
    # =====================================================

    st.markdown(
        f"""
        <div class="prediction-description">
            {description}
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PROBABILITY BOX
    # =====================================================

    probability_html = (
        '<div class="probability-box">'
        '<p class="probability-title">'
        '❤️ Heart Disease Risk Probability'
        '</p>'
        '<p class="probability-value">'
        f'{probability:.2f}%'
        '</p>'
        '</div>'
    )

    st.markdown(
        probability_html,
        unsafe_allow_html=True
    )


    # =====================================================
    # PROGRESS BAR
    # =====================================================

    st.progress(
        min(
            max(
                probability / 100,
                0.0
            ),
            1.0
        )
    )


    # =====================================================
    # PROGRESS LABEL
    # =====================================================

    st.markdown(
        """
        <p class="popup-progress-label">
            Heart Disease Risk Probability
        </p>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # CLOSE BUTTON
    # =====================================================

    if st.button(
        "Close",
        use_container_width=True,
        key="close_prediction_popup"
    ):
        st.rerun()


# =========================================================
# TITLE
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

except Exception as e:

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

    st.exception(e)

    st.stop()


# =========================================================
# PATIENT INFORMATION
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
# INPUT FIELDS
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# COLUMN 1
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
# COLUMN 2
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
    # CREATE DATA
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

    df = pd.DataFrame([data])


    # =====================================================
    # MATCH MODEL COLUMNS
    # =====================================================

    for column in expected_columns:

        if column not in df.columns:

            df[column] = 0

    df = df[expected_columns]


    # =====================================================
    # SCALE
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


    # =====================================================
    # PROBABILITY
    # =====================================================

    probability = (
        model.predict_proba(
            df_scaled
        )[0][1] * 100
    )


    # =====================================================
    # SHOW POPUP
    # =====================================================

    show_prediction_popup(
        prediction,
        probability
    )


    # =====================================================
    # ORIGINAL RESULT
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
        <h2 class="result-title">
            📊 Prediction Result
        </h2>

        <p class="result-subtitle">
            AI-based heart disease risk analysis
        </p>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # RESULT
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
    # PROGRESS LABEL
    # =====================================================

    st.markdown(
        """
        <p class="risk-probability-label">
            Risk Probability
        </p>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        min(
            max(
                probability / 100,
                0.0
            ),
            1.0
        )
    )


    # =====================================================
    # PATIENT SUMMARY
    # =====================================================

    st.markdown(
        """
        <h3 class="patient-summary-title">
            👤 Patient Summary
        </h3>
        """,
        unsafe_allow_html=True
    )


    summary1, summary2, summary3 = st.columns(3)


    # =====================================================
    # SUMMARY 1
    # =====================================================

    with summary1:

        st.metric(
            "Age",
            f"{age}"
        )

        st.metric(
            "Blood Pressure",
            f"{resting_bp}"
        )


    # =====================================================
    # SUMMARY 2
    # =====================================================

    with summary2:

        st.metric(
            "Cholesterol",
            f"{cholesterol}"
        )

        st.metric(
            "Maximum HR",
            f"{max_hr}"
        )


    # =====================================================
    # SUMMARY 3
    # =====================================================

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
