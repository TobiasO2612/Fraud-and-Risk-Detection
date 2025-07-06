import streamlit as st
import joblib
import pandas as pd
import base64

# Función para convertir imagen a base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Cargar imagen de fondo y preparar CSS
image_path = 'tuberias2.jpeg'  # Pon aquí el nombre de tu imagen local
img_base64 = get_base64(image_path)

page_bg_img = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    /* Para que el texto sea legible, puedes añadir un fondo semitransparente a todo el contenido */
    color: white;
}}
.stApp > .main {{
    background-color: rgba(0, 0, 0, 0.4);  /* negro semitransparente */
    padding: 1rem 2rem;
    border-radius: 10px;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Cargar modelos entrenados
clf = joblib.load('modelo_clasificacion.pkl')
regressor = joblib.load('modelo_regresion.pkl')

# Ejemplo de entrada
st.title("Predicción de Mantenimiento de Tuberías")

st.markdown("Por favor introduzca la siguiente informacion")

# Entradas del usuario
Thickness_mm=st.number_input("Espesor inicial de la tuberia",min_value=0.0,value=00.0)
Max_Pressure_psi=st.number_input("Presión máxima experimentada (psi)",min_value=0.0,value=00.0)
Corrosion_Impact_Percent=st.number_input("Porcentaje estimado de impacto por corrosión",min_value=0.0,value=00.0)
Thickness_Loss_mm =st.number_input(" Pérdida de espesor causada por corrosión o desgaste",min_value=0.0,value=00.0)
Time_Years=st.number_input("Cantidad de años en servicio",min_value=0,value=0)

# Crear DataFrame de entrada
if st.button("Detectar Condicion"):
    input_data=pd.DataFrame([{
        "Thickness_mm":Thickness_mm,
        "Max_Pressure_psi":Max_Pressure_psi,
        "Corrosion_Impact_Percent":Corrosion_Impact_Percent,
        "Thickness_Loss_mm":Thickness_Loss_mm,
        "Time_Years":Time_Years
    }])
    # Crear variables derivadas
    input_data["Presión_específica"] = input_data["Max_Pressure_psi"] / input_data["Thickness_mm"].replace(0, 1)
    input_data["Tasa_Corrosión"] = input_data["Thickness_Loss_mm"] / input_data["Time_Years"].replace(0, 1)

    
    # Reemplazar infinitos o NaN si aparecen
    input_data = input_data.replace([float('inf'), float('-inf')], 0).fillna(0)
  


    # Predicción clasificación
    mantenimiento = clf.predict(input_data)[0]
    st.subheader(f"Condicion:'{int(mantenimiento)}'")

    if mantenimiento==1:
        st.error("ATENCION.. Esta tuberia necesita mantenimiento urgente(condicion Critica)")
    else:
        tiempo_restante = regressor.predict(input_data)[0]
        st.write(f"Tiempo restante estimado hasta estado crítico: {tiempo_restante:.2f} años")

                #python -m streamlit run app_deteccion_tuberias.py


