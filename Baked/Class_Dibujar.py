import streamlit as st 
import gspread as gs 
import pandas as pd
import matplotlib.pyplot as plt 
from oauth2client.service_account import ServiceAccountCredentials as service

class Dibujar :
    def __init__ (self,bot,scope,id,hoja) :
        self.bot = bot
        self.scope = scope
        self.id = id 
        self.hoja = hoja
    
    def Grafica (self):
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            datos = worksheet.get_all_records()
        
            df = pd.DataFrame(datos)
            
        
        except FileNotFoundError as fnf_error:
            st.error(f"Archivo de credenciales no encontrado: {fnf_error}")
        
        except gs.exceptions.APIError as api_error:
            st.error(f"Error de la API de Google Sheets: {api_error}")
        
        except Exception as error:
            st.error(f"Hubo un error: {error}")
        
    def pastel (self): 
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            datos = worksheet.get_all_records()
        
            df = pd.DataFrame(datos)
            
        except FileNotFoundError as fnf_error:
            st.error(f"Archivo de credenciales no encontrado: {fnf_error}")
        
        except gs.exceptions.APIError as api_error:
            st.error(f"Error de la API de Google Sheets: {api_error}")
        
        except Exception as error:
            st.error(f"Hubo un error: {error}")