import streamlit as st
import time

import df as d


import df as aa


import sqlite3
db = sqlite3.connect("dd.db")
db.execute("create table if not exists dda (name text, Phonenumber integer)")


st.set_page_config(page_title="4S admin websitee")
with st.container():
    st.image(
            'https://cdn.discordapp.com/attachments/1049396625669361734/1057330425934139402/Untitled-1-removebg-preview.png')
    st.header("For resisting your name please fill the following ")

with st.container():
    st.write("##")
    def ac():
        while True:

            for row in db.execute('select name from dda'):

                st.write(f"Name: {row}")
                time.sleep(.3)
                q = db.cursor()
                aa = q.execute("delete from dda ")
                db.commit()
                print(aa.rowcount, "record(s) deleted")
            else:
                pass





    c = st.button("done")
    if c == True:
        command=ac()




        # for roww in d.db.execute("select Phonenumber from dda "):
        # b = print(roww)

        # st.write(f"Name: {b}")






    st.write("##")
    st.write("##")
    st.write("##")
    st.write("This website is created and supported by 4S Group")
    # d.db.close()

