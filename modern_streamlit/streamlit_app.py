import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

if "roles" not in st.session_state:
    st.session_state.roles = [None]


config_file_path = st.secrets.config_file_path
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def registration():

    try:
        email_of_registered_user, \
        username_of_registered_user, \
        name_of_registered_user = authenticator.register_user(roles=['general user'])
        if email_of_registered_user:
            st.success('User registered successfully')
            with open(config_file_path, 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)

def login():

    try:
        authenticator.login()
        st.warning('Please enter your username and password')
        if st.button(label="New User? Click Here to Register"):
                registration()
        with open(config_file_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False) 
        if st.session_state['authentication_status']:
            st.success('Login Successfull!')
            st.rerun()
        elif st.session_state['authentication_status'] is False:
            st.error('Username/password is incorrect')
    except Exception as e:
        st.error(e)

def logout():
    #authenticator.logout()
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)
    st.rerun()


role = st.session_state.roles[0]

registration_page = st.Page(registration, title='New User Registration', icon = ':material/person_add:')
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
#settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
home_page  = st.Page("landingpage/home_page.py",
    title="Home Page",
    icon="🏠",
    default=(role in ["general user", 'admin']),
)
app_1 = st.Page(
    "applications/App_1.py",
    title="App 1",
    icon=":material/help:",
)
app_2 = st.Page(
    "applications/App_2.py",
    title="App 2",
    icon=":material/healing:",
)
admin_1 = st.Page(
    "admin/Admin_Page.py",
    title="Admin Page",
    icon=":material/security:",
)

account_page = [logout_page, home_page]
application_pages = [app_1, app_2]
admin_pages = [admin_1]

#st.title("Request manager")
#st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.roles[0] in ["general user", "admin"]:
    page_dict["Applications"] = application_pages
if st.session_state.roles[0] == "admin":
    page_dict["Admin"] = admin_pages


if st.session_state['authentication_status']:
    pg = st.navigation({"Account": account_page} | page_dict)
#elif st.session_state['authentication_status'] is False:
    #pg = st.navigation([st.Page(login)])
elif st.session_state['authentication_status'] is None:
    pg = st.navigation([st.Page(login)])

pg.run()