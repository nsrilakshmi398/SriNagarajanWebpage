import streamlit as st

st.title("Contact")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.write("---")
st.header("Get in Touch With Me!")
st.write("##")

contact_form = """
<form action="https://formsubmit.co/nsrilakshmi398@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your Email" required>
<textarea name="Message" placeholder="Your message here" required></textarea>
<button type="submit">Send</button>
</form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
