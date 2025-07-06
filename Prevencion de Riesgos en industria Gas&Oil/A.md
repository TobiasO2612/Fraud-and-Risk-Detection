# 🔧 Predicción del Deterioro de Tuberías  
**Una evolución en el proyecto de mantenimiento predictivo** 🧠📊

En este proyecto se aborda el mantenimiento predictivo de tuberías de gas y petróleo utilizando técnicas de *machine learning*.  
En una primera etapa, se desarrolló un modelo de clasificación capaz de detectar tuberías que requerían mantenimiento urgente, alcanzando una **precisión del 100%** en dicha tarea.

## 🚀 Nuevos Objetivos

En esta segunda fase, se incorporó un nuevo desafío:  
**Predecir cuántos años le quedan a una tubería en condición normal o moderada antes de alcanzar un estado crítico** ⚠️

## 🔍 Metodología

- Análisis del comportamiento de la corrosión a lo largo del tiempo, observando mediante gráficos que su impacto tiende a desacelerarse con los años.
- Implementación de una **fórmula exponencial** para estimar el tiempo restante. Esta fue codificada en Python con ayuda de herramientas de IA.
- Incorporación de nuevas variables al modelo, como:
  - Tasa de corrosión
  - Presión específica de operación

Estas mejoras permitieron refinar el modelo de regresión, aumentando su precisión del **94% al 99%**.

## 🧠 Modelos Implementados

- **Modelo de Clasificación:** Detecta si una tubería requiere mantenimiento urgente.
- **Modelo de Regresión:** Estima el tiempo (en años) restante antes de que una tubería llegue a condición crítica.

## 🖥 Aplicación Interactiva

Se desarrolló una aplicación con **Streamlit** que permite:

- Cargar y visualizar datos
- Ejecutar predicciones
- Interpretar resultados  

Todo ello a través de una interfaz intuitiva, diseñada para usuarios no técnicos.

## 📈 Resultados

- El modelo final de regresión alcanzó una **precisión del 99%** al estimar el tiempo restante antes del deterioro crítico.
- Esta solución mejora significativamente la capacidad de **anticiparse al deterioro**, optimizando los planes de mantenimiento prevent

