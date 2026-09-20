import streamlit as st
import pandas as pd
import pickle


# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="wide"
)


# -----------------------------------------
# LOAD MODEL
# -----------------------------------------

with open("diamond_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("feature_columns.pkl", "rb") as file:
    feature_columns = pickle.load(file)


# -----------------------------------------
# TITLE
# -----------------------------------------

st.title("💎 Diamond Price Prediction")

st.write(
    "Enter the diamond details below to predict its estimated price."
)


# -----------------------------------------
# USER INPUTS
# -----------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    carat = st.number_input(
        "Carat",
        min_value=0.1,
        max_value=5.0,
        value=1.0
    )

    depth = st.number_input(
        "Depth",
        min_value=40.0,
        max_value=80.0,
        value=60.0
    )

    table = st.number_input(
        "Table",
        min_value=40.0,
        max_value=80.0,
        value=55.0
    )


with col2:

    x = st.number_input(
        "X (Length)",
        min_value=0.0,
        max_value=15.0,
        value=5.0
    )

    y = st.number_input(
        "Y (Width)",
        min_value=0.0,
        max_value=15.0,
        value=5.0
    )

    z = st.number_input(
        "Z (Depth)",
        min_value=0.0,
        max_value=15.0,
        value=3.0
    )


with col3:

    cut = st.selectbox(
        "Cut",
        ["Fair", "Good", "Very Good", "Premium", "Ideal"]
    )

    color = st.selectbox(
        "Color",
        ["D", "E", "F", "G", "H", "I", "J"]
    )

    clarity = st.selectbox(
        "Clarity",
        ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    )


# -----------------------------------------
# CREATE INPUT DATA
# -----------------------------------------

input_data = pd.DataFrame({
    "carat": [carat],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity]
})


# -----------------------------------------
# ENCODING
# -----------------------------------------

input_encoded = pd.get_dummies(
    input_data,
    columns=["cut", "color", "clarity"],
    drop_first=True
)


# -----------------------------------------
# MATCH TRAINING COLUMNS
# -----------------------------------------

input_encoded = input_encoded.reindex(
    columns=feature_columns,
    fill_value=0
)


# -----------------------------------------
# PREDICTION
# -----------------------------------------

if st.button("💎 Predict Diamond Price"):

    prediction = model.predict(input_encoded)

    st.success(
        f"Estimated Diamond Price: ${prediction[0]:,.2f}"
    )