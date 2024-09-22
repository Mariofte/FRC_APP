import streamlit as st 
from Sheet.Class_Hoja import Hoja

hoja = Hoja(
    url='https://docs.google.com/spreadsheets/d/1hApyaC_iw9ms59G1zocLZkfYOP-lX6jX5TI5U4TMSLs/export?formart=csv',
    bot=None,
    scope=None,
    id=None
)

st.dataframe(Hoja.leer(hoja))