import streamlit as st
from PIL import Image
import base64
import json

# --- Fondo ---
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            header {{ visibility: hidden; }}
            footer {{ visibility: hidden; }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# --- Cargar usuarios JSON ---
def cargar_usuarios():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)
    return datos["usuarios"]

# --- Mapeo de nombres completos si aplica ---
def nombre_amigable(usuario):
    nombres_directores = {
        "Marcosag": "Marcos Aguero"
    }
    return nombres_directores.get(usuario, usuario)

# --- Determinar link según rol ---
def obtener_link_por_rol(rol):
    if "jefe" in rol.lower() or "director" in rol.lower():
        return "https://chatgpt.com/g/g-6838c45c00788191a4bfcb6232b64cfe-aia-nexo-t-2-0"
    else:
        return "https://chatgpt.com/g/g-683632a4bf3481919f1732e145318886-aia-nexo-t1"

# --- Fondo + estilos CSS ---
set_background("fondo_ingreso.jpg")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Login Interface ---
with st.container():
    st.markdown("<h1>Nexo - T</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>Tu acceso a toda la información de Terraloteos</p>", unsafe_allow_html=True)

    usuario_input = st.text_input("Usuario", placeholder="Usuario", label_visibility="collapsed")
    pass_input = st.text_input("Contraseña", placeholder="Contraseña", type="password", label_visibility="collapsed")

    login_exitoso = False
    nombre_usuario = ""
    link_asistente = ""

    if st.button("INICIAR SESIÓN"):
        usuarios = cargar_usuarios()
        if usuario_input in usuarios and pass_input == usuarios[usuario_input]["clave"]:
            login_exitoso = True
            nombre_usuario = nombre_amigable(usuario_input)
            link_asistente = obtener_link_por_rol(usuarios[usuario_input]["rol"])
        else:
            st.markdown("<p class='mensaje error'>Usuario o contraseña incorrectos</p>", unsafe_allow_html=True)

    if login_exitoso:
        st.markdown(f"""
            <div style='text-align: center; margin-top: 30px;'>
                <a href='{link_asistente}' target='_blank'>
                    <button style='
                        background-color: #28a745;
                        color: white;
                        padding: 12px 24px;
                        font-size: 16px;
                        border: none;
                        border-radius: 8px;
                        font-weight: 600;
                        cursor: pointer;
                        font-family: "Poppins", sans-serif;
                        transition: background-color 0.3s ease;
                    ' onmouseover="this.style.backgroundColor='#218838'"
                    onmouseout="this.style.backgroundColor='#28a745'">
                        Bienvenido, {nombre_usuario}
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

    # --- Enlace a soporte ---
    st.markdown("""
        <div style='text-align: center; margin-top: 25px;'>
            <a href='https://docs.google.com/forms/d/e/1FAIpQLSfAdIQICYC3Ocr6NcgF0yRd18sTSP2NJUBYqptM9hm4YbUstQ/viewform?usp=dialog'
            target='_blank'
            style='font-size: 14px; color: #444; text-decoration: none; font-weight: 500;'>
            ¿No cuentas con usuario? Contactá al equipo de soporte
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""<div class="footer">By: Ariel Agüero :)</div>""", unsafe_allow_html=True)


