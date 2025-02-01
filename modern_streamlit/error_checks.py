import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def load_config(config_file_path):
    try:
        with open(config_file_path) as file:
            return yaml.load(file, Loader=SafeLoader)
    except Exception as e:
        st.error(f"Error loading config file: {e}")
        return None

def check_session_roles():
    if "roles" not in st.session_state:
        st.session_state.roles = [None]

def authenticate_user(config):
    try:
        return stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )
    except KeyError as e:
        st.error(f"Missing key in configuration: {e}")
        return None
    except Exception as e:
        st.error(f"Error during authentication setup: {e}")
        return None

def check_registration(authenticator, config_file_path, config):
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(roles=['general user'], captcha=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            with open(config_file_path, 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(f"Error during registration: {e}")

def check_login(authenticator, config_file_path, config):
    try:
        authenticator.login()
        st.warning('Please enter your username and password')
        if st.button(label="New User? Click Here to Register"):
                check_registration(authenticator, config_file_path, config)
        with open(config_file_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False) 
        if st.session_state['authentication_status']:
            st.success('Login Successful!')
            st.rerun()
        elif st.session_state['authentication_status'] is False:
            st.error('Username/password is incorrect')
    except Exception as e:
        st.error(f"Error during login: {e}")

def check_logout():
    try:
        keys = list(st.session_state.keys())
        for key in keys:
            st.session_state.pop(key)
        st.rerun()
    except Exception as e:
        st.error(f"Error during logout: {e}")

def check_reset_password(config, config_file_path):
    try:
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
    except Exception as e:
        st.error(f"Error during password reset: {e}")

def run_error_checks():
    config_file_path = st.secrets.get("config_file_path")
    if not config_file_path:
        st.error("Config file path not found in secrets")
        return

    config = load_config(config_file_path)
    if not config:
        return

    check_session_roles()

    authenticator = authenticate_user(config)
    if not authenticator:
        return

    check_registration(authenticator, config_file_path, config)
    check_login(authenticator, config_file_path, config)
    check_logout()
    check_reset_password(config, config_file_path)

    st.success("Error checks passed successfully")

if __name__ == "__main__":
    run_error_checks()
