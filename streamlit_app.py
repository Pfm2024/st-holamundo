import streamlit as st

st.title("lacasade")
st.header("mi primera pagina en python")
st.subheader("Introduccion")
st.write("hola mundo")
st.caption("Ey!")

st.divider()

st.markdown("en un **lugar** de la mancha")
st.markdown(":orange[TOMATE]")
st.markdown(":rainbow[fresas]")

multilinea = """
kjsadhlkasjdhfklsahdf 

jñlkjasdlkfj

kdjshdkljhasld

kjshdflksjhdlfk
sdkjfhksjdhfkkk
"""


st.markdown(multilinea)
