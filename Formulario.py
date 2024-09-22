import streamlit as st 
from Sheet.Class_Hoja import Hoja

hoja = Hoja(
    url=None,
    bot='Sheet\Servicio.json',
    scope=['https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ],
    id='1hApyaC_iw9ms59G1zocLZkfYOP-lX6jX5TI5U4TMSLs'
)

sco = st.text_input("Iniciales", key="sco")
Tipo = st.selectbox("Tipo de match",["Practica","Quals","Semifinales","Finales"], key="Tipo")
match = st.text_input("match",key="match")
ala = st.selectbox("Alianza",["Rojo-1","Rojo-2","Rojo-3","Azul-1","Azul-2","Azul-3"],key="ala")
Equipo = st.text_input("Equipo",key="Equipo")

datos = [[sco,Tipo,match,ala,Equipo]]

boton = st.button("Ingresar")

if boton:
    Hoja.escribir(hoja,datos)