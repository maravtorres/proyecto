import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.title("🚗 Análisis de vehículos en EE. UU.")
st.write("Explora la relación entre el precio y el kilometraje de los vehículos.")

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

price_range = st.slider(
    "Selecciona rango de precio",
    int(car_data["price"].min()),
    int(car_data["price"].max()),
    (5000, 20000)
)

filtered_data = car_data[
    (car_data["price"] >= price_range[0]) &
    (car_data["price"] <= price_range[1])
]
st.write("---")
st.subheader("Gráficas interactivas")

type_option = st.selectbox(
    "Selecciona tipo de vehículo",
    car_data["type"].dropna().unique()
)

filtered_data = filtered_data[filtered_data["type"] == type_option]
fig = px.histogram(filtered_data, x="odometer")
fig = px.scatter(filtered_data, x="odometer", y="price")

st.sidebar.header("Filtros")
price_range = st.sidebar.slider(...)
type_option = st.sidebar.selectbox(...)