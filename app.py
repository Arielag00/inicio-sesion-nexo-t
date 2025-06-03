import streamlit as st
import json

# Cargar usuarios
def cargar_usuarios():
    with open("usuarios.json", "r") as file:
        return json.load(file)["usuarios"]

# Validar usuario y clave
def validar(usuario, clave, data):
    return usuario in data and data[usuario]["clave"] == clave

# App principal
def main():
    st.set_page_config(page_title="Ingreso Seguro", layout="centered")
    st.title("🔐 Inicio de sesión")

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        data = cargar_usuarios()
        if validar(usuario, clave, data):
            rol = data[usuario]["rol"]
            st.success(f"Bienvenido {usuario} ({rol})")

            # Mostrar botón según el rol con link real que sí redirige
            if rol == "asesor":
                st.markdown(
                    """
                    <a href="https://chatgpt.com/g/g-683632a4bf3481919f1732e145318886-aia-terraloteos-demo" target="_blank">
                        <button style='padding:10px 20px; font-size:16px;'>Ir al asistente para asesores</button>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            elif rol == "jefe":
                st.markdown(
                    """
                    <a href="https://chatgpt.com/g/g-6838c45c00788191a4bfcb6232b64cfe-aia-nexo-t" target="_blank">
                        <button style='padding:10px 20px; font-size:16px;'>Ir al asistente para jefes</button>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.error("Usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
