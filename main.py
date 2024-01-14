import pandas as pd
import yahooquery as yq
from logic.clasificacion import clasificar_solvencia, clasificar_liquidez, clasificar_eficiencia, clasificacion_color
from logic.clase_color import ColorResultado
from logic.clase_analisisfinanciero import AnalisisFinanciero


# Uso de la clase
ticker = input("Escriba el ticker de la acción a analizar: ").upper()
analisis = AnalisisFinanciero(ticker)

analisis.resultados()