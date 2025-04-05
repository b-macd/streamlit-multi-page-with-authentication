import streamlit as st
from utilities.pagesetup import *

###############################################################
#              Initial Page Configuration                     #
###############################################################
tool_name = "User Profile"
about_tool = ''

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

st.write(f"Name: {st.session_state.name}")
st.write(f"Username: {st.session_state.username}")
st.write(f"Email: {st.session_state.email}")
st.write(f"User Roles")
for role in st.session_state.roles:
    st.write(role)


