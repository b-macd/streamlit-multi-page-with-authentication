from utilities.pagesetup import *
import streamlit as st
from streamlit_card import card
import base64
import os

###############################################################
#              Initial Page Configuration                     #
###############################################################
###########App Settings#####################
tool_name = "Landing Page"
about_tool = ''
############################################

add_user_log_event(tool_name)

############Building Sidebar################
with st.sidebar:
    idsg_load_logos()
    st.write(about_tool)
    idsg_load_buttons()

###############################################################
#              Application Specific Code                      #
###############################################################
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; padding: 10px;">
        <h1 style = "text-align: center; margin: 0;">Intelligence Data Solutions Group</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### Mission Statement
            put statement here

        ### Value Statement
            put value statement here

        Select a tool from below:
        """
    )

col1, col2, col3 = st.columns(3)

def create_image_for_card(image_base_path, image_path):
    with open(os.path.join(image_base_path, image_path), "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")
    return data

with col1:
    #container1 = st.container()
    #with container1:
    has_clicked_1st_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "1st Card",
        text = "This is the card for the 1st Application",
        styles={
        "card": {
            'aspect-ratio': "1 / 1",
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            #"min-height":"200px",
            #"height": "100%", # <- if you want to set the card height to 300px
            #"borderRadius": "0px",
            "margin":"40px"
        }
    }
    )

    if has_clicked_1st_card:
        st.switch_page("application_pages/Example_Application_1.py")

    has_clicked_4th_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "4th Card",
        text = "This is the card for the 4th Application",
        styles={
        "card": {
                'aspect-ratio': "1 / 1",
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                #"min-height":"200px",
                #"height": "100%" # <- if you want to set the card height to 300px
                #"borderRadius": "0px",
                "margin":"40px"
            }
    }
    )

    if has_clicked_4th_card:
        st.switch_page("application_pages/Example_Application_4.py")

with col2:
    has_clicked_2nd_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "2nd Card",
        text = "This is the card for the 2nd Application",
        styles={
        "card": {
                'aspect-ratio': "1 / 1",
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                #"min-height":"200px",
                #"height": "100%" # <- if you want to set the card height to 300px
                #"borderRadius": "0px",
                "margin":"40px"
            }
    }
    )

    if has_clicked_2nd_card:
        st.switch_page("application_pages/Example_Application_2.py")

    has_clicked_5th_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "5th Card",
        text = "This is the card for the 5th Application",
        styles={
        "card": {
                'aspect-ratio': "1 / 1",
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                #"min-height":"200px",
                #"height": "100%" # <- if you want to set the card height to 300px
                #"borderRadius": "0px",
                "margin":"40px"
            }
    }
    )

    if has_clicked_5th_card:
        st.switch_page("application_pages/Example_Application_5.py")

with col3:
    has_clicked_3rd_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "3rd Card",
        text = "This is the card for the 3rd Application",
        styles={
        "card": {
                'aspect-ratio': "1 / 1",
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                #"min-height":"200px",
                #"height": "100%" # <- if you want to set the card height to 300px
                #"borderRadius": "0px",
                "margin":"40px"
            }
    }
    )

    if has_clicked_3rd_card:
        st.switch_page("application_pages/Example_Application_3.py")

    has_clicked_6th_card = card(
        image = create_image_for_card(image_base_path, "../images/IDSG Gray Logo-cropped.png"),
        title = "6th Card",
        text = "This is the card for the 6th Application",
        styles={
        "card": {
                'aspect-ratio': "1 / 1",
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                #"min-height":"200px",
                #"height": "100%" # <- if you want to set the card height to 300px
                #"borderRadius": "0px",
                "margin":"40px"
            }
    }
    )

    if has_clicked_6th_card:
        st.switch_page("application_pages/Example_Application_6.py")