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

st.title("Monitoreo de Operaciones")

# Creating two tabs: Visualization and Editing
tab1, tab2 = st.tabs(["Visualización", "Edición"])

with tab1:

    st.header("Visualización de Datos")

    if st.button("Actualizar Vista"):
        df = load_excel(file_path)
        st.success("Datos actualizados correctamente!")
    
        
    # Filtering options
    st.sidebar.header("Filter Data")
    columns = st.sidebar.multiselect("Select columns to filter by:", options=df.columns)
    filtered_df = df.copy()

    
    for column in columns:
        unique_values = filtered_df[column].unique()
        selected_values = st.sidebar.multiselect(f"Filter by {column}:", options=unique_values)
        filtered_df = filtered_df[filtered_df[column].isin(selected_values)]
    
    st.subheader("Conteo de Registros y Suma de un Campo Numérico")
    record_count = filtered_df.shape[0]
    st.write(f"Total de registros: {record_count}")

    st.write("Filtered Data Preview:")
    st.dataframe(filtered_df, use_container_width=True)

with tab2:
    st.header("Editar Datos")

    # Data editor
    edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

    # Button to save changes
    if st.button("Guardar Cambios"):
        # Update the original dataframe with the edited data
        df.update(edited_df)
        save_excel(df, file_path)
        st.success("Cambios guardados exitosamente!")
