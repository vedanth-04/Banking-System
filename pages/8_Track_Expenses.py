import streamlit as st
from google.cloud import firestore
import pandas as pd
from PIL import Image
st.image(Image.open("Tracking_photo.png"),width=400)
def get_data(data_from_db,choice,choice2):
    listt=[]
    x=data_from_db.values()
    for i in x:
        if(i[choice]==choice2):
            listt.append(i)
    return listt
db = firestore.Client.from_service_account_json("firestone_key.json")
users_ref = db.collection('Banking System')
data_from_db={}
expense_date_list=[]
expense_category_list=[]
for doc in users_ref.stream():
    data_from_db[doc.id]=doc.to_dict()
    if(doc.to_dict()["Expense Date"] not in expense_date_list):
        expense_date_list.append(doc.to_dict()["Expense Date"])
    if(doc.to_dict()["Expense category"] not in expense_category_list):
        expense_category_list.append(doc.to_dict()["Expense category"])
choice=st.selectbox("How do you want to track your Expenses?",("Expense Date","Expense category"))
if(choice=="Expense Date"):
    choice_2=st.selectbox("Choose which date",expense_date_list)
    if st.button("Track"):
            result=get_data(data_from_db,choice,choice_2) 
            data=pd.DataFrame(result)
            st.data_editor(data)
if(choice=="Expense category"):
        choice_2=st.selectbox("Choose which cateogy expense",(expense_category_list))
        if st.button("Track"):
            result=get_data(data_from_db,choice,choice_2)
            data=pd.DataFrame(result)
            st.data_editor(data)