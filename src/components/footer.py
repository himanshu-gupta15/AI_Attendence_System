import streamlit as st

def footer_home():

   

    st.markdown(
        f"<div style='margin-top:2rem;display:flex;gap:6px;justify-content:center;align-items:center;'>"
        "<p style='margin:0;'>Created with ❤️ by</p>"
        "<p style='margin:0;font-weight:bold;'>Himanshu Gupta</p>"
        "</div>",
        unsafe_allow_html=True,
    )


def footer_dashboard():

    

    st.markdown(
        f"<div style='margin-top:2rem;display:flex;gap:6px;justify-content:center;align-items:center;'>"
        "<p style='margin:0;font-weight:bold;color:black;'>Created with ❤️ by</p>"
        "<p style='margin:0;font-weight:bold;'>Himanshu Gupta</p>"
        "</div>",
        unsafe_allow_html=True,
    )