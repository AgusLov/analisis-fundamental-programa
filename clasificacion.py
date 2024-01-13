
def clasificar_liquidez(currentratio):
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
        
    return (liquido, clasificacion_color(liquido))
    

def clasificar_solvencia(solv):
    if solv > 0 and solv < 0.5:
        solvencia = "Descartada"
    elif solv >= 0.5 and solv < 1:
        solvencia = "Arriesgada"
    elif solv >= 1 and solv < 1.5:
        solvencia = "Ok"
    elif solv >= 1.5 and solv < 2:
        solvencia = "Muy bien"
    elif solv >= 2:
        solvencia = "Excelente"
    else:
        solvencia = "Valor no válido"
        
    return (solvencia, clasificacion_color(solvencia))



def clasificar_eficiencia(turnover):
    if turnover < 1:
        eficiencia = "Ineficiente"
    elif turnover >= 1 and turnover < 2:
        eficiencia = "Ok"
    elif turnover >= 2 and turnover < 3:
        eficiencia = "Decente"
    elif turnover >= 3:
        eficiencia = "Excelente"
    else:
        eficiencia = "Valor no válido"
    
    return (eficiencia, clasificacion_color(eficiencia))


def clasificacion_color(clasificacion):
    
    if clasificacion == "Descartada" or "Arriesgada" or "Ineficiente" or "Valor no válido":
        return 31
    elif clasificacion == "Ok":
        return 33
    elif clasificacion == "Decente" or "Excelente" or "Muy bien":
        return 32
