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

    # Mostrar la tabla editable
    edited_df = st.experimental_data_editor(df, num_rows="dynamic", use_container_width=True)

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
