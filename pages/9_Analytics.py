import streamlit as st
from google.cloud import firestore
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plts
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
cat_analytics={"Clothing":0,"Food":0,"Other":0}
for dict in data_from_db.values():
    cat=dict["Expense category"]
    cat_analytics[cat]=cat_analytics[cat]+int(dict["Expense amount"])
fig, ax=plts.subplots()
ax.pie(cat_analytics.values(),labels=cat_analytics.keys(),radius=0.5) 
st.pyplot(fig)

#line chart based on the date
choice=st.selectbox("Choose which graph you want to plot against total expenses",("Expense Date","Expense category"))
bar_analytics={}
if choice=="Expense Date":
    for date in expense_date_list:
        bar_analytics[date]=0
if choice=="Expense category":
    for cat in expense_category_list:
        bar_analytics[cat]=0
for dict in data_from_db.values():
    value=dict[choice]
    bar_analytics[value]=bar_analytics[value]+int(dict["Expense amount"])
st.bar_chart(bar_analytics)



  
