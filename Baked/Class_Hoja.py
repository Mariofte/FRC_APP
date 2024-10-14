import gspread as gs
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials as service

class Hoja:
    def __init__ (self,bot,scope,id,hoja):
        self.bot = bot 
        self.scope = scope
        self.id = id
        self.hoja = hoja
    
    def leer (self):
        try:
            creds = service.from_json_keyfile_name(filename = self.bot, scopes = self.scope)
            
            client = gs.authorize(credentials = creds)

            sheet = client.open_by_key(key = self.id)

            worksheet = sheet.get_worksheet( index = self.hoja)

            datos = worksheet.get_all_records()
            
            df = pd.DataFrame(data = datos)
            
            return df
        
        except FileNotFoundError as fnf_error:
            st.error(f"Archivo de credenciales no encontrado: {fnf_error}")
        
        except gs.exceptions.APIError as api_error:
            st.error(f"Error de la API de Google Sheets: {api_error}")
        
        except Exception as error:
            st.error(f"Hubo un error: {error}")
            
    def leer_2 (self):
        try:
            url = f'https://docs.google.com/spreadsheets/d/{self.id}/export?fromat=csv'
            df = pd.DataFrame(data = url)
        
            return df
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")
    
    def escribir (self,datos):
        try:
            creds = service.from_json_keyfile_name(filename = self.bot, scopes = self.scope)
        
            client = gs.authorize(credentials = creds)
        
            sheet = client.open_by_key(key = self.id)
        
            worksheet = sheet.get_worksheet(index = self.hoja)
        
            worksheet.insert_rows(values = datos, row = 2)
        
        except FileNotFoundError as fnf_error:
            st.error(f"Archivo de credenciales no encontrado: {fnf_error}")
        
        except gs.exceptions.APIError as api_error:
            st.error(f"Error de la API de Google Sheets: {api_error}")
        
        except Exception as error:
            st.error(f"Hubo un error: {error}")
        
    def limpiar (self,rango):
        try:
            creds = service.from_json_keyfile_name(filename = self.bot, scopes = self.scope)
        
            client = gs.authorize(credentials = creds)
        
            sheet = client.open_by_key(key = self.id)
        
            worksheet = sheet.get_worksheet(index = self.hoja)
        
            worksheet.batch_clear(ranges = rango)
        
        except FileNotFoundError as fnf_error:
            st.error(f"Archivo de credenciales no encontrado: {fnf_error}")
        
        except gs.exceptions.APIError as api_error:
            st.error(f"Error de la API de Google Sheets: {api_error}")
        
        except Exception as error:
            st.error(f"Hubo un error: {error}")