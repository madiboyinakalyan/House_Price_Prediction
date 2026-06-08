import os
import joblib
import numpy as np
import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="House Price AI",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# 🎨 PREMIUM UI STYLE
# -----------------------------
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}

/* Hero Section */
.hero {
    padding: 40px 20px;
    border-radius: 15px;
    background: linear-gradient(90deg, #0f172a, #1e3a8a);
    margin-bottom: 25px;
}

/* Title */
.hero h1 {
    font-size: 48px;
    font-weight: 800;
    color: #ffffff;
}

/* Subtitle */
.hero p {
    font-size: 18px;
    color: #cbd5f5;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.06);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 20px;
}

/* Section Headings */
h3 {
    color: #22d3ee !important;
    font-weight: 700;
}

/* Labels */
label {
    color: #e2e8f0 !important;
    font-weight: 500;
}

/* Inputs */
input, select {
    border-radius: 8px !important;
    background-color: #020617 !important;
    color: #ffffff !important;
}

/* Dropdown text */
div[data-baseweb="select"] span {
    color: white !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #22d3ee, #6366f1);
    transform: scale(1.03);
}

/* Result Box */
.result {
    background: linear-gradient(90deg, #6366f1, #ec4899);
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(
    os.path.join(BASE_DIR, "..", "models", "linear_regression_model.pkl")
)

model = joblib.load(model_path)

# -----------------------------
# UTIL FUNCTIONS
# -----------------------------
def yn(val):
    return 1 if val == "Yes" else 0

def format_indian_currency(num):
    num = float(num)
    if num >= 10000000:
        return f"{num/10000000:.2f} Crore"
    elif num >= 100000:
        return f"{num/100000:.2f} Lakh"
    else:
        return f"{num:,.2f}"

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🏠 Smart Property Valuation</h1>
    <p>AI-powered house price prediction system</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# LAYOUT
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# LEFT COLUMN
# -----------------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏡 Property Core")

    area = st.number_input("Area (sqft)", value=1000)
    bedrooms = st.number_input("Bedrooms", value=2)
    parking = st.number_input("Parking Spaces", value=1)
    resale = st.selectbox("Resale", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏢 Building Features")

    security = st.selectbox("24x7 Security", ["No", "Yes"])
    power = st.selectbox("Power Backup", ["No", "Yes"])
    lift = st.selectbox("Lift Available", ["No", "Yes"])
    maintenance = st.selectbox("Maintenance Staff", ["No", "Yes"])
    rain = st.selectbox("Rain Water Harvesting", ["No", "Yes"])
    vaastu = st.selectbox("Vaastu Compliant", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# RIGHT COLUMN
# -----------------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏠 Interior")

    intercom = st.selectbox("Intercom", ["No", "Yes"])
    staff = st.selectbox("Staff Quarter", ["No", "Yes"])
    gas = st.selectbox("Gas Connection", ["No", "Yes"])
    ac = st.selectbox("AC", ["No", "Yes"])
    wifi = st.selectbox("WiFi", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛋️ Furnishing")

    play = st.selectbox("Children Play Area", ["No", "Yes"])
    wash = st.selectbox("Washing Machine", ["No", "Yes"])
    dining = st.selectbox("Dining Table", ["No", "Yes"])
    wardrobe = st.selectbox("Wardrobe", ["No", "Yes"])
    fridge = st.selectbox("Refrigerator", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# INPUT ARRAY (20 FEATURES)
# -----------------------------
input_data = np.array([[
    area,
    bedrooms,
    yn(resale),
    parking,
    yn(security),
    yn(power),
    yn(lift),
    yn(maintenance),
    yn(rain),
    yn(vaastu),
    yn(intercom),
    yn(staff),
    yn(gas),
    yn(ac),
    yn(wifi),
    yn(play),
    yn(wash),
    yn(dining),
    yn(wardrobe),
    yn(fridge)
]])

# -----------------------------
# PREDICT
# -----------------------------
st.divider()

if st.button("🚀 Predict Price"):
    prediction = model.predict(input_data)
    formatted_price = format_indian_currency(prediction[0])

    st.markdown(f"""
    <div class="result">
        💰 Estimated Price: ₹ {formatted_price}
        <br><small>(₹ {prediction[0]:,.2f})</small>
    </div>
    """, unsafe_allow_html=True)