import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de vehículos en EE. UU.")

# Botón para construir histograma
if st.button("Construir histograma"):
    st.write("Histograma de odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button("Construir gráfico de dispersión"):
    st.write("Precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Alternativa con casillas de verificación (opcional)
st.write("---")
st.write("O usar casillas de verificación:")
if st.checkbox("Mostrar histograma"):
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar dispersión"):
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
