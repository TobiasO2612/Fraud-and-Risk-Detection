#🔧 Predicción del deterioro de tuberías: una evolución en mi proyecto de mantenimiento predictivo 🧠📊

En mi publicación anterior mostré cómo mi modelo de machine learning era capaz de detectar tuberías de gas y petróleo que necesitaban un cambio urgente, alcanzando una precisión del 100% en esa tarea.
En esta nueva etapa, decidí llevar el proyecto un paso más allá: incorporar la predicción del tiempo estimado que le queda a una tubería en condición normal o moderada antes de alcanzar un estado crítico ⚠️
Para lograrlo:
  Primero analicé el comportamiento de la corrosión a lo largo del tiempo, 
  observando mediante gráficos que su impacto tiende a    desacelerarse con los años.
  A partir de este análisis, utilicé una fórmula exponencial para realizar un calculo en mi cuaderno,
  la cual tuve que pedir ayuda a la IA para recrearla con python porque no tenia idea de como hacerlo jeje.
  También incorporé nuevas variables como la tasa de corrosión y la presión específica,
  lo que permitió mejorar el modelo de regresión pasando de un 94% de precisión a un 99%.
🧠 Este proyecto incluye dos modelos:
    Un modelo de clasificación, que detecta si una tubería necesita mantenimiento urgente.
    Un modelo de regresión, que estima cuántos años le quedan antes de llegar a condición crítica.
🖥 Además, desarrollé una aplicación interactiva con Streamlit, que permite cargar datos, visualizar resultados y obtener predicciones de forma accesible para usuarios no técnicos.
🔍 Tras probar diferentes algoritmos, el modelo final alcanzó una precisión del 99% al estimar cuántos años le quedan a una tubería antes de necesitar mantenimiento urgente.
📌 Este avance permite anticiparse con mayor precisión al deterioro y optimizar los planes de mantenimiento preventivo, reduciendo riesgos y costos en la industria energética.
