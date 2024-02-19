import math
import json
import pandas as pd

import streamlit as st
from app.session import get_sess, get_sess_or_blank, get_sess_or_undefined, set_sess
from app.config import const 
import slowblood


class ProjectView:
    class Model:
        subheader_2 = "Upload PDF of Invoice"
        content_text = None


    def view(self, model, ui_width, device_type, device_width):

        st.header('Current Project:')
        with st.container():
            placeholder = get_sess_or_undefined(const.PROJECT_ID)
            pid = st.text_input("Project ID:", placeholder)
            if pid:
                set_sess(const.PROJECT_ID, pid) 

        if get_sess(const.JSON_FILE) is not None:
            with st.expander("View JSON Data"):
                json_data = get_sess_or_undefined(const.JSON_DATA)
                st.download_button(
                    label="Download JSON file",
                    data=json_data,
                    file_name=get_sess(const.JSON_FILE),
                    mime='text/json',
                )
                st.json(json_data)


        if get_sess(const.CSV_FILE) is not None:
            with st.expander("View CSV Data"):
                csv_df = pd.read_csv(get_sess(const.CSV_FILE))
                st.download_button(
                    label="Download CSV file",
                    data=csv_df.to_csv().encode('utf-8'),
                    file_name=get_sess(const.CSV_FILE),
                    mime='text/csv',
                )
                st.write(csv_df)