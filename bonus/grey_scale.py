import streamlit as st
from PIL import Image

camera_image = st.camera_input("Take a picture")

if camera_image:
# If an image is captured, convert it to grayscale and display it
    img = Image.open(camera_image)
# Convert the image to grayscale
    gray_img = img.convert("L")
# Display the grayscale image on web page
    st.image(gray_img)

st.write("This is a simple app that converts your image to grayscale.")
