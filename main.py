import streamlit as st
import google.generativeai as genai
import PIL.Image
import textwrap


# Configure the Google API Key
GOOGLE_API_KEY = 'AIzaSyA1fu-ob27CzsJozdr6pHd96t5ziaD87wM'
genai.configure(api_key=GOOGLE_API_KEY)

# Function to convert text to markdown with custom formatting
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Streamlit App Layout
st.title("Google Gemini Vision Pro Analysis")
st.subheader("Image and Text Analysis using Google's AI")
st.write("Upload an image and enter related text to get insightful analysis using Google Gemini Vision Pro.")

# Image Upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Text Input for Analysis
user_input_text = st.text_area("Enter text for analysis with the image:")

# Analyzing Image and Text with Google Gemini Vision Pro
if st.button('Analyze'):
    if uploaded_file is not None and user_input_text:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([user_input_text, image], stream=True)
        response.resolve()
        analysis_result = to_markdown(response.text)
        st.markdown(analysis_result)
    else:
        st.warning("Please upload an image and enter text for analysis.")

# Sidebar with Developer Contact Information
st.sidebar.header("Developer Contact")
st.sidebar.markdown("Name: A Chethan Reddy")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/achethanreddy/)")
st.sidebar.markdown("[GitHub](https://github.com/chethanreddy123)")

# Run this app with `streamlit run app.py` in your terminal
