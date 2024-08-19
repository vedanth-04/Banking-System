import streamlit as st
n1=st.text_input("Enter your first number",placeholder="Type here...")
n2=st.text_input("Enter your second number",placeholder="Type here...")
if st.button("Click me to add the two numbers"):
    result=int(n1)+int(n2)
    st.success(f"The sum of the following is {result}")
if st.button("Click me to multiply two numbers"):
    result=int(n1)*int(n2)
    st.success(f"The product of the following is {result}")