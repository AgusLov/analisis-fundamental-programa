from clase_color import ColorResultado

def clasificacion_color(clasificacion):
    
    if clasificacion in ["Descartada", "Arriesgada", "Ineficiente", "Valor no válido"]:
        return "31"
    elif clasificacion == "Ok":
        return "33"
    elif clasificacion in ["Decente", "Excelente", "Muy bien"]:
        return "32"




def clasificar_liquidez(currentratio):
    if 0 < currentratio < 0.5:
        liquido = "Descartada"
    elif 0.5 <= currentratio < 1:
        liquido = "Arriesgada"
    elif 1 <= currentratio < 1.5:
        liquido = "Ok"
    elif 1.5 <= currentratio < 2:
        liquido = "Muy bien"
    elif 2 <= currentratio:
        liquido = "Excelente"
    else:
        liquido = "Valor no válido"
        
    return (liquido, clasificacion_color(liquido))
    

def clasificar_solvencia(solv):
    if 0 < solv < 0.5:
        solvencia = "Descartada"
    elif 0.5 <= solv < 1:
        solvencia = "Arriesgada"
    elif 1 <= solv < 1.5:
        solvencia = "Ok"
    elif 1.5 <= solv < 2:
        solvencia = "Muy bien"
    elif 2 <= solv:
        solvencia = "Excelente"
    else:
        solvencia = "Valor no válido"
        
    return (solvencia, clasificacion_color(solvencia))



def clasificar_eficiencia(turnover):
    if turnover < 1:
        eficiencia = "Ineficiente"
    elif 1 <= turnover < 2:
        eficiencia = "Ok"
    elif 2 <= turnover < 3:
        eficiencia = "Decente"
    elif 3 <= turnover:
        eficiencia = "Excelente"
    else:
        eficiencia = "Valor no válido"
    
    return (eficiencia, clasificacion_color(eficiencia))

