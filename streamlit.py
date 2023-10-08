import streamlit
from quiz import quiz_func

streamlit.set_page_config(page_title="My Webpage", page_icon=":slightly_smiling_face:", layout="wide")
with streamlit.container():
    streamlit.subheader("Hygiene Hero 1.0")
    streamlit.title("Dashboard")
    if streamlit.button('Quiz Results'):
        quiz_func()