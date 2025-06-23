import streamlit as st
import custom_file as cf
import password_strength as ps
import re

st.set_page_config(page_title="LOGIN")


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'


# Main screen
if st.session_state.page == 'main':
    st.header("Login Form")

    email=st.text_input("Enter your EMAIL")
    password=st.text_input("Enter your PASSWORD",type="password")


    if st.button("LOGIN"):
        if not email or not password:
            st.error("Please enter both email and password!")
            st.stop()
        if cf.check_user(email,password):
            st.success("Login successful!")
            st.empty()
        elif cf.check_user(email,password) == False:
            st.error("Invalid email or password!")    
    if st.button("SIGN UP"):
        st.session_state.page = 'next'

# Next screen
elif st.session_state.page == 'next':
    st.header("SIGN UP")
    name=st.text_input("Enter your NAME")
    email=st.text_input("Enter your EMAIL")
    password=st.text_input("Create your PASSWORD",type="password")
    if password:
        if ps.password_strength(password) != True:
            st.error(ps.password_strength(password))
            st.stop()
    confirm_password=st.text_input("Confirm your PASSWORD",type="password")
    if confirm_password:
        if password != confirm_password:
            st.error("Passwords do not match!")
            st.stop() 
    
    if st.button("SIGN UP"):
        if name and email and password and confirm_password:
            cf.insert_user(email, name, password)
            st.success("User created successfully!")
            st.session_state.page = 'main'
        else:
            st.error("Please fill in all fields!")    
