import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("data/house_prices.csv")

model = load_model()
df = load_data()
X = df.drop("Price", axis=1)

st.title("🏠 House Price Prediction")
st.write("Enter property details to estimate the house price.")

inputs = {}
cols = st.columns(2)

numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

with cols[0]:
    st.subheader("Property Details")
    for feature in numeric_features:
        inputs[feature] = st.number_input(
            feature,
            value=float(X[feature].median()),
            step=1.0
        )

with cols[1]:
    st.subheader("Category Details")
    for feature in categorical_features:
        options = X[feature].dropna().unique().tolist()
        inputs[feature] = st.selectbox(feature, options)

input_df = pd.DataFrame([inputs])[X.columns]

if st.button("🔮 Predict House Price", type="primary", use_container_width=True):
    prediction = model.predict(input_df)[0]
    st.success("Prediction completed successfully!")
    st.metric("Estimated House Price", f"₹{prediction:,.0f}")

with st.expander("📊 Dataset Preview"):
    st.write(f"Records: {len(df):,}")
    st.dataframe(df.head(20), use_container_width=True)
