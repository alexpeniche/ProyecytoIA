import streamlit as st

# Custom CSS for styling and animations
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
        animation: fadeIn 1.5s ease-in-out;
    }

    /* File uploader styling */
    .stFileUploader {
        border: 2px solid #00796b;
        border-radius: 10px;
        padding: 10px;
        background-color: #ffffff;
        transition: box-shadow 0.3s ease;
    }

    .stFileUploader:hover {
        box-shadow: 0px 0px 10px #00796b;
    }

    /* Animation for fade-in effect */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Credit Card App Aavila")

# File uploader section
st.header("Upload Your File")
st.write("Please upload your credit card data file for processing.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xls", "xlsx", "pdf"])

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    # Display basic information about the file
    st.write("File type:", uploaded_file.type)
    st.write("File size:", len(uploaded_file.getvalue()), "bytes")

    # You can add further file processing logic here, depending on the file type
