import streamlit as st
import pandas as pd
import numpy as np
from topsis import topsis

st.title("TOPSIS Decision Making Tool")

st.write("Upload a CSV file and provide weights and impacts.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

weights = st.text_input("Enter Weights (comma separated)", "1,1,1,1")
impacts = st.text_input("Enter Impacts (comma separated)", "+,+,+,+")

if st.button("Run TOPSIS"):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        data.to_csv("temp.csv", index=False)
        
        topsis("temp.csv", weights, impacts, "output.csv")
        
        result = pd.read_csv("output.csv")
        st.success("TOPSIS Calculated Successfully!")
        st.dataframe(result)
        
        st.download_button(
            label="Download Result",
            data=result.to_csv(index=False),
            file_name="output.csv",
            mime="text/csv"
        )
    else:
        st.error("Please upload a CSV file.")

