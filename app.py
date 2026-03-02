import pandas as pd
import plotly.graph_objects as go
import streamlit as st

"""Aplicación web para análisis de vehículos usados."""

# Título de la aplicación (encabezado requerido)
st.header("Análisis de Vehículos Usados")

# Leer los datos
car_data = pd.read_csv("vehicles_us.csv")

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )
    # Crear histograma con plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos")
    # Crear gráfico de dispersión con plotly.graph_objects
    fig = go.Figure(
        data=[go.Scatter(x=car_data["odometer"], y=car_data["price"], mode="markers")]
    )
    fig.update_layout(title_text="Relación entre Odómetro y Precio")
    st.plotly_chart(fig, use_container_width=True)
