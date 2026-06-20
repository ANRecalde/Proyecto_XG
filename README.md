# ⚽ Proyecto XG

Plataforma de análisis futbolístico desarrollada en Python y Streamlit para el registro de tiros, cálculo de Expected Goals (xG) y visualización interactiva de datos.

## 🚀 Características

- Registro manual de tiros.
- Cálculo automático de Expected Goals (xG).
- Almacenamiento de eventos en formato CSV.
- Dashboard interactivo para análisis de rendimiento.
- Filtros por tipo de remate y valor de xG.
- Visualización de tiros sobre una cancha de fútbol.

## 🛠️ Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- NumPy
- Scikit-learn

## 📊 Funcionalidades principales

### Shot Logger
Permite registrar remates indicando:
- Ubicación del tiro
- Tipo de remate
- Resultado de la acción

El sistema calcula automáticamente el valor de xG para cada intento.

### Dashboard
Visualización interactiva de:
- Cantidad de tiros
- xG total
- xG promedio
- Distribución espacial de remates
- Filtros dinámicos para explorar los datos

## 📂 Estructura del proyecto

```text
Proyecto_XG/
│
├── app.py
├── datos/
├── modelos/
├── assets/
├── requirements.txt
└── README.md
