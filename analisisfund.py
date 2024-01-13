import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import yahooquery as yq
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

def liquidez(currentratio):
    if currentratio > 0 and currentratio < 0.5:
        liquido = "Descartada"
    elif currentratio >= 0.5 and currentratio < 1:
        liquido = "Arriesgada"
    elif currentratio >= 1 and currentratio < 1.5:
        liquido = "Ok"
    elif currentratio >= 1.5 and currentratio < 2:
        liquido = "Muy bien"
    elif currentratio >= 2:
        liquido = "Excelente"
    else:
        liquido = "Valor no válido"
    return liquido

def solvencia(solv):
    if solv > 0 and solv < 0.5:
        solvente = "Descartada"
    elif solv >= 0.5 and solv < 1:
        solvente = "Arriesgada"
    elif solv >= 1 and solv < 1.5:
        solvente = "Ok"
    elif solv >= 1.5 and solv < 2:
        solvente = "Muy bien"
    elif solv >= 2:
        solvente = "Excelente"
    else:
        solvente = "Valor no válido"
    return solvente


def eficiencia(turnover):
    if turnover < 1:
        eficiente = "Ineficiente"
    elif turnover >= 1 and turnover < 2:
        eficiente = "Ok"
    elif turnover >= 2 and turnover < 3:
        eficiente = "Decente"
    elif turnover >= 3:
        eficiente = "Excelente"
    else:
        eficiente = "Valor no válido"
    return eficiente
  


valido = None

while valido is None:

    #ticker = input("Escriba el ticker de la accion a analizar: ").upper()
    ticker = input()
    tickeryq = yq.Ticker(ticker)
    tickeryf = yf.Ticker(ticker)
    try:
        valido= tickeryq.asset_profile
    except ValueError:
        print("El ticker no es valido o tiene problemas de conexion (en ese caso intente mas tarde)")
        valido = None
        continue
    else:
        break


hoy = datetime.today()


#obtenemos los datos financieros
balance_sheet = tickeryq.balance_sheet(frequency='q')
financials = tickeryq.all_financial_data(frequency="q")
income_statement = tickeryq.income_statement(frequency="q")


#obtenemos el último trimestre
current_quarter = -1



#calculando current ratio (liquidez) 
current_assets = balance_sheet["CurrentAssets"][current_quarter]

current_liabilities = balance_sheet['CurrentLiabilities'][current_quarter]

current_ratio = current_assets / current_liabilities


print(f"La liquedez esta: {liquidez(current_ratio)}")


#calculando solvencia
total_assets = balance_sheet['TotalAssets'][current_quarter]

total_liabilities = balance_sheet['TotalLiabilitiesNetMinorityInterest'][current_quarter]

solv = total_assets/total_liabilities

print(f"Su solvencia esta: {solvencia(solv)}")


#calculando asset turnover (eficiencia)
sales = financials["TotalRevenue"][current_quarter]
total_assets = balance_sheet["TotalAssets"][current_quarter]

asset_turnover = sales / total_assets


print(f"Su eficiencia es: {eficiencia(asset_turnover)}")


#calculando return on equity (rentabilidad)
total_equity = balance_sheet["StockholdersEquity"]
roe = income_statement["NetIncome"][current_quarter] / total_equity


#calculando price/earning (valuacion)
latest_net_income = income_statement["NetIncomeCommonStockholders"][current_quarter]


if 'regularMarketPrice' in tickeryq.price and latest_net_income > 0:
    pe_ratio = float(tickeryq.price['regularMarketPrice']) / float(latest_net_income)
else:
    pe_ratio = None

















