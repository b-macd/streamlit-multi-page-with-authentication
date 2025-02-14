import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

config_file_path = st.secrets.config_file_path
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)


if st.session_state['authentication_status']:
    st.switch_page('Home_Page.py')
else:    
    try:
        email_of_registered_user, \
        username_of_registered_user, \
        name_of_registered_user = authenticator.register_user(roles=['general user'])
        if email_of_registered_user:
            st.success('User registered successfully')
            with open(config_file_path, 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.switch_page('pages/User_Login.py')
    except Exception as e:
        st.error(e)