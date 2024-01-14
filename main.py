import pandas as pd
import yahooquery as yq
from clasificacion import clasificar_solvencia, clasificar_liquidez, clasificar_eficiencia, clasificacion_color
from clase_color import ColorResultado
from clase_analisisfinanciero import AnalisisFinanciero


# Uso de la clase
ticker = input("Escriba el ticker de la acción a analizar: ").upper()
analisis = AnalisisFinanciero(ticker)

analisis.resultados()