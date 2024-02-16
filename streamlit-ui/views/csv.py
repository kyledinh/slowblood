import json
import math
import os
import time

import streamlit as st
import slowblood
from app.config import const 
from app.session import seed_with_default, seed_to_dirty, get_sess, get_sess_or_blank, get_sess_or_default, get_sess_or_undefined, set_sess

class CsvView:
    class Model:
        page_title = 'CSV Dataframes'
        sidebar_subheader = "Upload Files"
        initial_msg = "Upload or enter a JSON payload... "

        upload_help = "Upload a file to extract data from it"
        upload_button_text = "Upload"
        upload_button_text_desc = "Choose a file"

    def view(self, model):
        st.title(model.page_title)

        with st.sidebar:
            st.markdown("---")
            st.subheader(model.sidebar_subheader)

            with st.form("upload-form", clear_on_submit=True):
                workdir = get_sess_or_default(const.WORKDIR, "workdir/")

                uploaded_file = st.file_uploader(model.upload_button_text_desc, 
                                                 accept_multiple_files=False,
                                                 type=['json'],
                                                 help=model.upload_help)
                submitted = st.form_submit_button(model.upload_button_text)

                if submitted and uploaded_file is not None:
                    ret = self.upload_file(workdir, uploaded_file)

                    if ret is not False:
                        set_sess(const.JSON_FILE, ret)
                        set_sess(const.CSV_DATA, None)

        if get_sess(const.JSON_FILE) is not None:
            # doc_text = get_sess(const.INVOICE_CONTENT_TEXT) 
            # self.render_doc(model, doc_text, 600, 800, 600)
            self.render_results(model)
        else:
            st.title(model.initial_msg)

    def upload_file(self, workdir, uploaded_file):
        timestamp = str(time.time())
        timestamp = timestamp.replace(".", "")
        project_id = get_sess_or_undefined(const.PROJECT_ID)

        file_name, file_extension = os.path.splitext(uploaded_file.name)
        uploaded_file.name = file_name + "_" + project_id + file_extension

        if os.path.exists(os.path.join(workdir, uploaded_file.name)):
            st.write("File already exists")
            return False

        if len(uploaded_file.name) > 500:
            st.write("File name too long")
            return False

        with open(os.path.join(workdir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        with open(os.path.join(workdir, uploaded_file.name), "r") as j:
            set_sess(const.JSON_DATA, j.read())

        st.success("File uploaded successfully")

        return os.path.join(workdir, uploaded_file.name)


    def render_results(self, model):

        if get_sess(const.JSON_FILE) is not None:
            with st.expander("Edit JSON DATA"):
                json_data = get_sess_or_undefined(const.JSON_DATA)
                new_json_data = st.text_area("JSON FILE:", json_data, height=400)
                if new_json_data:
                    set_sess(const.JSON_DATA, new_json_data)  


   