import streamlit as st
from google.cloud import firestore
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Initialize Firestore
db = firestore.Client.from_service_account_json("firestone_key.json")
users_ref = db.collection('Banking System')

# Fetch data from Firestore
data_from_db = {}
for doc in users_ref.stream():
    data_from_db[doc.id] = doc.to_dict()

# Convert data to a pandas DataFrame
dataframe = pd.DataFrame(data_from_db.values())
# Display the DataFrame in Streamlit's data editor
st.data_editor(dataframe, key='editable_dataframe')

#Create a dictionary with serial numbers with corresponding doc id
id_dict={}
i=0
for id in data_from_db:
    id_dict[str(i)]=id
    i+=1

# Allow the user to select a document to update
doc_id = st.selectbox('Select Serial Number to Delete permanently', options=id_dict.keys())

# Display current data for the selected document
if doc_id:
    doc_data = data_from_db[id_dict[doc_id]]
    st.write('Current Data:', doc_data)
if st.button("Delete this expense"):
    db.collection("Banking System").document(id_dict[doc_id]).delete()  
    st.error("The expense has been sucessfully deleted")