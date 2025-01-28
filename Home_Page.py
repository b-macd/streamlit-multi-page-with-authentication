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
    config['cookie']['expiry_days'],
    config['cookie']['name'],
)

if st.session_state['authentication_status']:
    with st.sidebar:
        authenticator.logout()
        st.success('Login Successfull!')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.write(f'Current Role: *{st.session_state["roles"][0]}*')
elif st.session_state['authentication_status'] is False:
    st.switch_page('pages/User_Login.py')
elif st.session_state['authentication_status'] is None:
    st.switch_page('pages/User_Login.py')

st.title('This is the homepage')

st.divider()

st.page_link('pages/App_1.py', label='This is the link to App 1')

st.divider()

st.page_link('pages/App_2.py', label='This is the link to App 2')