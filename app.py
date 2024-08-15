
import streamlit as st
import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('archivo_consolidado 1.xlsx')

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Operaciones", "Auditoría", "Monitoreo Servidores", "APIs"])

with tab1:
    st.header("Vista de Operaciones")
    
    # Crear filtros para cada columna del DataFrame
    filters = {}
    for col in df.columns:
        unique_values = df[col].dropna().unique()  # Valores únicos, excluyendo NaN
        selected_values = st.multiselect(f'Selecciona valores para {col}:', options=unique_values)
        if selected_values:
            filters[col] = selected_values

    # Aplicar los filtros al DataFrame
    df_filtered = df.copy()
    for col, selected_values in filters.items():
        df_filtered = df_filtered[df_filtered[col].isin(selected_values)]

    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtered)

with tab2:
    st.header("Vista de Auditoría")
    st.write("Aquí puedes agregar contenido relacionado con la auditoría.")

with tab3:
    st.header("Monitoreo de Servidores")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de servidores.")

with tab4:
    st.header("Monitoreo de APIs")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de APIs.")
