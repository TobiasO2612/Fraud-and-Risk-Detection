# Detección de Transferencias Fraudulentas + Aplicación Web con Streamlit

## Descripción

Este proyecto tiene como objetivo detectar transferencias bancarias potencialmente fraudulentas mediante técnicas
de análisis de datos y machine learning. 
Además, se desarrolló una aplicación interactiva con **Streamlit** para facilitar el uso del modelo predictivo por parte de usuarios o 
analistas.

## Objetivos

- Analizar y limpiar un conjunto de datos de transferencias financieras.
- Eliminar columnas irrelevantes o redundantes para mejorar el rendimiento del modelo.
- Detectar posibles fraudes financieros mediante un modelo predictivo.
- Desarrollar una aplicación web simple e intuitiva para cargar datos y obtener predicciones en tiempo real.

## Tecnologías y Librerías Utilizadas

- **Python**
  - `pandas` y `numpy` para la manipulación y limpieza de datos.
  - `seaborn` para visualización exploratoria.
  - `scikit-learn` para el entrenamiento y evaluación del modelo.
- **Streamlit**
  - Para la creación de una aplicación web interactiva que permite cargar nuevas transferencias y obtener predicciones de fraude en tiempo real.

## Proceso del Proyecto

1. **Carga y Limpieza de Datos**
   - Eliminación de valores nulos.
   - Remoción de columnas que no aportan valor a la predicción (por ejemplo: nameOrig,nameDest).

2. **Análisis Exploratorio**
   - Visualización de la distribución de clases (fraude vs. no fraude).
   - Análisis de correlaciones y patrones en los datos.
   - Analisis que metodo tiende a fraude(transferencia,debito,deposito)

3. **Modelado**
   - Entrenamiento de un modelo de clasificación
   - Evaluación con métricas como precisión, recall, F1-score y matriz de confusión.

4. **Aplicación Web con Streamlit**
   - Interfaz para cargar datos de transferencias.
   - Visualización de estadísticas básicas.
   - Predicción en tiempo real de transacciones sospechosas.

