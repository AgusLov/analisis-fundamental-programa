import pandas as pd
import yahooquery as yq
from clase_analisis import AnalisisFinanciero
from clase_color import ColorResultado

# Uso de la clase
ticker = input("Escriba el ticker de la acción a analizar: ").upper()
analisis = AnalisisFinanciero(ticker)

analisis.realizar_analisis()