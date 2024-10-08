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
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            datos = worksheet.get_all_records()
        
            df = pd.DataFrame(datos)
        
            return df
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")
            
    def leer_2 (self):
        url = f'https://docs.google.com/spreadsheets/d/{self.id}/export?fromat=csv'
        df = pd.DataFrame(url)
    
        return df
    
    def escribir (self,datos):
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            worksheet.insert_rows(datos,2)
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")
        
    def limpiar (self,rango):
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            worksheet.batch_clear(rango)
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")