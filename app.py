import streamlit as st
import random
import string
from datetime import datetime

# Configuración de la app
st.set_page_config(page_title="Generador de Contraseñas", layout="centered")

# Título y encabezado
st.title("Universidad Nacional Abierta y a Distancia")
st.subheader("Curso: Programación")
st.write("Fecha actual:", datetime.now().strftime("%d/%m/%Y"))

# Reproduce saludo con voz (voz de navegador)
st.markdown("""
    <script>
        const msg = new SpeechSynthesisUtterance("Bienvenido a la aplicación de generación de contraseñas");
        window.speechSynthesis.speak(msg);
    </script>
""", unsafe_allow_html=True)

# Entrada del usuario
nombre = st.text_input("Ingresa tu nombre:")

# Longitud de la contraseña
longitud = st.number_input("Longitud de la contraseña (mínimo 8)", min_value=8, step=1)

# Caracteres permitidos
numeros = string.digits
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
especiales = "¿¡?=)(/¨*+- %&$#!"

todos = numeros + mayusculas + minusculas + especiales

def generar_contraseña(longitud):
    while True:
        password = []
        password.append(random.choice(numeros))
        password.append(random.choice(mayusculas))
        password.append(random.choice(minusculas))
        password.append(random.choice(especiales))

        restantes = longitud - 4
        todos_sin_repetir = list(set(todos) - set(password))

        if restantes > len(todos_sin_repetir):
            return None  # No se puede generar sin repetir

        password += random.sample(todos_sin_repetir, restantes)
        random.shuffle(password)
        return ''.join(password)

if st.button("Generar Contraseña"):
    if nombre.strip() == "":
        st.warning("Por favor, ingresa tu nombre.")
    else:
        contraseña = generar_contraseña(longitud)
        if contraseña:
            st.success(f"Hola {nombre}, tu contraseña generada es:\n`{contraseña}`")
            st.balloons()
        else:
            st.error("No se pudo generar la contraseña con caracteres únicos.")
