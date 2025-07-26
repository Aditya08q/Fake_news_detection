import joblib
import streamlit as st

model = joblib.load("model.pkl")

st.title("Fake News Detection App")
user_input = st.text_area("Enter News Text:", height=300)

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == "FAKE":
            st.error(" This news is FAKE.")
        else:
            st.success("This news is REAL.")
