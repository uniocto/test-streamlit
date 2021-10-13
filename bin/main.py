import state
from pages import Pages
import streamlit as st


st.set_page_config(
    page_title="ML Simlation app",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "",
        "Report a bug": "",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


query_params = st.experimental_get_query_params()
app_state = st.experimental_get_query_params()

session_state = state.get(page_query_params=query_params)
page_query_params = session_state.page_query_params

default_index = (
    Pages.page_names.index(app_state["page"])
    if "page" in app_state and app_state["page"] in Pages.page_names
    else 0
)
set_page = st.sidebar.radio("Menu", Pages.page_names, index=default_index)
app_state["page"] = set_page

Pages.pageComponents[Pages.page_names.index(set_page)].render(app_state)

st.experimental_set_query_params(**app_state)
