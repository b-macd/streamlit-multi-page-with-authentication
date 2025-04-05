import streamlit as st
import streamlit_authenticator as stauth
from utilities.pagesetup import *
import yaml
from yaml.loader import SafeLoader
import os

st.set_page_config(layout="wide")
# Initialize session state roles and load configuration.
# 1. Check if 'roles' is not in the Streamlit session state:
#    - If 'roles' is not present, initialize it with [None].  
# 2. Load configuration file:
#    - Retrieve the configuration file path from Streamlit secrets.
#    - Open and load the configuration file using the SafeLoader from the YAML library.
# 3. Create an authenticator instance:
#    - Initialize the authenticator object using credentials, cookie name, cookie key, and cookie expiry days from the configuration file.
# Code:
# Step 1: Initialize session state roles
if "roles" not in st.session_state:
    st.session_state.roles = [None]
# Step 2: Load configuration file
os_base_path = os.path.dirname(os.path.realpath(__file__))

config_file = "utilities/config.yaml"
config_file_path = os.path.join(os_base_path, config_file)
with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)
# Step 3: Create an authenticator instance
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def login():
    """
    This function handles user login using the Streamlit library and an authenticator object.
    It prompts the user to enter their username and password, provides an option for new users to register,
    and updates the configuration file upon successful login.

    Parameters:
    None

    Returns:
    None

    Behavior:
    1. The function attempts to log in the user using the authenticator object.
    2. It displays a warning message prompting the user to enter their username and password.
    3. It provides a button for new users to register, invoking the registration() function if clicked.
    4. The configuration file is updated by writing to the config file path.
    5. If the authentication status is successful, a success message is displayed, and the page is reloaded.
    6. If the authentication status is false, an error message is displayed indicating incorrect username/password.
    7. Any exceptions during the process are caught and displayed as error messages.

    Example Usage:
    # Call the login function to display the login form and handle user authentication
    login()
    """
    try:
        authenticator.login()
        #Sst.warning('Please enter your username and password')
        with open(config_file_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False) 
        if st.session_state['authentication_status']:
            st.success('Login Successfull!')
            st.rerun()
        elif st.session_state['authentication_status'] is False:
            st.error('Username/password is incorrect')
            if st.button(label="New User? Click Here to Register"):
                st.session_state.roles[0] = "New User"
                st.rerun()
            elif st.button(label="Forgot Password? Click Here to Reset"):
                st.session_state.roles[0] = "Password Reset"
                st.rerun()
        elif st.session_state['authentication_status'] is None:
            st.warning("Please enter your username and password")
            if st.button(label="New User? Click Here to Register"):
                st.session_state.roles[0] = "New User"
                st.rerun()
            elif st.button(label="Forgot Password? Click Here to Reset"):
                st.session_state.roles[0] = "Password Reset"
                st.rerun()

    except Exception as e:
        st.error(e)

def logout():
    """
    This function handles user logout using the Streamlit library. It clears all session state keys and reloads the page.

    Parameters:
    None

    Returns:
    None

    Behavior:
    1. The function retrieves a list of all keys in the Streamlit session state.
    2. It iterates through the list of keys and removes each key from the session state.
    3. The function calls st.rerun() to reload the page, effectively logging the user out.

    Example Usage:
    # Call the logout function to log the user out and clear session state
    logout()
    """
    with open(config_file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False) 
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)
    st.rerun()

def registration():
    """
    This function handles the registration of a new user using the Streamlit library and an authenticator object.
    It registers the user with the specified roles and updates the configuration file upon successful registration.

    Parameters:
    None

    Returns:
    None

    Behavior:
    1. The function attempts to register a new user with the role 'general user' using the authenticator object.
    2. If the registration is successful, the email, username, and name of the registered user are returned.
    3. A success message is displayed using Streamlit's st.success method.
    4. The configuration file is updated with the new user information by writing to the config file path.
    5. If an exception occurs during registration, it is caught and displayed using Streamlit's st.error method.

    Example Usage:
    # Call the registration function to display the registration form and handle user registration
    registration()
    """
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        try:
            email_of_registered_user, \
            username_of_registered_user, \
            name_of_registered_user = authenticator.register_user(roles=['general user'])
            if email_of_registered_user:
                st.success('User registered successfully')
                with open(config_file_path, 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                add_registration_log_event(username_of_registered_user, name_of_registered_user, email_of_registered_user)
                logout()
        except Exception as e:
            st.error(e)

def reset_password():
    """
    This function creates a form for resetting a user's password using the Streamlit library.
    It verifies the provided username, email, first name, and last name against stored credentials,
    and if they match, allows the user to set a new password.

    Parameters:
    None

    Returns:
    None

    Form Fields:
    - Username: The username of the user requesting the password reset.
    - Email: The email address associated with the username.
    - First Name: The first name of the user.
    - Last Name: The last name of the user.
    - New Password: The new password to be set (entered as a password field).
    - Confirm Password: The confirmation of the new password (entered as a password field).

    Behavior:
    1. The function checks if the provided username exists in the stored credentials.
    2. It verifies that the provided email, first name, and last name match the stored information for the username.
    3. If the new password and confirmation password match, the new password is hashed and updated in the stored credentials.
    4. A success message is displayed if the password is reset successfully.
    5. Error messages are displayed for mismatched passwords, incorrect user information, or non-existent usernames.

    Example Usage:
    # Call the reset_password function to display the form and handle password reset
    reset_password()
    """
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("Reset Password")
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
# Initialize role and define Streamlit pages.

# 1. Retrieve the role from the Streamlit session state:
#    - Set the variable 'role' to the first element in the 'roles' list from the session state.  
# 2. Define Streamlit pages:
#    - Create a new page for user registration with the title 'New User Registration' and a person_add icon.
#    - Create a new page for logging out with the title 'Log out' and a logout icon.
#    - Create a new page for password reset with the title 'Reset Password'.
#    - Optionally, create a page for settings (commented out in the code).
#    - Create a home page with the title 'Home Page' and a house icon, set as the default if the role is 'general user' or 'admin'.
#    - Create a page for 'App 1' with the title 'App 1' and a help icon.
#    - Create a page for 'App 2' with the title 'App 2' and a healing icon.
#    - Create an admin page with the title 'Admin Page' and a security icon.
# 3. Group pages into categories:
#    - Assign logout_page, home_page, and reset_password_page to the 'account_page' list.
#    - Assign app_1 and app_2 to the 'application_pages' list.
#    - Assign admin_1 to the 'admin_pages' list.
# Code:
# Step 1: Retrieve the role from the session state
role = st.session_state.roles[0]
# Step 2: Define Streamlit pages
registration_page = st.Page(registration, 
    title='New User Registration', 
    icon = ':material/person_add:'
)
logout_page = st.Page(logout, 
    title="Log out", 
    icon=":material/logout:"
)
password_reset_page = st.Page(reset_password, 
    title='Reset Password', 
    icon = ':material/lock_reset:'
)
profile_page = st.Page(
    "utility_pages/User_Profile.py",
    title="User Profile",
    icon=":material/person:"
)
admin_1 = st.Page(
    "utility_pages/Admin_Page.py",
    title="Admin Page",
    icon=":material/security:",
)
home_page = st.Page(
    "utility_pages/Home_Page.py",
    title="Home Page",
    icon=":material/house:",
    default=(role in ["general user", 'admin']),
)
app_1 = st.Page(
    "application_pages/Example_Application_1.py",
    title="App 1",
    icon=":material/help:",
)
app_2 = st.Page(
    "application_pages/Example_Application_2.py",
    title="App 2",
    icon=":material/healing:",
)
app_3 = st.Page(
    "application_pages/Example_Application_3.py",
    title="App 3",
    icon=":material/analytics:",
)
app_4 = st.Page(
    "application_pages/Example_Application_4.py",
    title="App 4",
    icon=":material/anchor:",
)
app_5 = st.Page(
    "application_pages/Example_Application_5.py",
    title="App 5",
    icon=":material/area_chart:",
)
app_6 = st.Page(
    "application_pages/Example_Application_6.py",
    title="App 6",
    icon=":material/assistant:",
)


# Step 3: Group pages into categories
landing_page = [home_page]
account_pages = [profile_page, logout_page]
application_pages = [app_1, app_2, app_3, app_4, app_5, app_6]
admin_pages = [admin_1]

# Define and manage page navigation based on user roles and authentication status.
# 1. Initialize page dictionary:
#    - Create an empty dictionary 'page_dict'.
# 2. Assign pages based on user roles:
#    - If the user's role is 'general user' or 'admin', add 'application_pages' to 'page_dict' under the key "Applications".
#    - If the user's role is 'admin', add 'admin_pages' to 'page_dict' under the key "Admin".
# 3. Handle page navigation based on authentication status:
#    - If the user is authenticated ('authentication_status' is True), create the navigation object 'pg' with "Account" pages and additional pages from 'page_dict'.
#    - If the user is not authenticated ('authentication_status' is None), create the navigation object 'pg' with the login page only.
# 4. Run the page navigation:
#    - Call the run() method on the 'pg' navigation object to display the appropriate page.
# Code:
# Step 1: Initialize page dictionary
page_dict = {}
# Step 2: Assign pages based on user roles
if st.session_state.roles[0] in ["general user", "admin"]:
    page_dict["Applications"] = application_pages
    page_dict["Account"] = account_pages
if st.session_state.roles[0] == "admin":
    page_dict["Admin"] = admin_pages
# Step 3: Handle page navigation based on user roles
if st.session_state['roles'][0] is not None:
    if st.session_state['roles'][0] == "New User":
        pg = st.navigation([st.Page(registration)])
    elif st.session_state['roles'][0] == "Password Reset":
        pg = st.navigation([st.Page(reset_password)])
    else:
        pg = st.navigation({"Home Page": landing_page} | page_dict)
elif st.session_state['roles'][0] is None:
    pg = st.navigation([st.Page(login)])
# Step 4: Run the page navigation
pg.run()