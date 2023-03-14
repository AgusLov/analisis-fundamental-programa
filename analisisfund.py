import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

valido = None

while valido is None:
    ticker = input("Escriba el ticker de la accion a analizar: ").upper()
    tickeryf = yf.Ticker(ticker)
    try:
        valido = tickeryf.basic_info
    except ValueError:
        print("El ticker no es valido o tiene problemas de conexion (en ese caso intente mas tarde)")
        valido = None
        continue
    else:
        break
    
    
hoy = datetime.today()


#obtenemos los datos financieros
financials = tickeryf.financials
balance_sheet = tickeryf.balance_sheet

#obtenemos el último trimestre
current_quarter = financials.columns[-1]

#calculando current ratio (liquidez)
current_assets = balance_sheet.loc["Total Current Assets", current_quarter]
current_liabilities = balance_sheet.loc["Total Current Liabilities", current_quarter]

current_ratio = current_assets / current_liabilities

#calculando solvencia
total_assets = balance_sheet.loc["Total non-current assets", current_quarter]
total_liabilities = balance_sheet.loc["Total non-current assets", current_quarter]

solvencia = total_assets/total_liabilities

#calculando asset turnover (eficiencia)
sales = financials.loc["Total Revenue", current_quarter]
total_assets = balance_sheet.loc["Total Assets", current_quarter]

asset_turnover = sales / total_assets

#calculando return on equity (rentabilidad)
total_equity = balance_sheet.loc["Total Stockholders' Equity", current_quarter]
roe = financials.loc["Net Income", current_quarter] / total_equity

#calculando price/earning (valuacion)

latest_net_income = financials.loc["Net Income Applicable To Common Shares", current_quarter]

if latest_net_income > 0:
    pe_ratio = tickeryf.info["regularMarketPrice"] / latest_net_income
else:
    pe_ratio = None



















