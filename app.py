# ==========================================================
# Proyecto Sprint 7 - Aplicación Web con Streamlit
# ==========================================================
# Autor: Alexis Esteban Reyes Hinojosa
# Descripción:
# Aplicación web interactiva para explorar el dataset de
# anuncios de vehículos. Permite visualizar un histograma
# y un gráfico de dispersión utilizando Plotly Express.
# ==========================================================

import pandas as pd
import plotly.express as px
import streamlit as st

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(
    page_title="Auto Vision",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Cargar datos
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

car_data = load_data()

# -----------------------------
# Encabezado principal
# -----------------------------
st.header("🚗 Auto Vision")
st.markdown(
    """
    Esta aplicación te permite **explorar anuncios de vehículos usados**.
    Puedes construir un **histograma** o un **gráfico de dispersión**
    interactivo con los datos del archivo `vehicles_us.csv`.
    """
)

# -----------------------------
# Controles en la barra lateral
# -----------------------------
st.sidebar.title("Opciones de control")

show_hist = st.sidebar.checkbox("Mostrar histograma", value=True)
show_scatter = st.sidebar.checkbox("Mostrar gráfico de dispersión", value=True)

# Selección de columnas (solo numéricas)
numeric_cols = car_data.select_dtypes(include="number").columns.tolist()

# Evitar errores si faltan columnas
if not numeric_cols:
    st.error("No se encontraron columnas numéricas en el dataset.")
else:
    st.sidebar.markdown("---")
    st.sidebar.subheader("Opciones para el histograma")
    x_hist = st.sidebar.selectbox("Columna (eje X):", options=numeric_cols, index=0)

    st.sidebar.subheader("Opciones para el gráfico de dispersión")
    x_scatter = st.sidebar.selectbox("Eje X:", options=numeric_cols, index=0)
    y_scatter = st.sidebar.selectbox(
        "Eje Y:",
        options=[c for c in numeric_cols if c != x_scatter],
        index=0
    )

# -----------------------------
# Botones de acción
# -----------------------------
col1, col2 = st.columns(2)
build_hist_btn = col1.button("Generar histograma")
build_scatter_btn = col2.button("Generar gráfico de dispersión")

# -----------------------------
# Visualizaciones
# -----------------------------
if show_hist or build_hist_btn:
    st.subheader("📊 Histograma")
    st.write(f"Distribución de valores en la columna **{x_hist}**.")
    fig_hist = px.histogram(car_data, x=x_hist, nbins=40, title=f"Histograma de {x_hist}")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter or build_scatter_btn:
    st.subheader("📈 Gráfico de dispersión")
    st.write(f"Relación entre **{x_scatter}** y **{y_scatter}**.")
    fig_scatter = px.scatter(
        car_data,
        x=x_scatter,
        y=y_scatter,
        opacity=0.7,
        title=f"{x_scatter} vs {y_scatter}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# Pie de página
# -----------------------------
st.markdown("---")
st.caption("Proyecto desarrollado para el Sprint 7 | Por Alexis Esteban Reyes Hinojosa, Estuve visualizando "
"la pagina por bastante tiempo para poder construir esta cosa")
