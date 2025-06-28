import streamlit as st
import pandas as pd
import joblib

model=joblib.load("deteccion_critica_tuberia_pipeline.pkl")
st.title("Deteccion del Estado de las tuberia Gas y Petroleo")

st.markdown("Por favor introduzca la siguiente informacion")

st.divider()

Thickness_mm=st.number_input("Espesor inicial de la tuberia",min_value=0.0,value=10.0)
Max_Pressure_psi=st.number_input("Presión máxima experimentada (psi)",min_value=0.0,value=1000.0)
Corrosion_Impact_Percent=st.number_input("Porcentaje estimado de impacto por corrosión",min_value=0.0,value=3.0)
Thickness_Loss_mm =st.number_input(" Pérdida de espesor causada por corrosión o desgaste",min_value=0.0,value=15.0)
Time_Years=st.number_input("Cantidad de años en servicio",min_value=0,value=5)


if st.button("Detectar Condicion"):
    input_data=pd.DataFrame([{
        "Thickness_mm":Thickness_mm,
        "Max_Pressure_psi":Max_Pressure_psi,
        "Corrosion_Impact_Percent":Corrosion_Impact_Percent,
        "Thickness_Loss_mm":Thickness_Loss_mm,
        "Time_Years":Time_Years
    }])

    prediccion=model.predict(input_data)[0]

    st.subheader(f"Condicion:'{int(prediccion)}'")

    if prediccion==1:
        st.error("ATENCION.. Esta tuberia necesita mantenimiento(condicion Critica)")
    else:
        st.success("Esta tuberia tiene una condicion normal o moderada")

        #python -m streamlit run deteccion_cambio_tuberia.py
