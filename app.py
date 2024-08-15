import streamlit as st
import pandas as pd

# Función para cargar el archivo Excel
def load_excel():
    df = pd.read_excel('archivo_consolidado 1.xlsx')
    return df

# Función para guardar el archivo Excel
def save_excel(df):
    df.to_excel('archivo_consolidado 1.xlsx', index=False)

# Cargar el archivo Excel
df = load_excel()

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Operaciones", "Auditoría", "Monitoreo Servidores", "APIs"])

with tab1:
    st.header("Vista de Operaciones")

    # Dividir la pantalla en dos columnas, con más espacio para la tabla y edición
    col1, col2 = st.columns([1, 4])

    with col1:
        st.subheader("Filtros")

        # Botones para seleccionar la acción
        action = st.radio("Selecciona una acción:", ["Vista (y Filtrado)", "Edición", "Agregar", "Eliminar"])

        # Sección de Vista (y Filtrado)
        if action == "Vista (y Filtrado)":
            st.subheader("Vista y Filtrado de Datos")

            # Filtrado de datos
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

    with col2:
        if action == "Edición":
            st.subheader("Editar directamente en la tabla")

            # Edición directa en la tabla (experimental)
            edited_df = st.data_editor(df_filtered)

            if st.button("Guardar cambios"):
                df.update(edited_df)  # Actualizar el DataFrame original con los cambios
                save_excel(df)
                st.success("Cambios guardados exitosamente")

        elif action == "Agregar":
            st.subheader("Agregar un nuevo registro")
            with st.form(key='add_record'):
                new_record = {}
                for col in df.columns:
                    new_record[col] = st.text_input(f'Nuevo valor para {col}')

                submit_button = st.form_submit_button(label='Agregar registro')

            if submit_button:
                df = df.append(new_record, ignore_index=True)
                save_excel(df)
                st.success("Registro agregado exitosamente")
                df_filtered = df  # Mostrar el DataFrame completo

        elif action == "Eliminar":
            st.subheader("Eliminar un registro")
            row_to_delete = st.number_input("Número de fila para eliminar", min_value=0, max_value=len(df) - 1, step=1)
            
            if row_to_delete is not None:
                # Vista previa de los datos de la fila seleccionada en formato horizontal
                st.subheader(f"Vista previa de la fila {row_to_delete}")
                st.write(df.iloc[row_to_delete].to_frame().T)

            if st.button("Eliminar Fila"):
                df = df.drop(row_to_delete).reset_index(drop=True)
                save_excel(df)
                st.success("Registro eliminado exitosamente")
                df_filtered = df  # Mostrar el DataFrame completo

        if action == "Vista (y Filtrado)":
            st.subheader("Datos Filtrados")
            st.dataframe(df_filtered, width=1000)  # Dar más espacio al DataFrame

with tab2:
    st.header("Vista de Auditoría")
    st.write("Aquí puedes agregar contenido relacionado con la auditoría.")

with tab3:
    st.header("Monitoreo de Servidores")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de servidores.")

with tab4:
    st.header("Monitoreo de APIs")
    st.write("Aquí puedes agregar contenido relacionado con el monitoreo de APIs.")
