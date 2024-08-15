import streamlit as st 
import numpy as np 
import pandas as pd
import plotly.offline as py 
#py.init_notebook_mode(connected=True) # this code, allow us to work with offline plotly version
import plotly.graph_objs as go # it's like "plt" of matplot
import plotly.tools as tls # It's useful to we get some tools of plotly


#writing simple text 

st.title("Credit Card App")

st.markdown(
    """
    <style>
    /* Estilo principal */
    .main {
        background-color: rgb(132, 0, 88);
        color: white;
        padding: 20px;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Estilo de los títulos */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
        animation: fadeIn 1.5s ease-in-out;
    }

    /* Estilo de los inputs */
    .stTextInput, .stNumberInput, .stSelectbox, .stFileUploader {
        font-size: 16px;
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
        transition: box-shadow 0.3s ease;
    }

    /* Hover effect para inputs */
    .stTextInput:hover, .stNumberInput:hover, .stSelectbox:hover, .stFileUploader:hover {
        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.5);
    }

    /* Estilo de los botones */
    .stButton button {
        background-color: #660066;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 10px;
        margin-bottom: 10px;
        transition: background-color 0.3s ease, transform 0.3s ease;
        border: none;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
    }

    /* Hover effect para botones */
    .stButton button:hover {
        background-color: #990099;
        transform: scale(1.05);
    }

    /* Estilo para el File Uploader */
    .stFileUploader {
        background-color: #ffffff;
        color: #000000;
    }

    /* Animación para los títulos */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    </style>
    """,
    unsafe_allow_html=True
)
#definir funciones
def get_eda(dataset):
    # Distribución de Creditos por Tipo de Casa
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["housing"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["housing"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["housing"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["housing"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Housing Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

    # Distribución de Creditos por Genero
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["sex"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["sex"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["sex"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["sex"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Gender Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

    # Distribución de Creditos por Job
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["job"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["job"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["job"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["job"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Job Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

    # Distribución de Creditos por Cuentas de ahorro
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["saving_accounts"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["saving_accounts"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["saving_accounts"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["saving_accounts"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Saving Accounts Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)


    # Distribución de Creditos por Cuentas de Crédiro
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["checking account"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["checking account"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["checking account"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["checking account"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Checking Account Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

    # Distribución de Creditos por duración
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["duration"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["duration"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["duration"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["duration"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Duration Distribution'
    )

    fig = go.Figure(data=data, layout=layout)   
    st.plotly_chart(fig)
    
    # Distribución de Creditos por Propósito
    trace0 = go.Bar(
        x=dataset[dataset["risk"] == 'good']["purpose"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'good']["purpose"].value_counts().values,
        name='Good credit'
    )

    trace1 = go.Bar(
        x=dataset[dataset["risk"] == 'bad']["purpose"].value_counts().index.values,
        y=dataset[dataset["risk"] == 'bad']["purpose"].value_counts().values,
        name="Bad Credit"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='Purpose Distribution'
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)


#writing simple text 

st.title("Credit Card App")

    
# ============ Aplicación Principal  ============
        
# Definir las opciones de página
pages = ["Cargar Datos", "Explorar Datos", "Feature Engineering", "Modelado", "Neural Network", "Prediccion"]


# Mostrar un menú para seleccionar la página
selected_page = st.sidebar.multiselect("Seleccione una página", pages)

# Condicionales para mostrar la página seleccionada
if "Cargar Datos" in selected_page:
    st.write("""
    ## Cargar Datos""")
    # Cargar archivo CSV usando file uploader
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    # Si el archivo se cargó correctamente
    if uploaded_file is not None:
    # Leer archivo CSV usando Pandas
        dataset = pd.read_csv(uploaded_file)
    # Mostrar datos en una tabla
        st.write(dataset)

if "Explorar Datos" in selected_page:
    st.write("""
    ## Explore Data
    Distributions""")
    if uploaded_file is not None:
        get_eda(dataset)
        
if "Feature Engineering" in selected_page:
    st.write("""
    ## Feature Engineering
    New datset""")

if "Modelado" in selected_page:
    st.write("""
    ## Entrenamiento con diferentes modelos
    Resultados""")

        
if "Neural Network" in selected_page:
    st.write("""
    ## Neural Network
    Resultados""")

        
if "Prediccion" in selected_page:
    st.write("""
    ## Predicción de un Crédito
    Capture los datos""")
 

# ============ Aplicación Principal  ============
        
# Definir las opciones de página
pages = ["Cargar Datos", "Explorar Datos", "Feature Engineering", "Modelado", "Neural Network", "Prediccion"]


# Mostrar un menú para seleccionar la página
selected_page = st.sidebar.multiselect("Seleccione una página", pages)

# Condicionales para mostrar la página seleccionada
if "Cargar Datos" in selected_page:
    st.write("""
    ## Cargar Datos""")
    # Cargar archivo CSV usando file uploader
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    # Si el archivo se cargó correctamente
    if uploaded_file is not None:
    # Leer archivo CSV usando Pandas
        dataset = pd.read_csv(uploaded_file)
    # Mostrar datos en una tabla
        st.write(dataset)

if "Explorar Datos" in selected_page:
    st.write("""
    ## Explore Data
    Distributions""")
        
if "Feature Engineering" in selected_page:
    st.write("""
    ## Feature Engineering
    New datset""")

if "Modelado" in selected_page:
    st.write("""
    ## Entrenamiento con diferentes modelos
    Resultados""")

        
if "Neural Network" in selected_page:
    st.write("""
    ## Neural Network
    Resultados""")

        
if "Prediccion" in selected_page:
    st.write("""
    ## Predicción de un Crédito
    Capture los datos""")
 
