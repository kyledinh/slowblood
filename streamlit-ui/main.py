import streamlit as st 
import streamlit_javascript as st_js
from streamlit_option_menu import option_menu

import pandas as pd 
import json

import sys
sys.path.append('/Users/kyle/src/github.com/kyledinh/slowblood')
## import locally instead of `pip install slowblood`
from pypi.src import slowblood as sb 

## local imports 
from app.config import config, const
from app.utilities import load_css
from app.session import any_not_in_sess, get_sess, get_sess_or_blank, get_sess_or_undefined, set_sess

from views.about import AboutView
from views.csv import CsvView
from views.project import ProjectView 
from views.session import SessionView 

st.set_page_config(
    page_title="GSB Audit Agent",
    page_icon="favicon.ico",
    layout="wide"
)

load_css()

class Model:
    sidebar_title = "Slowblood App"
    tab_about = "About"
    tab_csv = "CSV"
    tab_project = "Project"
    tab_session = "Session"
    tab_runpod = "Runpod"
    tab_huggingface = "Huggingface"

    icon_about = "person-badge"
    icon_csv = "file-earmark-ruled"
    icon_project = "folder-fill"
    icon_session = "database-check"
    icon_menu = "stack"
    icon_runpod = "gpu-card"
    icon_huggingface = "emoji-laughing-fill"


def view(model):
    with st.sidebar:
        menuItem = option_menu(
            model.sidebar_title,
            [model.tab_project, model.tab_csv, model.tab_session, model.tab_about],
            icons=[model.icon_project, model.icon_csv, model.icon_session, model.icon_about],
            menu_icon=model.icon_menu,
            default_index=0,
            styles=config.sidebar_styles
        )

    if menuItem == model.tab_project:
        if any_not_in_sess([const.UI_WIDTH,const.DEVICE_TYPE,const.DEVICE_WIDTH]):
            # Get UI width
            ui_width = st_js.st_javascript("window.innerWidth", key="ui_width_comp")
            device_width = st_js.st_javascript("window.screen.width", key="device_width_comp")

            if ui_width > 0 and device_width > 0:
                # Add 20% of current screen width to compensate for the sidebar
                ui_width = round(ui_width + (20 * ui_width / 100))

                if device_width > 768:
                    device_type = const.DESKTOP
                else:
                    device_type = const.MOBILE

                set_sess(const.UI_WIDTH, ui_width)
                set_sess(const.DEVICE_TYPE, device_type)
                set_sess(const.DEVICE_WIDTH, device_width)

                st.experimental_rerun()

        else:
            ProjectView().view(ProjectView.Model(), get_sess(const.UI_WIDTH), get_sess(const.DEVICE_TYPE), get_sess(const.DEVICE_WIDTH))
            logout_widget()

    if menuItem == model.tab_csv:
        CsvView().view(CsvView.Model())
        logout_widget()

    if menuItem == model.tab_session:
        SessionView().view(SessionView.Model())
        logout_widget()

    if menuItem == model.tab_about:
        AboutView().view(AboutView.Model())
        logout_widget()

def logout_widget():
    with st.sidebar:
        st.markdown("---")
        st.write("Version:", config.version)

        if get_sess('visitors') is None:
            with open("config/visitors.json", "r") as f:
                visitors_json = json.load(f)
                visitors = visitors_json["meta"]["visitors"]

            visitors += 1
            visitors_json["meta"]["visitors"] = visitors

            with open("docs/visitors.json", "w") as f:
                json.dump(visitors_json, f)

            set_sess('visitors', visitors)
        else:
            visitors = get_sess('visitors')

        st.write("Counter:", visitors)

## MAIN
st.write(sb.help())
view(Model())