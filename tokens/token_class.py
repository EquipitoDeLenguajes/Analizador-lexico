class Token:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
    def __str__(self):
        return f"<{self.nombre}, {self.fila}, {self.columna}>"