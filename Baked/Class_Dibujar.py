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
            
        
        except Exception as error:
            st.error(f"Hubo un error:{error}")
        
    def pastel (self): 
        try:
            creds = service.from_json_keyfile_name(self.bot,self.scope)
        
            client = gs.authorize(creds)
        
            sheet = client.open_by_key(self.id)
        
            worksheet = sheet.get_worksheet(self.hoja)
        
            datos = worksheet.get_all_records()
        
            df = pd.DataFrame(datos)
        except Exception as error:
            st.error(f"Hubo un error:{error}")