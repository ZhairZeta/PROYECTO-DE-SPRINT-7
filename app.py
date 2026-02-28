import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de página
st.set_page_config(page_title="Dashboard de Vehículos", page_icon="🚗", layout="wide")

# Título principal
st.title("🚗 Dashboard de Análisis de Vehículos Usados")
st.markdown("Análisis exploratorio de datos de anuncios de vehículos")


# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df


df = load_data()

# Mostrar info básica
st.header("📊 Información del Dataset")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total de vehículos", f"{df.shape[0]:,}")
with col2:
    st.metric("Total de columnas", df.shape[1])

# --- BOTÓN 1: HISTOGRAMA ---
st.header("📈 Histograma")
st.write("Haz clic para ver la distribución de precios:")

hist_button = st.button("Construir Histograma", type="primary")

if hist_button:
    st.write("### Histograma de Precios de Vehículos")
    fig = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Distribución de Precios",
        labels={"price": "Precio (USD)", "count": "Cantidad de vehículos"},
    )
    st.plotly_chart(fig, use_container_width=True)

# --- BOTÓN 2: GRÁFICO DE DISPERSIÓN ---
st.header("🔵 Gráfico de Dispersión")
st.write("Haz clic para ver la relación entre odómetro y precio:")

scatter_button = st.button("Construir Gráfico de Dispersión")

if scatter_button:
    st.write("### Relación: Odómetro vs Precio")
    fig = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Odómetro vs Precio",
        labels={"odometer": "Odómetro (millas)", "price": "Precio (USD)"},
    )
    st.plotly_chart(fig, use_container_width=True)

# --- CHECKBOX OPCIONAL ---
st.sidebar.header("⚙️ Opciones")
show_data = st.sidebar.checkbox("Mostrar primeros 10 registros")

if show_data:
    st.write("### Primeros 10 vehículos:")
    st.dataframe(df.head(10))

# Footer
st.markdown("---")
st.caption("Dashboard creado con Streamlit | Dataset: vehicles_us.csv")
