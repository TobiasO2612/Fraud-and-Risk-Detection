
# Detección de Tuberías en Estado Crítico (Gas y Petróleo)

## Descripción

Este proyecto tiene como objetivo desarrollar un sistema de análisis predictivo que detecte tuberías de gas y petróleo en estado crítico, 
utilizando técnicas de ciencia de datos con Python. El análisis permite a las empresas anticipar fallos o condiciones peligrosas,
optimizando el mantenimiento preventivo y reduciendo riesgos ambientales y económicos.

## Objetivos

- Limpiar, transformar y analizar los datos relacionados con tuberías.
- Detectar patrones y variables clave asociadas a fallos críticos.
- Desarrollar un modelo de machine learning que prediga el estado crítico de una tubería.
- Implementar un pipeline completo de procesamiento y predicción para facilitar su reutilización.

## Herramientas y Tecnologías

- **Python**
  - `pandas` para manipulación y análisis de datos.
  - `numpy` para operaciones numéricas eficientes.
  - `matplotlib` y `seaborn` para visualización de datos.
  - `scikit-learn` para el modelado predictivo y la creación de pipelines.

## Proceso del Proyecto

1. **Carga y exploración de datos**
   - Análisis exploratorio (EDA) para entender distribución, valores nulos, correlaciones, etc.

2. **Preprocesamiento**
   - Limpieza de datos, tratamiento de valores faltantes, codificación de variables categóricas.
   - Normalización y escalado de variables numéricas.

3. **Visualización**
   - Gráficos de dispersión, mapas de calor, histogramas y más para identificar tendencias y relaciones.

4. **Modelado predictivo**
   - Entrenamiento de modelos.
   - Evaluación con métricas como accuracy, F1-score y matriz de confusión.

5. **Pipeline**
   - Implementación de un pipeline completo con `scikit-learn` para encapsular todo el flujo: preprocesamiento → entrenamiento → predicción.

## Resultados Esperados

- Detección precisa de tuberías en estado crítico.
- Identificación de factores más relevantes en el deterioro de infraestructura.
- Modelo reproducible para aplicarse en datos nuevos o en producción.


