import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit_javascript as st_js

import pandas as pd 
import json

import sys
sys.path.append('/Users/kyle/src/github.com/kyledinh/slowblood')
## import locally instead of `pip install slowblood`
from pypi.src import slowblood as sb 

## local imports 
from app.config import config
from app.utilities import load_css
from views.project import CurrentProject 
from views.about import About


st.set_page_config(
    page_title="GSB Audit Agent",
    page_icon="favicon.ico",
    layout="wide"
)

load_css()

class Model:
    sidebar_title = "Slowblood App"
    tab_about = "About"
    tab_project = "Project"

    icon_about = "chat"
    icon_project = "stack"
    icon_menu = "globe-americas"


def view(model):
    with st.sidebar:
        menuItem = option_menu(
            model.sidebar_title,
            [model.tab_project, model.tab_about],
            icons=[model.icon_project, model.icon_about],
            menu_icon=model.icon_menu,
            default_index=0,
            styles=config.sidebar_styles
        )

    if menuItem == model.tab_project:
        if 'ui_width' not in st.session_state or 'device_type' not in st.session_state or 'device_width' not in st.session_state:
            # Get UI width
            ui_width = st_js.st_javascript("window.innerWidth", key="ui_width_comp")
            device_width = st_js.st_javascript("window.screen.width", key="device_width_comp")

            if ui_width > 0 and device_width > 0:
                # Add 20% of current screen width to compensate for the sidebar
                ui_width = round(ui_width + (20 * ui_width / 100))

                if device_width > 768:
                    device_type = 'desktop'
                else:
                    device_type = 'mobile'

                st.session_state['ui_width'] = ui_width
                st.session_state['device_type'] = device_type
                st.session_state['device_width'] = device_width

                st.experimental_rerun()
        else:
            CurrentProject().view(CurrentProject.Model(), st.session_state['ui_width'], st.session_state['device_type'],
                                    st.session_state['device_width'])
    if menuItem == model.tab_about:
        About().view(About.Model())
        logout_widget()


def logout_widget():
    with st.sidebar:
        st.markdown("---")
        st.write("Version:", config.version)

        if 'visitors' not in st.session_state:
            with open("config/visitors.json", "r") as f:
                visitors_json = json.load(f)
                visitors = visitors_json["meta"]["visitors"]

            visitors += 1
            visitors_json["meta"]["visitors"] = visitors

            with open("docs/visitors.json", "w") as f:
                json.dump(visitors_json, f)

            st.session_state['visitors'] = visitors
        else:
            visitors = st.session_state['visitors']

        st.write("Counter:", visitors)

## MAIN

st.write(sb.help())

view(Model())