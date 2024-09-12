class Error:
    def __init__(self, fila, columna, mensaje=">>>Error léxico"):
        self.fila = fila
        self.columna = columna
        self.mensaje = mensaje
    def __str__(self):
        return f"{self.mensaje} (línea: {self.fila}, posición: {self.columna})"