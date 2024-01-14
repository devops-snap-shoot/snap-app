import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import base64

# Convert image to base64
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_base64 = img_to_base64("assets/snap-logo.png")


# Create header with image and text 

def head(header_text, caption_text):
    st.markdown(
    f'<h3 style="display: inline;">'
    f'<img src="data:image/png;base64,{image_base64}" style="vertical-align:middle; margin-right: 5px;" width="30" height="30"/>'
    f'{header_text}</h2>',
    unsafe_allow_html=True
    )
    if caption_text:
        st.caption(caption_text)
    
        


