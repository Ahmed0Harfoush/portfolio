import streamlit as st
import os
import base64

st.set_page_config(page_title="Ahmed Harfoush - Portfolio", layout="wide")

# Load HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Convert all images in "Image/" folder to base64 and replace paths
image_folder = "Image"
if os.path.exists(image_folder):
    for image_file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, image_file)
        with open(file_path, "rb") as img_f:
            data = base64.b64encode(img_f.read()).decode()
            # Detect file type (jpg, png, jpeg)
            ext = image_file.split(".")[-1]
            html_code = html_code.replace(
                f"Image/{image_file}", f"data:image/{ext};base64,{data}"
            )

# Render HTML in Streamlit
st.components.v1.html(html_code, height=1500, scrolling=True)
