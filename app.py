import streamlit as st
#writing simple text
st.title("Credit Card App Aavila")


# Text input
user_input = st.text_input("Enter some text:")

# Display the input
st.write("You entered:", user_input)

# Number input
number = st.number_input("Enter a number:", min_value=0, max_value=100)

# Display the number
st.write("Your number is:", number)

# Selectbox
option = st.selectbox(
    "Choose an option:",
    ("Option 1", "Option 2", "Option 3")
)

# Display the selected option
st.write("You selected:", option)

# Button to trigger an action
if st.button("Click me"):
    st.write("Button clicked!")

# Slider
slider_value = st.slider("Select a range of values", 0, 100, (25, 75))

# Display the slider value
st.write("Slider value range:", slider_value)

# File uploader
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write("File uploaded:", uploaded_file.name)
    st.write(bytes_data)

