
class Configuration():
    version = "0.0.1"

    sidebar_styles = {
      "container": {"padding": "5!important", "background-color": "#fafafa"},
      "icon": {"color": "black", "font-size": "24px"},
      "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
      "nav-link-selected": {"background-color": "#037ffc"},
    }

class Constants():

    # KEYS
    PROJECT_ID = 'project_id'
    SEEDED = 'seeded'
    WORKDIR = 'workdir'


    # VALUES
    DEFAULT = 'default'
    DIRTY = 'dirty'
    DRAFT = 'draft'
    UNDEFINED = 'undefined'

## VARS
const = Constants()  
config = Configuration()  