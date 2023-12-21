# Google Gemini Vision Pro Streamlit App

## Overview
This Streamlit application allows users to upload images and enter text, which are then analyzed using Google's Gemini Vision Pro API. The app provides insightful analysis by generating content based on the image and the user-provided text.

## Features
- **Image Upload**: Users can upload images in JPG, PNG, or JPEG format.
- **Text Input**: Users can input text to be analyzed in conjunction with the uploaded image.
- **Google Gemini Vision Pro Integration**: The app utilizes the Gemini Pro Vision model for generating analysis content.
- **Responsive UI**: A user-friendly interface with a clear layout for uploading images, entering text, and viewing results.

## Installation

To run this application, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/[your-username]/gemini-vision-pro-streamlit.git
cd gemini-vision-pro-streamlit

python -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

GOOGLE_API_KEY = 'YOUR_API_KEY'

streamlit run app.py
```