import streamlit as st
import pandas as pd
from model import BertClassifierModel

# Title and Subtitle
st.title("Text Classification")
st.subheader("POC project to classify text (NOISE, TEXT, FIN_TABLE)")

st.write("Created By Anshul Chaudhary")

st.markdown("<br>", unsafe_allow_html=True)

st.session_state["text"] = ''

bertClassifierModel = BertClassifierModel()

data = pd.read_json('../data/unlabeled_data.json', orient="records").head(100)

# Dropdown list
option = st.selectbox("Select an option", data['text'].tolist())

# Text field
input_text = st.text_area("Enter text:")

st.divider()

if input_text or option is not None:
  text = input_text if input_text else option
  st.session_state.text = text
  with st.container():
    st.text_area("Text Set For Processing", value=st.session_state.text, disabled=True)

# Button to proceed
proceed_button = st.button("Proceed")

# Function to process text based on selected option
def process_text():
    # You can add your processing logic here
    text = st.session_state.text
    res = bertClassifierModel.predict(text)
    return f"The result is: {res}"

# Processing and displaying result in a panel
if proceed_button and 'text' in st.session_state.keys() and st.session_state.text is not None:
    processed_result = process_text()
    st.sidebar.subheader("Result:")
    st.sidebar.write(processed_result)