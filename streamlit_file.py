import streamlit as st
st.set_page_config(page_title="LOGIN")


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'


# Main screen
if st.session_state.page == 'main':
    st.header("Login Form")

    st.text_input("Enter your EMAIL")
    st.text_input("Enter your PASSWORD",type="password")

    button1=st.button("LOGIN")
    button2=st.button("SIGN UP")
    if button2:
        st.session_state.page = 'next'

# Next screen
elif st.session_state.page == 'next':
    st.header("SIGN UP")

    st.text_input("Enter your NAME")
    st.text_input("Enter your EMAIL")
    st.text_input("Create your PASSWORD",type="password")
    st.text_input("Confirm your PASSWORD",type="password")

    button=st.button("SIGN UP")
    if button:
        st.session_state.page = 'main'
