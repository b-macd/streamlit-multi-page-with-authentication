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

def reset_password():
    reset_pw_form = st.form('Reset Password')
    with reset_pw_form:
        username = st.text_input('Username')
        email = st.text_input('Email')
        first = st.text_input('First Name')
        last = st.text_input('Last Name')
        new_pw = st.text_input('New Password', type='password')
        confirm_new_pw = st.text_input('Confirm Password', type='password')
        if reset_pw_form.form_submit_button():     
            if username in config['credentials']['usernames']:
                adhoc_list = []
                for entry in config['credentials']['usernames'][username].values():
                    adhoc_list.append(entry) 
                #st.write(adhoc_list)  
                if email == adhoc_list[0] and first == adhoc_list[2] and last == adhoc_list[3]:
                    if confirm_new_pw == new_pw:
                        hashed_pw = stauth.Hasher.hash(new_pw) 
                        config['credentials']['usernames'][username]['password'] = hashed_pw
                        with open(config_file_path, 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)

                        st.success('Password Reset')
                    else:
                        st.error('Passwords do not match')  
                else:
                    st.error('The email, first name, or last name do not match our records')  

            else:
                st.error('That username does not exist')



role = st.session_state.roles[0]

registration_page = st.Page(registration, title='New User Registration', icon = ':material/person_add:')
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
reset_password_page = st.Page(reset_password, title='Reset Password')
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

account_page = [logout_page, home_page, reset_password_page]
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