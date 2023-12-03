import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos')

# Botón para construir histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="price", y="odometer", color="condition")
    st.plotly_chart(fig_scatter, use_container_width=True)
