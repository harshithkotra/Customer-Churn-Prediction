import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="🏦",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background:#F4F8FB;
}

.main-title{
    text-align:center;
    font-size:44px;
    color:#0A3D62;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:20px;
    margin-bottom:25px;
}

div.stButton > button{
    background:#0A3D62;
    color:white;
    border:none;
    border-radius:10px;
    height:55px;
    width:100%;
    font-size:20px;
    font-weight:bold;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:12px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:16px;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    "<div class='main-title'>🏦 Customer Churn Prediction Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Powered Banking Analytics System</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# LAYOUT
# ==========================================================

left_col, right_col = st.columns([1.5,1])

# ==========================================================
# CUSTOMER DETAILS
# ==========================================================

with left_col:

    st.subheader("📋 Customer Details")

    col1,col2 = st.columns(2)

    with col1:

        credit = st.number_input(
            "Credit Score",
            300,
            900,
            650
        )

        geo = st.selectbox(
            "Geography",
            ["France","Germany","Spain"]
        )

        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        age = st.number_input(
            "Age",
            18,
            100,
            35
        )

        tenure = st.number_input(
            "Tenure",
            0,
            10,
            5
        )

    with col2:

        balance = st.number_input(
            "Balance",
            value=50000.0
        )

        products = st.selectbox(
            "Number Of Products",
            [1,2,3,4]
        )

        card = st.selectbox(
            "Has Credit Card",
            ["Yes","No"]
        )

        active = st.selectbox(
            "Is Active Member",
            ["Yes","No"]
        )

        salary = st.number_input(
            "Estimated Salary",
            value=60000.0
        )

    predict = st.button(
        "🔍 Predict Customer",
        use_container_width=True
    )

# ==========================================================
# RIGHT PANEL
# ==========================================================

with right_col:

    st.subheader("📊 Prediction Summary")

    prediction_box = st.empty()

    probability_box = st.empty()

    risk_box = st.empty()

    progress_box = st.empty()
# ==========================================================
# CONNECT TO FASTAPI
# ==========================================================

if predict:

    payload = {

        "CreditScore": int(credit),
        "Geography": geo,
        "Gender": gender,
        "Age": int(age),
        "Tenure": int(tenure),
        "Balance": float(balance),
        "NumOfProducts": int(products),
        "HasCrCard": 1 if card == "Yes" else 0,
        "IsActiveMember": 1 if active == "Yes" else 0,
        "EstimatedSalary": float(salary)

    }
    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code != 200:
            st.error("Prediction Failed!")
            st.write(response.text)
            st.stop()

        result = response.json()

        prediction = result["prediction"]
        probability = result["churn_probability"]
        risk = result["risk_level"]

        # =====================================================
        # RIGHT PANEL OUTPUT
        # =====================================================

        if prediction == 1:
            prediction_box.error("🔴 Customer Likely To Churn")
        else:
            prediction_box.success("🟢 Customer Not Likely To Churn")

        probability_box.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        risk_box.metric(
            "Risk Level",
            risk
        )

        progress_box.progress(float(probability))

        # =====================================================
        # ANALYTICS
        # =====================================================

        st.markdown("---")

        st.header("📈 Customer Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:

            fig = go.Figure(data=[

                go.Pie(

                    labels=["Churn","Stay"],

                    values=[
                        probability*100,
                        100-(probability*100)
                    ],

                    hole=0.65

                )

            ])

            fig.update_layout(
                title="Customer Churn Probability"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with chart2:

            feature_df = pd.DataFrame({

                "Feature":[
                    "Credit Score",
                    "Age",
                    "Balance",
                    "Salary",
                    "Products"
                ],

                "Value":[
                    credit,
                    age,
                    balance/1000,
                    salary/1000,
                    products*20
                ]

            })

            fig2 = px.bar(

                feature_df,

                x="Feature",

                y="Value",

                text="Value",

                color="Feature"

            )

            fig2.update_layout(
                title="Customer Profile"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )
        # =====================================================
        # CUSTOMER INFORMATION
        # =====================================================

        st.markdown("---")

        st.header("📋 Customer Information")

        info1, info2 = st.columns(2)

        with info1:

            st.write(f"**Credit Score:** {credit}")
            st.write(f"**Geography:** {geo}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Age:** {age}")
            st.write(f"**Tenure:** {tenure}")

        with info2:

            st.write(f"**Balance:** ₹{balance:,.2f}")
            st.write(f"**Products:** {products}")
            st.write(f"**Credit Card:** {card}")
            st.write(f"**Active Member:** {active}")
            st.write(f"**Estimated Salary:** ₹{salary:,.2f}")

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        st.markdown("---")

        st.header("🧠 AI Recommendation")

        if probability < 0.30:

            st.success("""
### ✅ Low Risk Customer

This customer has a low probability of churn.

**Recommended Actions**
- Continue providing quality service.
- Offer premium banking products.
- Maintain regular engagement.
""")

        elif probability < 0.70:

            st.warning("""
### ⚠️ Medium Risk Customer

This customer has a moderate probability of churn.

**Recommended Actions**
- Send personalized offers.
- Increase customer engagement.
- Provide loyalty rewards.
""")

        else:

            st.error("""
### 🚨 High Risk Customer

This customer has a high probability of churn.

**Recommended Actions**
- Contact the customer immediately.
- Provide exclusive retention offers.
- Assign a relationship manager.
""")

        st.markdown("---")

        st.info(
            f"🕒 Prediction generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

    except Exception as e:

        st.error("❌ Unable to connect to FastAPI Server.")

        st.write(e)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px;color:gray;">
<h4>🏦 Customer Churn Prediction System</h4>
<p>Developed by <b>Harshith Kotra</b></p>
<p>Machine Learning • FastAPI • Streamlit • Plotly</p>
</div>
""",
unsafe_allow_html=True
)