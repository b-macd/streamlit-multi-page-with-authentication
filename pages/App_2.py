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
    with st.sidebar:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.write(f'Current Role: *{st.session_state["roles"][0]}*')
elif st.session_state['authentication_status'] is False:
    st.switch_page('pages/User_Login.py')
elif st.session_state['authentication_status'] is None:
    st.switch_page('pages/User_Login.py')

st.title('This is App 2')

st.divider()

