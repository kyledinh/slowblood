import streamlit as st
import csv 
import json
import os

from app.config import const

## FUNCTIONS
def seed_with_default():
    st.session_state[const.SEEDED] = const.DEFAULT 
    st.session_state[const.PROJECT_ID] = const.DRAFT
    st.session_state[const.WORKDIR] = 'workdir/'

def seed_to_dirty():
    st.session_state[const.SEEDED] = const.DIRTY 

# Used to check for unset session state, return None
# if get_sess('somekey') in not None: 
def get_sess(key):
    if key not in st.session_state:
        return None 
    return st.session_state[key]

def get_sess_or_default(key, dflt):
    if key not in st.session_state:
        return dflt 
    return st.session_state[key]

# Used to concatenate string with blank "" instead of None
def get_sess_or_blank(key):
    return get_sess_or_default(key, "") 

# Used to concatenate string with "undefined" string instead of None
def get_sess_or_undefined(key):
    return get_sess_or_default(key, const.UNDEFINED) 

def set_sess(key, val):
    if key in st.session_state:
        st.session_state[key] = val 
    else:
        print(f"{key}: <- key not found in st.session_state")
        st.session_state[key] = val 

# checks if ['ui_width','device_type','device_width']
def any_not_in_sess(arr):
    for a in arr:
        if a not in st.session_state:
            return True
    
    return False

def rename_file_to(file_name, new_ext):
    if os.path.isfile(file_name):
        base = os.path.splitext(file_name)[0]
        os.rename(file_name, base + "." + new_ext)

def convert_json_to_csv(file_name):
    if os.path.isfile(file_name):
        base = os.path.splitext(file_name)[0]

        with open(file_name) as json_file:
            jsondata = json.load(json_file)
        
        data_file = open(base + '.csv', 'w', newline='')
        csv_writer = csv.writer(data_file)
        
        count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        data_file.close()
        set_sess(const.CSV_FILE, base + ".csv")