import streamlit as st
from utilities.pagesetup import *

###############################################################
#              Initial Page Configuration                     #
###############################################################
tool_name = "Example Application 4"
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
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('''
                This is where you would start adding in the code for your actual application.
                ''')