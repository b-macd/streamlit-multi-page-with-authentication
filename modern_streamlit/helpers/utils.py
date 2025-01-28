import streamlit as st

# not in use right now, but will ultimately be used to control which pages are available by user role
def general_user_menu_options():
    pages = {
        "Your account": [
            st.Page("pages/App_1.py", title="App 1"),
            st.Page("manage_account.py", title="Manage your account"),
        ],
        "Resources": [
            st.Page("learn.py", title="Learn about us"),
            st.Page("trial.py", title="Try it out"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()

def admin_menu_options():
    pages = {
        "Your account": [
            st.Page("pages/App_1.py", title="App 1"),
            st.Page("manage_account.py", title="Manage your account"),
        ],
        "Resources": [
            st.Page("learn.py", title="Learn about us"),
            st.Page("trial.py", title="Try it out"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()