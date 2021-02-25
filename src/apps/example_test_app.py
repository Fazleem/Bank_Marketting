import streamlit as st
import pandas as pd
import numpy as np

# from prettytable import PrettyTable


st.title("Bank Marketting App")

# DATE_COLUMN = "date/time"
# DATA_URL = (
#     "https://s3-us-west-2.amazonaws.com/"
#     "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
# )

Dataset = "/home/fazleem/Desktop/DataScience/bank_marketting/data/raw/bank-full.csv"


@st.cache
# def load_data(nrows):
#     data = pd.read_csv(Dataset, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis="columns", inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


def load_data(nrows):
    data = pd.read_csv(Dataset, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

# select dataset - sidebar
dataset_name = st.sidebar.selectbox("Select Dataset", ("Bank_Marketting", "Default"))
st.write(f"## {dataset_name} Dataset")

# select classifier
classifier_name = st.sidebar.selectbox(
    "Select classifier", ("Random Forest", "Deep Learning")
)
