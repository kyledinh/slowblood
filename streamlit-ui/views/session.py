import streamlit as st
from app.st_functions import st_button

class SessionView:
    class Model:
        page_title = "Session"

    def view(self, model):
        st.title(model.page_title)
        st.write("Session State")
