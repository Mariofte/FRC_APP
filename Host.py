import streamlit as st
from Baked.Class_Hoja import Hoja
from Styles.fun_css import css

def main ():
    hoja = Hoja(
    bot='Baked\Servicio.json',
    scope=['https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ],
    id='1hApyaC_iw9ms59G1zocLZkfYOP-lX6jX5TI5U4TMSLs',
    hoja=1
    )
    #css(file_name = 'Styles\styles.css')

    opciones = st.sidebar.selectbox(label = "Eliga una pagina", options = ["visualizar","resumen"], key='Eliga una pagina --usuario')

    if opciones == "Datos crudos":
        st.dataframe(data = hoja.leer(), key='datafraem -- usuario')
    
    elif opciones == "Resumen":
        pass
        
if __name__ == '__main__':
    main()
    
#A2:AF2
#A3:U3
