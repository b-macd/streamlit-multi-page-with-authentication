import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

config_file_path = st.secrets.config_file_path
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
    with open(config_file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)  
except Exception as e:
    st.error(e)

if st.session_state['authentication_status']:
    st.success('Login Successfull!')
    st.switch_page('Home_Page.py')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
    st.page_link('pages/User_Registration.py', label="New User? Click Here to Register")  
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
    st.page_link('pages/User_Registration.py', label="New User? Click Here to Register")  