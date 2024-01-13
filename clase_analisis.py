import pandas as pd
import yahooquery as yq
from clasificacion import clasificar_eficiencia, clasificar_liquidez, clasificar_solvencia
from clase_analisis import AnalisisFinanciero

class AnalisisFinanciero:
    def __init__(self, ticker):
        self.ticker = ticker
        self.tickeryq = yq.Ticker(ticker)
        self.balance_sheet = self.tickeryq.balance_sheet(frequency='q')
        self.financials = self.tickeryq.all_financial_data(frequency="q")
        self.income_statement = self.tickeryq.income_statement(frequency="q")
        self.current_quarter = -1

    def calcular_liquidez(self):
        current_assets = self.balance_sheet["CurrentAssets"][self.current_quarter]
        current_liabilities = self.balance_sheet['CurrentLiabilities'][self.current_quarter]
        current_ratio = current_assets / current_liabilities

        return clasificar_liquidez(current_ratio)


    def calcular_solvencia(self):
        total_assets = self.balance_sheet['TotalAssets'][self.current_quarter]
        total_liabilities = self.balance_sheet['TotalLiabilitiesNetMinorityInterest'][self.current_quarter]
        solv = total_assets / total_liabilities

        return clasificar_solvencia(solv)

    def calcular_eficiencia(self):
        sales = self.financials["TotalRevenue"][self.current_quarter]
        total_assets = self.balance_sheet["TotalAssets"][self.current_quarter]
        asset_turnover = sales / total_assets

        return clasificar_eficiencia(asset_turnover)
    
    def validar_ticker():
            try:
                tickeryq.asset_profile
                balance_sheet["CurrentAssets"][self.current_quarter]
                balance_sheet['CurrentLiabilities'][self.current_quarter]
                return True
            except:
                return False
    
    def realizar_analisis(self):
        if self.validar_ticker():
            print(f"Ticker: {self.ticker}")
            print(f"Liquidez: {self.calcular_liquidez()}")
            print(f"Solvencia: {self.calcular_solvencia()}")
            print(f"Eficiencia: {self.calcular_eficiencia()}")
            print(f"Return on Equity: {self.calcular_return_on_equity()}")
            print(f"PE Ratio: {self.calcular_pe_ratio()}")
        else:
            print("Análisis no realizado debido a problemas con el ticker.")
