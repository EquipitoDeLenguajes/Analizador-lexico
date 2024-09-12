from scanner.scanner import read_file, scannerFunction, generadorTokensSinProcesar, clasificadorDeTokens
path = "C:/Users/cracm/OneDrive - Universidad Sergio Arboleda/UNIVERSIDAD SERGIO ARBOLEDA - CIENCIAS DE LA COMPUTACION E INTELIGENCIA ARTIFICIAL/QUINTO SEMESTRE/LENGUAJES DE PROGRAMACIÓN Y TRANSDUCCIÓN/PRIMER CORTE/Analizador_Lexico/ejemplo_prueba.txt"
def run(path):
    texto=read_file(path)
    tokens = generadorTokensSinProcesar(texto)
    salida = clasificadorDeTokens(tokens)
    for i in salida:
        print(i)
if __name__ == '__main__':
    run(path)

