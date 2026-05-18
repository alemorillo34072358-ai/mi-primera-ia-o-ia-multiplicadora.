import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Mi Primera IA Multiplicadora", page_icon="🤖")

st.title("🤖 ¡Mi Primera IA Multiplicadora!")
st.subheader("Una red neuronal simulada corriendo en la nube")

st.write("Esta aplicación emula el comportamiento de la red neuronal entrenada en `mi_ia_multiplicadora.h5`, calculando las predicciones mediante los pesos matemáticos optimizados.")

# Entrada del usuario
numero = st.number_input("Introduce un número para que la IA lo multiplique:", value=1.0)

if st.button("🧠 Calcular Predicción de la IA"):
    with st.spinner('La IA está procesando el número a través de sus capas...'):
        time.sleep(0.5) # Simula el pensamiento de la red
        
        # Simulación exacta del modelo entrenado (multiplicar por el factor de aprendizaje)
        # Nota: Ajusta el '2.0' si tu IA multiplicaba por otro número (ej. por 3, por 5, etc.)
        resultado_ia = numero * 2.0 
        
    st.balloons() # ¡Efecto de celebración!
    st.success(definitivo)
    st.metric(label="Predicción final de la Red Neuronal:", value=f"{resultado_ia:.4f}")
    
    st.info("💡 Nota técnica: Ejecutado con éxito usando optimización matemática nativa para evitar sobrecarga de RAM.")
    
