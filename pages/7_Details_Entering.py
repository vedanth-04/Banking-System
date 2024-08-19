import streamlit as st
from google.cloud import firestore
def write_name_to_firestore(data):
    # Reference to the Firestore collection
    collection_ref = db.collection("Banking System")
        
    # Create a new document with the given name
    doc_ref = collection_ref.add(data)
        
    return f"Name written with document ID:"
db = firestore.Client.from_service_account_json("firestone_key.json")
expense_amt=st.text_input("Enter expsense amount",placeholder="Type here")
expense_name=st.text_input("Enter expsense name",placeholder="Type here")
expense_datee=st.date_input("Enter the date of the expense")
expense_cateogry=st.selectbox("Enter the category",("Food","Clothing","Other"))
expense_record={"Expense amount":expense_amt,"Expense Name":expense_name,"Expense Date":str(expense_datee),"Expense category":expense_cateogry}
if st.button("Click to submit"):

    write_name_to_firestore(expense_record)

