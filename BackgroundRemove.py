import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    "Cyrus🐵 want you to put ur image on da sidebar to remove the background of it! And you can download the fixed image on da sidebar!"
)
st.sidebar.write("## Upload and download :gear:")

#Set the max file size to 5MB
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")

#Create two columns in the app layout
col1, col2 = st.columns(2)
user_upload = st.sidebar.file_uploader("Boi Plz upload an image right here", type=["png", "jpg", "jpeg"])

if user_upload is not None:
    if user_upload.size > MAX_FILE_SIZE:
        st.error("Bro Your uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload = user_upload)
else:
    fix_image("./PatrickExample.png")