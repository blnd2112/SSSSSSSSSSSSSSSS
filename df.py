import streamlit as st
import os
from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")



data = Deta(DETA_KEY)
db= data.Base("bb")

def insert_period(name, ph):
    return db.put({"Name": name, "Phone number": ph})

def fetch_all_period():
    res= db.fetch()
    return res.items

def get_period(period):
    return db.get(period)



