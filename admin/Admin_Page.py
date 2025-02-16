import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

config_file_path = st.secrets.config_file_path
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)


st.title('This is the Admin Page')

st.divider()


user_name = st.selectbox('Choose a user', options= config['credentials']['usernames'].keys())

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

if st.toggle('Change user role'):
    new_role = st.selectbox('Available roles', options=['general user', 'admin'])
    change_role = st.button('Make Change')
    if change_role:
        config['credentials']['usernames'][user_name]['roles'][0] = new_role
        with open(config_file_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.rerun()



