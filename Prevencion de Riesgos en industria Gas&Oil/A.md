🔧 Predicción del Deterioro de Tuberías
Una evolución en el proyecto de mantenimiento predictivo 🧠📊

En este proyecto, se aborda el mantenimiento predictivo de tuberías de gas y petróleo utilizando técnicas de machine learning.
En una primera etapa, se desarrolló un modelo de clasificación capaz de detectar tuberías que requerían mantenimiento urgente, alcanzando una precisión del 100% en dicha tarea.

🚀 Nuevos objetivos
En la evolución del proyecto, se incorporó una segunda meta:
predecir cuántos años le quedan a una tubería antes de alcanzar una condición crítica ⚠️, permitiendo así una planificación más precisa del mantenimiento.

🔍 Metodología
Se analizó el comportamiento de la corrosión a lo largo del tiempo, observando mediante gráficos que su impacto tiende a desacelerarse con los años.

A partir de este análisis, se implementó una fórmula exponencial para estimar el tiempo restante. Esta fórmula fue codificada en Python con apoyo de herramientas de IA.

Se integraron nuevas variables, como:

Tasa de corrosión

Presión específica de operación

Estas mejoras permitieron refinar el modelo de regresión, aumentando su precisión del 94% al 99%.

🧠 Modelos implementados
Modelo de clasificación: Detecta si una tubería requiere mantenimiento urgente.

Modelo de regresión: Estima el tiempo (en años) restante antes de que una tubería llegue a condición crítica.

🖥 Aplicación interactiva
Se desarrolló una aplicación con Streamlit que permite:

Cargar y visualizar datos

Ejecutar predicciones

Interpretar resultados
Todo ello con una interfaz accesible para usuarios no técnicos.

📈 Resultados
El modelo final de regresión alcanzó una precisión del 99% al estimar el tiempo restante para mantenimiento.

Esta herramienta mejora significativamente la capacidad de anticiparse al deterioro, optimizando los planes de mantenimiento preventivo y reduciendo riesgos y costos en la industria energética.
