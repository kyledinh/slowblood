
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

    DEVICE_TYPE = 'device_type'
    DEVICE_WIDTH = 'device_width'
    UI_WIDTH = 'ui_width'

    CSV_DATA = 'csv_data'
    CSV_FILE = 'csv_file'
    JSON_DATA = 'json_data'
    JSON_FILE = 'json_file'

    # VALUES
    DEFAULT = 'default'
    DESKTOP = 'desktop'
    DIRTY = 'dirty'
    DRAFT = 'draft'
    MOBILE = 'mobile'
    UNDEFINED = 'undefined'

## VARS
const = Constants()  
config = Configuration()  