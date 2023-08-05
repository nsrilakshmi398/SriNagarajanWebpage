# Fill the different sections for projects

import streamlit as st
from PIL import Image

def under_construction():
    img_loc='images/under_construction.jpeg'
    image = Image.open(img_loc)
    st.image(image)

st.title("Projects")

#Call CSS if applicable

#st.write("You have entered", st.session_state["my_inupt"])

under_construction()
