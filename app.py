import streamlit as st
from home import *
from mlcode import *
from About import *

st.set_page_config(
        page_title="Summarizer",
        page_icon="📚",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"}
    )
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Code","About"])

# Page content
if selection == "Home":
    st.title("Summarizer")
    runhome()


elif selection == "Code":
    st.title("NLP Code Of This Project")
    runcode()

elif selection == "About":
    # st.title("About Page")
    about_section()
# Add more sections/pages as needed
# Input box for user to enter text


