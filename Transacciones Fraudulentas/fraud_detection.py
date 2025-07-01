import streamlit as st
import  pandas as pd
import joblib

model= joblib.load("fraud_detection_pipeline.pkl")
st.title("Aplicacion Prediccion-Deteccion de Fraude")

st.markdown("Por favor ingrese los detalles de la transaccion y presione el boton PREDICCION")

st.divider()

transaction_type=st.selectbox("Tipo de Transaccion",["TRANSFER","PAYMENT","CASH_OUT","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0 ,value=1000.0)
oldbalanceOrg=st.number_input("Saldo Antes(Emisor)",min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input("Saldo Actual(Emisor)",min_value=0.0,value=9000.0)
oldbalanceDest=st.number_input("Saldo Antes(Receptor)",min_value=0.0,value=0.0)
newbalanceDest=st.number_input("Saldo Actual (Receptor)",min_value=0.0,value=0.0)

if st.button("Predecir"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest

    }])

    prediction=model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction==1:
        st.error("Esta Transaccion puede ser fraude")
    else:
        st.success("Esta Transaccion no parece fraude")

    #python -m streamlit run fraud_detection.py