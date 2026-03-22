import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de vehículos en EE. UU.")

st.write("---")
st.write("Selecciona las gráficas:")

if st.checkbox("Mostrar histograma"):
    st.write("Histograma de odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar dispersión"):
    st.write("Precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

