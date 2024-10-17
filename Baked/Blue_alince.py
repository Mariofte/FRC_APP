import requests
import streamlit as st 
from oauth2client.service_account import ServiceAccountCredentials as service

"""
    GET: Se utiliza para obtener información de un servidor.
    POST: Se utiliza para enviar datos a un servidor, como al registrarte en un sitio web.
    PUT: Se utiliza para actualizar información en un servidor.
    DELETE: Se utiliza para eliminar información de un servidor.

    Puedes usar peticiones HTTP a través de herramientas como curl o 
    Postman, o incluso directamente desde tu navegador web.
"""

class API:
    def __init__(self,url):
        self.url = url
        
    def equipo (self,key):
        try:
            api = 'https://www.thebluealliance.com/api/v3/team/frc ' + str(key)  + "/awards"
            
            r = requests.get(url=api,)
        except Exception as error:
            st.error(f"Hubo un error")

