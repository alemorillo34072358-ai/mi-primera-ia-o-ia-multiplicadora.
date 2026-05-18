
import streamlit as st
import tensorflow as tf
import numpy as np

st.set_page_config(page_title="Mi Primera IA", page_icon="🤖", layout="centered")
st.title("🤖 Mi App Multiplicadora con IA")
st.write("Esta aplicación utiliza la neurona artificial que entrenaste en Google Colab para predecir el doble de cualquier número.")

try:
    @st.cache_resource
    def cargar_modelo():
        return tf.keras.models.load_model('mi_ia_multiplicadora.h5')
    
    modelo = cargar_modelo()
    st.success("¡Cerebro de la IA cargado con éxito!")

    st.subheader("Haz tu prueba aquí:")
    numero_usuario = st.number_input("Introduce un número cualquiera:", value=10.0, step=1.0)

    if st.button("Calcular con la IA 🚀"):
        prediccion = modelo.predict(np.array([[numero_usuario]]), verbose=0)
        resultado = prediccion[0][0]
        st.metric(label="La IA calcula que el resultado es:", value=f"{resultado:.4f}")
        st.balloon()

except Exception as e:
    st.error("No se pudo encontrar el archivo 'mi_ia_multiplicadora.h5'. Asegúrate de subirlo junto a este script.")
    st.info("Error técnico: " + str(e))
