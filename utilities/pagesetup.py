import streamlit as st
from PIL import Image
import os
import base64
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import datetime

image_base_path = os.path.dirname(os.path.realpath(__file__))
template_main_page = "https://github.com/b-macd/streamlit-multi-page-with-authentication/tree/main"
idsg_image = '../images/IDSG Gray Logo-cropped.png'
innovation_image = '../images/innovation-logo2.png'
idsg_landing = ''
innovation_landing = ''

##########################Page Setup Functions###########################################
def master_set_page_config(page_title, about):
    idsg_logo_image = Image.open(os.path.join(image_base_path, idsg_image))
    st.set_page_config(
        page_title=page_title,
        menu_items={
            'Get Help':template_main_page,
            "Report a bug": template_main_page,
            'About': about
        },
        page_icon= idsg_logo_image,
        initial_sidebar_state = "auto",
        layout="wide"
    )

def get_b64_image(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_image_href(img_path, url, width, height):
    bin_str = get_b64_image(img_path)
    html = f'''
        <a href="{url}" target="_blank">
            <img src="data:image/png;base64,{bin_str}" width="100%" height="{height}"/>
        </a>'''
    return html

def idsg_load_logos():
    innovation_logo, idsg_logo = st.columns([1,1])
    image_base_path = os.path.dirname(os.path.realpath(__file__))
    innovation_logo.markdown(get_image_href(os.path.join(image_base_path, innovation_image), innovation_landing, 150, 140), unsafe_allow_html=True)
    idsg_logo.markdown(get_image_href(os.path.join(image_base_path, idsg_image), idsg_landing, 150, 140), unsafe_allow_html=True)

def idsg_load_buttons():
    st.info("Want to see continued support or new features for this tool? Let us know [here](https://github.com/b-macd/streamlit-multi-page-with-authentication/tree/main)!")
    idsg_tools_button, report_bug_button = st.columns([1,1])
    #with idsg_tools_button:
        #st.link_button("IDSG Tools", idsg_landing)
    with report_bug_button:
        st.link_button("Report a Bug", template_main_page)
    
def load_tool_header(title='', logo_path=None, logo_size=150):
    logo_col, title_col, blank_col = st.columns([1,1,1])
    if logo_path:
        tool_logo_image = Image.open(os.path.join(os.getcwd(), logo_path))
        logo_col.image(tool_logo_image, width=150)
    else:
        logo_col.write(' ')
    title_col.title(title)
    blank_col.write(' ')


##########################Homepage Setup###########################################

def load_custom_css():
    custom_css = """
    <style>
    .stCard {
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 16px;
        text-align: center;
        max-width: 300px;
        margin: 300px;
        display: block;
        color: inherit;
        text-decoration: none;
    }

    .stCard img {
        max-width: 100%;
        height: auto;
        border-radius: 4px;
    }   

    .stCard p {
        color: #666
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def streamlit_card(image, title, description, url):
    image_64 = get_b64_image(image)

    load_custom_css()

    card_html = f"""
    <a href = '{url}' target = '_blank' class='stCard'>
        <img src="data:image/png;base64,{image_64}" alt='{title}'>
        <h3>{title}</h3>
        <p>{description}</p>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

##########################Logs###########################################

def add_user_log_event(page):
    os_base_path = os.path.dirname(os.path.realpath(__file__))
    config_file = "../utilities/config.yaml"
    config_file_path = os.path.join(os_base_path, config_file)
    with open(config_file_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    user_activity_logs_file = "../utilities/activity_logs.csv"
    user_activity_logs_file_path = os.path.join(os_base_path, user_activity_logs_file)

    username = st.session_state.username
    name = st.session_state.name
    email_address = st.session_state.email
    user_role = st.session_state.roles[0]
    user_logs = pd.read_csv(user_activity_logs_file_path)
    current_time = datetime.datetime.now()

    if f'{page}' not in st.session_state:
        st.session_state[f'{page}'] = False
    
    if st.session_state[f'{page}'] == False:
        d = pd.DataFrame({'dtg':current_time, 'username':username,
                        'name':name, 'email':email_address,
                        'role':user_role, 'page_accessed':page}, index=[0])
        query_data_new = pd.concat([user_logs,d], ignore_index=True)
        query_data_new.to_csv(user_activity_logs_file_path, index=False)


def add_registration_log_event(username, name, email):
    os_base_path = os.path.dirname(os.path.realpath(__file__))
    config_file = "../utilities/config.yaml"
    config_file_path = os.path.join(os_base_path, config_file)
    with open(config_file_path) as file:
        config = yaml.load(file, Loader=SafeLoader)
    
    registration_logs_file = "../utilities/registration_logs.csv"
    registration_logs_file_path = os.path.join(os_base_path, registration_logs_file)

    registration_logs = pd.read_csv(registration_logs_file_path)
    current_time = datetime.datetime.now()

    d = pd.DataFrame({'dtg':current_time, 'username':username,
                        'name':name, 'email':email}, index=[0])
    query_data_new = pd.concat([registration_logs,d], ignore_index=True)
    query_data_new.to_csv(registration_logs_file_path, index=False) 

def top_banner():

    hide_streamlit_style = '''
        <style>
            .stApp [data-testid=stHeader]{display: none;}
            div.block-container {padding-top: 0rem; z-index: 9999; !important}
        </style>
    '''
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown(
        '''
        <style>
        .banner {
            background-color: green;
            padding: .01px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            color: black;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 9999;
            object-fit: cover;   
        }
        </style>
    ''',
    unsafe_allow_html = True
    )

    st.markdown('<div class="banner">Add your top banner text here</div>', unsafe_allow_html=True)

def bottom_banner():
    st.markdown(
        '''
        <style>
        .footer {
            background-color: green;
            padding: .01px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            color: black;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            z-index: 9999;
            object-fit: cover;   
        }
        </style>
    ''',
    unsafe_allow_html = True
    )
    st.markdown('<div class="footer">Add your top banner text here</div>', unsafe_allow_html=True)