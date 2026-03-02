# PROYECTO-DE-SPRINT-7
# Análisis de Vehículos Usados


## Descripción

Aplicación web interactiva para el análisis exploratorio de datos de vehículos usados. Construida con Streamlit y Plotly, permite visualizar distribuciones de precios y relaciones entre variables del dataset.

##  Características

-  **Histograma interactivo** – Distribución de precios de vehículos
-  **Gráfico de dispersión** – Relación entre odómetro y precio
-  **Visualizaciones dinámicas** – Generadas con Plotly Express
-  **Panel lateral** – Opciones adicionales (checkbox)
-  **Diseño responsive** – Adaptado a diferentes dispositivos



##  Aplicación en vivo

Puedes probar la aplicación desplegada en Render aquí:

 **[https://proyecto-de-sprint-7.onrender.com](https://proyecto-de-sprint-7.onrender.com)**

##  Estructura del proyecto

PROYECTO-DE-SPRINT-7/<br>
├── app.py<br>
├── vehicles_us.csv<br>
├── requirements.txt<br>
└── notebooks/<br>
 &nbsp;└── EDA.ipynb<br>



 **Dataset**
 El archivo vehicles_us.csv contiene 51,525 registros de vehículos usados con 13 columnas:
 
| Columna       | Descripción                          | Tipo        |
|--------------|--------------------------------------|------------|
| price        | Precio del vehículo (USD)           | numérico   |
| odometer     | Millaje recorrido                   | numérico   |
| model_year   | Año del modelo                      | numérico   |
| condition    | Estado del vehículo                 | categórico |
| type         | Tipo de vehículo                    | categórico |
| paint_color  | Color exterior                      | categórico |
| is_4wd       | Tracción 4x4 (1 = sí)                | booleano   |
| date_posted  | Fecha del anuncio                   | fecha      |
| days_listed  | Días publicado                      | numérico   |

**Autor**
Zhair   
Zeta GitHub