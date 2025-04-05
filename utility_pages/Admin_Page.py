from utilities.pagesetup import *
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
import datetime
import pandas as pd

###############################################################
#                      File Mapping                           #
###############################################################
os_base_path = os.path.dirname(os.path.realpath(__file__))
config_file = "../utilities/config.yaml"
config_file_path = os.path.join(os_base_path, config_file)
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)
registration_logs_file = "../utilities/registration_logs.csv"
user_activity_logs_file = "../utilities/activity_logs.csv"
registration_logs_file_path = os.path.join(os_base_path, registration_logs_file)
user_activity_logs_file_path = os.path.join(os_base_path, user_activity_logs_file)
###############################################################
#              Initial Page Configuration                     #
###############################################################
tool_name = 'Admin Page'
about_tool = 'This is an example of how you would set up an application.'

add_user_log_event(tool_name)

with st.sidebar:
    idsg_load_logos()
    st.write(about_tool)
    idsg_load_buttons()

load_tool_header(title=tool_name)

st.divider()

###############################################################
#              Application Specific Code                      #
###############################################################

admin_options = st.radio("Admin Options" , ["Users and Roles", "Logs"], index= 0, horizontal=True)


if admin_options == "Users and Roles":
    number_of_users = len(list(config['credentials']['usernames'].keys()))
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.subheader(f"There are currently {number_of_users} users registered")
    col1, col2, col3 = st.columns(3)
    with col1:
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
    col1, col2, col3 = st.columns(3)
    with col1:
        advanced_options = st.expander("Advanced Options")
        with advanced_options:
            user_options = st.radio("User Specific Options", ["Modify User Roles", "Remove User"], index=0, horizontal=True)
            if user_options == "Modify User Roles":
                new_role = st.selectbox("Available Roles", options=["general user", "admin"])
                change_role = st.button("Make Change")
                if change_role:
                    config["credentials"]["usernames"][user_name]["roles"][0] = new_role
                    with open(config_file_path, 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.rerun()
            else:
                remove_user = st.button("Remove User")
                if remove_user:
                    del config["credentials"]["usernames"][user_name]
                    with open(config_file_path, 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.rerun()           

else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("User Logs")
        users_df = pd.read_csv(user_activity_logs_file_path)
        st.dataframe(users_df)
    with col2:
        st.subheader("Registration Logs")
        regs_df = pd.read_csv(registration_logs_file_path)
        st.dataframe(regs_df)