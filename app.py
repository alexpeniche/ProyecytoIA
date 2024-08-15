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

    # Bucle para permitir múltiples filtros
    filter_count = 0
    while True:
        # Seleccionar el campo a filtrar
        selected_field = st.selectbox(f"Selecciona el campo a filtrar (Filtro {filter_count + 1}):", options=df_filtered.columns, key=f"field_{filter_count}")

        # Seleccionar valores basados en el campo seleccionado
        if selected_field:
            unique_values = df_filtered[selected_field].dropna().unique()  # Obtener valores únicos del campo seleccionado
            selected_values = st.multiselect(f'Selecciona valores para {selected_field}:', options=unique_values, key=f"values_{filter_count}")

            # Aplicar el filtro al DataFrame basado en los valores seleccionados
            if selected_values:
                df_filtered = df_filtered[df_filtered[selected_field].isin(selected_values)]

            # Mostrar el DataFrame filtrado
            st.dataframe(df_filtered)

        # Preguntar si se desea aplicar otro filtro
        apply_another_filter = st.radio("¿Deseas aplicar otro filtro?", ("Sí", "No"), key=f"radio_{filter_count}")

        if apply_another_filter == "No":
            break

        filter_count += 1

with tab2:
    st.header("Vista de Auditoría")
    st.write("Aquí puedes agregar contenido relacionado con la auditoría.")

with tab3:
    st.header("Monitoreo de Servidores")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de servidores.")

with tab4:
    st.header("Monitoreo de APIs")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de APIs.")
