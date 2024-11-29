import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fetal_health.csv")

st.title("Exploratory Data Analysis")

st.write("This page is for exploratory data analysis of the fetal health dataset.")

st.write("First lets look at the data samples and its description")
st.write(df.head())
st.write(df.describe())

st.markerdown("""
The data consists of 2126 rows with 21 features and a target variable 'fetal health'. 
The features are related to fetal health parameters such as fetal movement, uterine contractions, and accelerations.
""")