import math
import json
import pandas as pd

import streamlit as st
from app.session import get_sess, get_sess_or_blank, get_sess_or_undefined, set_sess
from app.config import const as kon
import slowblood


class CurrentProject:
    class Model:
        subheader_2 = "Upload PDF of Invoice"
        content_text = None


    def view(self, model, ui_width, device_type, device_width):

        st.header('Current Project:')
        with st.container():
            placeholder = get_sess_or_undefined(kon.PROJECT_ID)
            pid = st.text_input("Project ID:", placeholder)
            if pid:
                set_sess(kon.PROJECT_ID, pid) 