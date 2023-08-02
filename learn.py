#To run the webpage use the following command in the terminal:
# streamlit run .\learn.py 

import streamlit as st

st.set_page_config(page_title='Sri Nagarajan', page_icon=':blue_heart:', layout='wide')
#For emoji: https://www.webfx.com/tools/emoji-cheat-sheet/

#----------HEADER SECTION----------
st.subheader('Hi I am Sri Nagarajan.')
st.title('Amateur Data Scientist for Climate Change')
st.write('I am passionate about fidning ways to use AI and data science to understand Earth processes and study about climate change.')
st.write("[LinkedIn](https://www.linkedin.com/in/srilakshminagarajan/)")

#----WHAT I DO----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a recent graduate from TUM yada yada. Write something about myself!
            """
        )
        st.write("Look into LottieFiles and Animations")

# To add animations use LottieFiles a json based animation file format. Look for other ways for animation.

#----PROJECTS----
with st.container():
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2)) #Second column i.e. text here is twice as big as the image
    #with image_column:
        #insert image
    with text_column:
        st.subheader("Test project title")
        st.write(
            """
            Write a brief description of the test project.
            - Learning how to use streamlit package from Python to create a personal website
            - I will soon add the details of the projects I take up
            - Also information about my past projects
            """
        )

#----CONTACT-----
with st.container():
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
        

