import streamlit as st
import pandas as pd
import numpy as np

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("Police1.csv")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco,from the year 2018 to 2020, with details from each case suach as date, day of the week, police district, neighborhood')

mapa = pd.DataFrame()

mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of the Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()

