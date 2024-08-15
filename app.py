import streamlit as st
import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('archivo_consolidado 1.xlsx')

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Operaciones", "Auditoría", "Monitoreo Servidores", "APIs"])

with tab1:
    st.header("Vista de Operaciones")

    # Crear una copia del DataFrame original para aplicar filtros de manera acumulativa
    df_filtered = df.copy()

    # Paso 1: Seleccionar el campo a filtrar
    selected_field = st.selectbox("Selecciona el campo a filtrar:", options=df_filtered.columns)

    # Paso 2: Seleccionar valores basados en el campo seleccionado
    if selected_field:
        unique_values = df_filtered[selected_field].dropna().unique()  # Obtener valores únicos del campo seleccionado
        selected_values = st.multiselect(f'Selecciona valores para {selected_field}:', options=unique_values)

        # Aplicar el filtro al DataFrame basado en los valores seleccionados
        if selected_values:
            df_filtered = df_filtered[df_filtered[selected_field].isin(selected_values)]

    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtered)

    # Agregar opción para filtrar nuevamente sobre el DataFrame ya filtrado
    if not df_filtered.empty:
        update_filter = st.checkbox("¿Quieres aplicar otro filtro?", value=False)
        if update_filter:
            selected_field_2 = st.selectbox("Selecciona el siguiente campo a filtrar:", options=df_filtered.columns)
            if selected_field_2:
                unique_values_2 = df_filtered[selected_field_2].dropna().unique()
                selected_values_2 = st.multiselect(f'Selecciona valores para {selected_field_2}:', options=unique_values_2)

                if selected_values_2:
                    df_filtered = df_filtered[df_filtered[selected_field_2].isin(selected_values_2)]

            # Mostrar el DataFrame nuevamente después de aplicar el segundo filtro
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
