import streamlit as st
from Baked.Class_Hoja import Hoja
from Baked.Class_Dibujar import Dibujar
from Styles.fun_css import css

def main ():
    hoja = Hoja(
    bot='Baked\Servicio.json',
    scope=['https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ],
    id='1hApyaC_iw9ms59G1zocLZkfYOP-lX6jX5TI5U4TMSLs',
    hoja=0
    )

    dibujar = Dibujar(
    bot='Baked\Servicio.json',
    scope=['https://spreadsheets.google.com/feeds', 
        'https://www.googleapis.com/auth/drive'
        ],
    id='1hApyaC_iw9ms59G1zocLZkfYOP-lX6jX5TI5U4TMSLs',
    hoja=0
    )

    css(file_name = 'Styles\styles.css')

    opciones = st.sidebar.selectbox(label = "Eliga una pagina", options = ["visualizar","Graficas"], key='Eliga una pagina --usuario')

    if opciones == 'visualizar':
    
        st.dataframe(hoja.leer(), key='datafraem -- usuario')

        rango_limpiar = st.text_input("Rango a limpiar", key='Rango a limpiar --usuario')
        boton = st.button("Limpiar", key='Limpiar --usuario')

        if boton:
            hoja.limpiar(rango=rango_limpiar)
    
    elif opciones == 'Graficas':
        st.balloons()
        
if __name__ == '__main__':
    main()
    
#A2:AF2