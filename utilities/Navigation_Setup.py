import streamlit as st

def admin_pages():
        admin_1 = st.Page(
        "utility_pages/Admin_Page.py",
        title="Admin Page",
        icon=":material/security:",
    )
        return admin_1

def account_pages():
    profile_page = st.Page(
        "utility_pages/User_Profile.py",
        title="User Profile",
        icon=":material/person:"
    )
    logout_page = st.Page(logout, 
        title="Log out", 
        icon=":material/logout:"
    )
    return profile_page, logout_page

def landing_page():
    home_page = st.Page(
        "utility_pages/Landing_Page.py",
        title="Your Group Name Here",
        icon=":material/house:",
        default=(role in ["general user", 'admin']),
    )
    return home_page

def registration_page():
    registration_page = st.Page(registration, 
        title='New User Registration', 
        icon = ':material/person_add:'
    )
    return registration_page

def password_reset_page():
    password_reset_page = st.Page(reset_password, 
        title='Reset Password', 
        icon = ':material/lock_reset:'
    )
    return password_reset_page

def application_pages():
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