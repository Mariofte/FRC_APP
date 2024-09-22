import gspread as gs
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials as service

class Hoja:
    def __init__ (self,url,bot,scope,id):
        self.url = url
        self.bot = bot 
        self.scope = scope
        self.id = id
    
    def leer (self):
        try:
            df = pd.read_csv(self.url)
        
            return df
        
        except Exception as error:
            st.error(f"Hubo un errror:{error}")
        
    def escribir (self,datos):
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            clinet = gs.authorize(creds)
        
            sheet = clinet.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(0)
        
            worksheet.insert_rows(datos,2)
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")