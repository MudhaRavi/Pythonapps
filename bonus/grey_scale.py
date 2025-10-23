import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
# If an image is captured, convert it to grayscale and display it
    img = Image.open(camera_image)
elif uploaded_image:
# If an image is uploaded, convert it to grayscale and display it
    img = Image.open(uploaded_image)

# Convert the image to grayscale
    gray_img = img.convert("L")
# Display the grayscale image on web page
    st.image(gray_img)



st.write("This is a simple app that converts your image to grayscale.")
