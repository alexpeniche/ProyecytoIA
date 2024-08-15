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

    # Límite máximo de filtros
    max_filters = 5
    filter_count = 0

    # Bucle para aplicar múltiples filtros con límite de 5
    while filter_count < max_filters:
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

        # Incrementar el contador de filtros
        filter_count += 1

        # Verificar si se ha alcanzado el número máximo de filtros
        if filter_count >= max_filters:
            st.warning("Has alcanzado el número máximo de 5 filtros.")
            break

        # Preguntar si se desea aplicar otro filtro
        apply_another_filter = st.radio("¿Deseas aplicar otro filtro?", ("Sí", "No"), key=f"radio_{filter_count}")

        if apply_another_filter == "No":
            break

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
    if st.button("Guardar Cambios"):
        save_excel(edited_df)
        st.success("Cambios guardados exitosamente")

    # Mostrar el DataFrame actualizado
    st.dataframe(edited_df)

with tab2:
    st.header("Vista de Auditoría")
    st.write("Aquí puedes agregar contenido relacionado con la auditoría.")

with tab3:
    st.header("Monitoreo de Servidores")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de servidores.")

with tab4:
    st.header("Monitoreo de APIs")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de APIs.")
