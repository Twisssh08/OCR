import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.markdown(
    """
    <style>
    .stApp {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto que contenga texto en ella, este sitio web lo pasará a texto por tí.")

with st.sidebar:
    st.markdown(
    """
    <style>
    .stApp {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)
      filtro = st.radio("¿Quieres aplicar filtro?",('Sí quiero', 'No quiero'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Sí quiero':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img= cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 
    


    


