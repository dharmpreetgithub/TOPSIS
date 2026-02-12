import streamlit as st
import pandas as pd
import numpy as np

def basic_topsis(input_file, weights, impacts):

    data = pd.read_csv(input_file)

    decision_matrix = data.iloc[:, 1:]

    # Normalize
    norm = decision_matrix / np.sqrt((decision_matrix**2).sum())

    # Convert weights
    weights = np.array(weights)

    weighted_matrix = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data['Topsis Score'] = score
    data['Rank'] = score.rank(ascending=False)

    return data

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

