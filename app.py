import streamlit as st
import pandas as pd

# Custom CSS for colors and improved UI
st.markdown(
    """
    <style>
    .main {
        background-color: rgb(132, 0, 88);
        color: white;
        padding: 20px;
    }

    h1, h2, h3 {
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }

    .stTextInput, .stNumberInput, .stSelectbox {
        font-size: 18px;
        border: 2px solid #FFFFFF;
        border-radius: 10px;
    }

    .stButton button {
        background-color: #660066;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #990099;
    }

    .stFileUploader {
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        background-color: #ffffff;
        color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title and introduction
st.title("Credit Card App")
st.subheader("Una herramienta para analizar y predecir riesgos crediticios")

# Sidebar menu
pages = ["Cargar Datos", "Explorar Datos", "Feature Engineering", "Modelado", "Neural Network", "Predicción"]
selected_page = st.sidebar.radio("Seleccione una página", pages)

# Function to display the data upload page
def cargar_datos():
    st.header("Cargar Datos")
    st.write("Suba su archivo CSV para comenzar.")
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    if uploaded_file is not None:
        dataset = pd.read_csv(uploaded_file)
        st.write("Datos cargados con éxito. Aquí una vista previa de los primeros registros:")
        st.write(dataset.head())
        return dataset
    else:
        st.info("Esperando a que se cargue un archivo...")
        return None

# Function to display the data exploration page
def explorar_datos(dataset):
    st.header("Explorar Datos")
    if dataset is not None:
        st.write("Distribución de los datos:")
        st.write(dataset.describe())
        st.write("Vista previa de los primeros registros:")
        st.write(dataset.head())
    else:
        st.warning("Primero debe cargar los datos.")

# Function to handle feature engineering
def feature_engineering(dataset):
    st.header("Feature Engineering")
    if dataset is not None:
        st.write("Implementar aquí las técnicas de ingeniería de características.")
        if st.button("Agregar nueva columna 'Balance/Income Ratio'"):
            dataset['Balance/Income Ratio'] = dataset['Balance'] / dataset['Income']
            st.write("Columna agregada con éxito.")
            st.write(dataset.head())
    else:
        st.warning("Primero debe cargar los datos.")

# Function for modeling page
def modelado(dataset):
    st.header("Modelado")
    if dataset is not None:
        st.write("Entrenamiento con diferentes modelos.")
        st.write("Implementar aquí los modelos de Machine Learning.")
    else:
        st.warning("Primero debe cargar los datos.")

# Function for neural network page
def neural_network(dataset):
    st.header("Neural Network")
    if dataset is not None:
        st.write("Entrenamiento de redes neuronales.")
        st.write("Implementar aquí la red neuronal.")
    else:
        st.warning("Primero debe cargar los datos.")

# Function for prediction page
def prediccion():
    st.header("Predicción de un Crédito")
    st.write("Capture los datos para realizar una predicción.")
    st.write("Implementar aquí el formulario para capturar los datos y hacer la predicción.")

# Dictionary to map page names to functions
page_functions = {
    "Cargar Datos": cargar_datos,
    "Explorar Datos": explorar_datos,
    "Feature Engineering": feature_engineering,
    "Modelado": modelado,
    "Neural Network": neural_network,
    "Predicción": prediccion
}

# Store dataset across pages
if "dataset" not in st.session_state:
    st.session_state.dataset = None

# Call the function associated with the selected page
if selected_page:
    st.session_state.dataset = page_functions[selected_page](st.session_state.dataset)
