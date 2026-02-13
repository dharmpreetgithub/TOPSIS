import streamlit as st
import pandas as pd
import numpy as np

# 1️⃣ FIRST define topsis function

def topsis(input_file, weights, impacts, output_file):
    ...
    full function code
    ...

# 2️⃣ THEN Streamlit UI code

st.title("TOPSIS Decision Making Tool")

uploaded_file = st.file_uploader(...)

weights = st.text_input(...)
impacts = st.text_input(...)

if st.button("Run TOPSIS"):
    ...
    topsis("temp.csv", weights, impacts, "output.csv")
