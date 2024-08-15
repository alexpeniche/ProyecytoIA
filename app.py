import streamlit as st
#writing simple text
st.title("Credit Card App Aavila")

import streamlit as st

# Custom CSS for colors and animations
st.markdown(
    """
    <style>
    /* Background color for the main content */
    .main {
        background-color: #e0f7fa;
        padding: 20px;
    }

    /* Title styling */
    h1 {
        color: #00695c;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }

    h2 {
        color: #00796b;
        font-family: 'Helvetica Neue', sans-serif;
    }

    h3 {
        color: #004d40;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Input box styling */
    .stTextInput, .stNumberInput, .stSelectbox {
        font-size: 18px;
        border: 2px solid #00796b;
        border-radius: 10px;
    }

    /* Button styling and hover effect */
    .stButton button {
        background-color: #004d40;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #00796b;
        color: white;
    }

    /* File uploader styling */
    .stFileUploader {
        border: 2px solid #00796b;
        border-radius: 10px;
        padding: 10px;
    }

    /* Animation for headers */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    h1, h2, h3 {
        animation: fadeIn 1.5s ease-in-out;
    }

    /* Animation for buttons */
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-20px); }
        60% { transform: translateY(-10px); }
    }

    .stButton button {
        animation: bounce 2s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("Enhanced Streamlit App with Colors & Animations")
st.subheader("An improved UI with custom colors, animations, and better layout")

# Creating columns for better layout
col1, col2 = st.columns(2)

# First column: Text input and number input
with col1:
    st.header("User Input")
    user_input = st.text_input("Enter some text:", placeholder="Type something here...")
    st.write("You entered:", user_input)

    number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
    st.write("Your number is:", number)

# Second column: Dropdown and button
with col2:
    st.header("Options")
    option = st.selectbox(
        "Choose an option:",
        ("Option 1", "Option 2", "Option 3")
    )
    st.write("You selected:", option)

    if st.button("Submit"):
        st.success(f"Submitted: {user_input}, {number}, {option}")

# Slider below the columns
st.header("Adjust Values")
slider_value = st.slider("Select a range of values", 0, 100, (25, 75))
st.write("Slider value range:", slider_value)

# File uploader at the bottom
st.header("File Upload")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    st.write("File contents:", uploaded_file.getvalue())
