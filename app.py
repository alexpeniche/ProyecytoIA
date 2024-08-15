import streamlit as st
import pandas as pd

# Función para cargar el archivo Excel desde SharePoint (simulada aquí)
def load_excel():
    df = pd.read_excel('archivo_consolidado 1.xlsx')
    return df

# Función para guardar el archivo Excel de vuelta en SharePoint (simulada aquí)
def save_excel(df):
    df.to_excel('archivo_consolidado 1.xlsx', index=False)

# Cargar el archivo Excel
df = load_excel()

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Operaciones", "Auditoría", "Monitoreo Servidores", "APIs"])

with tab1:
    st.header("Vista de Operaciones")

    # Inicializar el DataFrame filtrado
    df_filtered = df.copy()

    # Primer filtro
    selected_field_1 = st.selectbox("Selecciona el primer campo a filtrar:", options=df_filtered.columns, key="field_1")
    if selected_field_1:
        unique_values_1 = df_filtered[selected_field_1].dropna().unique()
        selected_values_1 = st.multiselect(f'Selecciona valores para {selected_field_1}:', options=unique_values_1, key="values_1")
        if selected_values_1:
            df_filtered = df_filtered[df_filtered[selected_field_1].isin(selected_values_1)]

    # Segundo filtro (opcional)
    selected_field_2 = st.selectbox("Selecciona el segundo campo a filtrar (opcional):", options=df_filtered.columns, key="field_2")
    if selected_field_2:
        unique_values_2 = df_filtered[selected_field_2].dropna().unique()
        selected_values_2 = st.multiselect(f'Selecciona valores para {selected_field_2}:', options=unique_values_2, key="values_2")
        if selected_values_2:
            df_filtered = df_filtered[df_filtered[selected_field_2].isin(selected_values_2)]

    # Mostrar la tabla editable del DataFrame filtrado
    edited_df = st.experimental_data_editor(df_filtered, num_rows="dynamic", use_container_width=True)

    # Botones para agregar o eliminar filas
    if st.button("Agregar Fila"):
        new_row = {col: "" for col in df.columns}
        df = df.append(new_row, ignore_index=True)
        edited_df = df

    # Selección de fila para eliminar
    row_to_delete = st.number_input("Número de fila para eliminar", min_value=0, max_value=len(edited_df) - 1, step=1)
    if st.button("Eliminar Fila"):
        df = edited_df.drop(row_to_delete).reset_index(drop=True)
        edited_df = df

    # Botón para guardar cambios
    if st.button("Guardar Ca
