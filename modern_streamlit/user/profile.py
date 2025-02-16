import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

st.title('Profile')


st.divider()

config_file_path = st.secrets.config_file_path
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

user_name = st.session_state.username

first_name = config['credentials']['usernames'][user_name]['first_name']
last_name = config['credentials']['usernames'][user_name]['last_name']
email_address = config['credentials']['usernames'][user_name]['email']
user_role = config['credentials']['usernames'][user_name]['roles'][0]
#st.write(f'{first_name} {last_name} \n {user_name} \n {email_address}')
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
                ##### Name:  
                {first_name} {last_name}  
                ##### Email:  
                {email_address}
                """
                )
with col2:
    st.markdown(f""" 
            ##### Username:  
            {user_name}  
            ##### Role:
            {user_role}
            """
            )