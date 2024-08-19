import streamlit as st
from PIL import Image
st.title("HELLO WELCOME TO MY NEW PAGE ")
st.header("This is a parent")
st.subheader("This is a child")
st.text("This is a normal text command")
st.markdown("This is a markdown header")
st.success("Sucess-Green colour is displayed")
st.error("error-Red colour is displayed")
st.info("Info-Blue colour is displayed")
st.warning("Warning-yellow colour is displayed")
img=Image.open("imagie.jpg")  
st.image(img,width=500)
if st.checkbox("tick/not tick"):
    st.text("You have checked the tickbox")     