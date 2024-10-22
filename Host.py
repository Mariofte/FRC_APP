import streamlit as st
from Baked.Class_Hoja import Hoja
from Styles.fun_css import css

def main ():
    hoja = Hoja(
    bot='Baked\Servicio.json',
    scope=['https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ],
    id='1UK2mlF74IUYR_ZGuQiuYFo7zt2hCdloaAjjbU7dcv0s',
    hoja=0
    )
    css(file_name = 'Styles\styles.css')

    opciones = st.sidebar.selectbox(label = "Eliga una pagina", options = ["visualizar","resumen"], key='Eliga una pagina --usuario')

    if opciones == 'visualizar':
        st.dataframe(data = hoja.leer(), key='datafraem -- usuario')
    
    elif opciones == "Promedios":
        pass
        
if __name__ == '__main__':
    main()
    
#A2:AF2
#A3:U3
