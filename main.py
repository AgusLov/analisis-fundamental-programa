import pandas as pd
import yahooquery as yq
from clasificacion import clasificar_solvencia, clasificar_liquidez, clasificar_eficiencia, clasificacion_color
from clase_color import ColorResultado

class AnalisisFinanciero:
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.__tickeryq = yq.Ticker(ticker)
        self.__balance_sheet = self.__tickeryq.balance_sheet(frequency='q')
        self.__financials = self.__tickeryq.all_financial_data(frequency="q")
        self.__current_quarter = -1

    def __validar_ticker(self):
            try:
                self.__tickeryq.asset_profile
                self.__balance_sheet["CurrentAssets"][self.__current_quarter]
                self.__balance_sheet['CurrentLiabilities'][self.__current_quarter]
                return True
            except:
                return False        
            
            
    def calcular_liquidez(self):
        current_assets = self.__balance_sheet["CurrentAssets"][self.__current_quarter]
        current_liabilities = self.__balance_sheet['CurrentLiabilities'][self.__current_quarter]
        current_ratio = current_assets / current_liabilities
        return current_ratio
    
    def calcular_solvencia(self):
        total_assets = self.__balance_sheet['TotalAssets'][self.__current_quarter]
        total_liabilities = self.__balance_sheet['TotalLiabilitiesNetMinorityInterest'][self.__current_quarter]
        solvencia = total_assets / total_liabilities
        return solvencia
    
    def calcular_eficiencia(self):
        sales = self.__financials["TotalRevenue"][self.__current_quarter]
        total_assets = self.__balance_sheet["TotalAssets"][self.__current_quarter]
        asset_turnover = sales / total_assets
        return asset_turnover
    
        
    
    def resultados(self):
        if self.__validar_ticker():
            print(f"Ticker: {self.ticker}")
            print(f"Liquidez: {ColorResultado(*clasificar_liquidez(self.calcular_liquidez()))}")
            print(f"Solvencia: {ColorResultado(*clasificar_solvencia(self.calcular_solvencia()))}")
            print(f"Eficiencia: {ColorResultado(*clasificar_eficiencia(self.calcular_eficiencia()))}")
        else:
            print("Análisis no realizado debido a problemas con el ticker.")
        
        


# Uso de la clase
ticker = input("Escriba el ticker de la acción a analizar: ").upper()
analisis = AnalisisFinanciero(ticker)

analisis.resultados()