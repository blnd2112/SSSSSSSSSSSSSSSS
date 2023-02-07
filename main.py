import streamlit as st
from deta import Deta
from PIL import Image


# Data to be written to Deta Base
with st.form("form"):
    Name = st.text_input("Your name")
    ph = st.text_input("Your Phone number")
    submitted = st.form_submit_button("done")


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("bb")
db = deta.Base("bb")
image = Image.open('b.png')
# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"Name": Name, "Phone number": ph})

