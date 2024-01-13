class ColorResultado:
    def __init__(self,clasificacion,color) -> None:
        self.clasificacion = clasificacion
        self.color = color
    
    def __str__(self) -> str:
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.clasificacion)
