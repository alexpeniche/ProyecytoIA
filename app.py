import streamlit as st
import pandas as pd

# Function to load the Excel file
def load_excel(file_path):
    return pd.read_excel(file_path)

# Function to save the edited DataFrame back to the Excel file
def save_excel(df, file_path):
    df.to_excel(file_path, index=False)

# Load the file
file_path = "archivo_consolidado 1.xlsx"
df = load_excel(file_path)

st.title("Data Editor with Streamlit")

# Filtering options
st.sidebar.header("Filter Data")
columns = st.sidebar.multiselect("Select columns to filter by:", options=df.columns)
filtered_df = df.copy()

for column in columns:
    unique_values = filtered_df[column].unique()
    selected_values = st.sidebar.multiselect(f"Filter by {column}:", options=unique_values, default=unique_values)
    filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

# Data editor
st.header("Edit Data")
edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

# Button to save changes
if st.button("Save Changes"):
    save_excel(edited_df, file_path)
    st.success("Changes saved successfully!")

st.write("Data preview:")
st.dataframe(edited_df)
