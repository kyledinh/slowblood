import streamlit as st

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