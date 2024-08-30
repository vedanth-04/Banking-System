import streamlit as st
from PIL import Image
st.image(Image.open("welcome.jpg"),width=600)
st.title("EXPENSE MANGAMENT SYSTEM")
st.markdown(":red[What can you do with this system?]")
st.page_link(page="pages/7_Details_Entering.py",label="🟢Enter expenses ")
st.page_link(page="pages/8_Track_Expenses.py",label="🔍Track expenses ")
st.page_link(page="pages/10_Update_Expense.py",label="🟠Update existing expenses")
st.page_link(page="pages/11_Delete_Expenses.py",label="🗑️Delete existing expenses")
st.page_link(page="pages/9_Analytics.py",label="📈Check expense analytics")