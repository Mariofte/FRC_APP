import streamlit as st 
from Baked.Class_Hoja import Hoja
from Baked.Blue_alince import API
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
    css(file_name = 'Styles\styles.css')

    st.title("Cerbotics App Scouthing")

    st.header("Reguistro")

    sco = st.text_input(label = "Iniciales de scouter", key='Iniciales de scouter')
    ti = st.selectbox(label = "Tipo de Match", options = ["Practica","Quals","Semifinales","Finales"], key='Tipo de Match')
    ma = st.text_input(label = "Match", key='Match')
    eq = st.text_input(label = "Equipo", key='Equipo')

    st.header("Match")

    st.subheader("Autonomo")

    opciones = st.selectbox(label="Es coge una imagen", options=["Azul","Rojo"],key= 'imagenes -- auto')
    if  opciones == 'Azul':
        st.image(image='Styles\AZUL.png')
    elif opciones == 'Rojo':
        st.image(image='Styles\ROJO.png')
    pa = st.selectbox(label="Cual es su posicion inicial", options=["Arriba azul","Enmedio azul","A bajo azul","Arriba rojo","Enmedio rojo","A bajo rojo",],key='Cual es su posicion inicial --auto')
    sa = st.radio(label = "Sale de la Zona inicial", options = ["si","no",], key='Sale de la Zona inicial --auto')
    amp1 = st.number_input(label = "Notas en Amp", min_value = 0, max_value = 100, key='Notas en Amp --auto')
    spe1 = st.number_input(label = "Notas en Speaker", min_value = 0, max_value = 100, key='Notas en Speaker --auto')
    fa1 = st.number_input(label = "Notas Falladas", min_value = 0, max_value = 100, key='Notas falladas --auto')
    cru = st.radio(label = "Cruzo la Mitad de la Cancha", options = ["si","no"], key='Cruzo la Mitad de la Cancha --auto')

    st.subheader("TeleOp")

    amp2 = st.number_input(label = "Notas en Amp", min_value = 0,max_value = 100, key='Notas en Amp --teleop')
    spe2 = st.number_input(label = "Notas en el Speaker", min_value = 0, max_value = 100, key='Notas en el Speaker --teleop')
    fa2 = st.number_input(label = "Notas Falladas", min_value = 0, max_value = 100, key='Notas Falladas --teleop')
    vamp = st.number_input(label = "Veces Amplificado", min_value = 0, max_value = 100, key='Veces Amplificado --teleop')
    nf = st.number_input(label = "Notas Feeded a otro Robot", min_value = 0, max_value = 100, key='Notas Feeded a otro Robot --teleop')
    nl = st.number_input(label = "Notas que lanza fuera de la cancha",min_value= 0 ,max_value = 100,key='Notas que lanza fuera de la cancha --teleop')
    dar = st.selectbox(label = "De donde agarra",options = ["Source","Suelo","Ambas","No intento"],key='De donde agarra --teleop')
    
    st.subheader("Endgame")

    t = st.text_input(label = "Tiempo de Escalado", key='Teimpo de Escalado --end')
    po = st.selectbox("Posicion Finalizada",options = ["Parked","Onstage","Intento","No intento"], key='Posicion Finalizada --end')
    cas = st.radio(label="Intento escalar pero no pudo", options=["si","no"], key='Intento escalar pero no pudo')
    caw = st.radio(label="Iso harmony", options=["si","no"],key='Iso harmony')
    cs = st.radio(label="Iso Spotlit", options=["si","no"],key='Iso Spotlit --end')
    nt = st.radio(label = "Note en Trap", options = ["si","no"], key='Nota en Trap --end')

    st.header("Preguntas")

    ha = st.selectbox(label = "Habilidad de Driver", options = ["No Effectivo","Promedio","Bastante Efectivo","No observado"], key='Habilidad de Drivar --preguntas')
    hi = st.text_input(label="Tienen n buen hiuman", key='Tienen n buen hiuman --preguntas')
    lu  = st.selectbox(label = "Lugar de Disparo", options = ["Pegado al Subwoofer","Alejado al subwoofer","Ambas","No intento"], key='Lugar de Disparo --preguntas')
    bue = st.selectbox(label="Es bueno contra la defensa",options=["si es bueno","no es bueno","muy bueno","no observado"], key='Es bueno contra la defensa --preguntas')
    ni = st.selectbox(label = "Nivel de Defensa", options = ["Debajo del promedio","Promedio","Bueno","Exelente","No jugo defensa"], key='Nivel de Defensa --preguntas')
    bf = st.radio(label = "Es buen feeder?" , options = ["si beun feeder","no es beun feeder","no jugo de feeder"], key='Es buen feeder --preguntas')
    ve = st.selectbox(label = "Velocidad", options = ["1 (lento)", "2", "3", "4", "5 (rapido)"], key='Velocidad --preguntas')
    mi = st.radio(label = "Murio/Inmobilizado ", options=["si","no"], key='Murio/Inmobilizado --preguntas')
    ca = st.radio(label = "Casi se cae", options = ["si","no"], key='Casi se cae --preguntas')
    no = st.radio(label = "Notas que se le cayeron ", options = ["si","no"], key='Notas que se le cayeron --preguntas')
    tar = st.radio(label = "Tarjetas?", options = ["si","no"], key='Tarjetas? --preguntas')
    fun = st.radio(label = "Funciona bien el swerve", options = ["si","no", "no tiene"], key='Funcionea bien el swerve --preguntas')
    es = st.radio(label = "Lo escogerias de segundo pick?", options = ["si","no"], key='Lo escogerias de segundo pick? --preguntas')
    co = st.radio(label = "Hace un buen compañero de alianza", options = ["si","no"], key='Hace un buen compañero de alianza --preguntas')
    com = st.text_area(label = "Comentarios", key = 'Comentarios --preguntas')

    da = [[sco,ti,ma,eq,pa,sa,amp1,spe1,fa1,cru,amp2,spe2,fa2,vamp,nf,nl,dar,t,po,cas,caw,cs,nt,ha,hi,lu,bue,ni,bf,ve,mi,ca,no,tar,fun,es,co,com]]
    boton = st.button(label = "Ingresar" , key='Ingresar --usuario')

    if boton:
        hoja.escribir(datos=da)
        st.success("Se ingrasaron los datos")
        
if __name__ == '__main__':  
    main()