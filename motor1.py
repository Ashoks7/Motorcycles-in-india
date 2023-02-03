# Import packages

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

# Read file

bike = pd.read_csv("bike_dataset.csv")

# Add back ground image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.trakntell.com/wp-content/uploads/2021/04/bike-banner.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# Code for Button style 
import streamlit as st
primaryColor = st.get_option("theme.primaryColor")
s = f"""
<style>
div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

# Title of the page

st.title("Motorcycles in India")

# Add option menu

selected = option_menu(menu_title=None, options=["Analytics","Best bike","Top bikes","High end bike"], icons=["clipboard-data","award","capslock-fill","coin"], orientation="horizontal")

# Code for analytics page

if selected=="Analytics":
    option1 = st.selectbox(
    'Type of bike?',
    ('Electric Bike','Petrol Bike'))

    st.write('You selected:', option1)

    option2 = st.selectbox(
    'what u need?',
    ('mileage','price',"CC","weight_in_kg"))

    st.write('You selected:', option2)

    if st.button("show"):
       b1= bike[(bike["type_of_bike"]==option1)]
       fig=px.bar(x=b1["model_name"],y=b1[option2])
       st.write(b1)
       st.write(fig)

# Code for Best bike page

if selected=="Best bike":
    option3 = st.selectbox(
    'Type of bike?',
    ('Electric Bike','Petrol Bike'))

    st.write('You selected:', option3)

    option4 = st.selectbox(
    'what u need?',
    ('mileage','top_speed',"CC","weight_in_kg"))

    st.write('You selected:', option4)

    option5 = st.slider(
    'Price range?',min_value=35000, max_value=9990000)

    st.write('You selected:', option5)

    if st.button("show"):
       bb1 = bike[(bike["type_of_bike"]==option3)&(bike["price"]<option5)]
       st.write(bb1[["model_name","price","mileage","top_speed","weight_in_kg"]][bb1[option4]==bb1[option4].max()])

# Code for top bike page

if selected=="Top bikes":
    option7 = st.selectbox(
    'Type of bike?',
    ('Electric Bike','Petrol Bike'))

    st.write('You selected:', option7)

    option8 = st.selectbox(
    'what u need?',
    ('mileage','top_speed',"CC","weight_in_kg"))

    st.write('You selected:', option8)

    if st.button("show"):
        bb1 = bike[(bike["type_of_bike"]==option7)]
        st.write(bb1.sort_values(by=[option8], ascending=False).head(5))

# Code for high end bike 
if selected=="High end bike":
    option6 = st.selectbox(
    'Type of bike?',
    ('Electric Bike','Petrol Bike'))

    st.write('You selected:', option6)

    if st.button("show"):
       bb1 = bike[(bike["type_of_bike"]==option6)]
       st.write(bb1[["model_name","price","mileage","top_speed","weight_in_kg"]][bb1["price"]==bb1["price"].max()])
