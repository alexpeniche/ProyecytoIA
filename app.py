import streamlit as st
#writing simple text
st.title("Credit Card App Aavila")




# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border: None;
    }
    .stButton button:hover {
        background-color: #ff0000;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("Enhanced Streamlit App")
st.subheader("An improved UI with better layout and styling")

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
