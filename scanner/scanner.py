from tokens.tokens import character_special,word_reserved,methods,data_types
from tokens.token_class import Token
from tokens.error import Error
from tokens.identifier_class import Identifier
def read_file(file_name):
    lines = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line)
    return lines
def scannerFunction(cadena):
    textoEscaneado = []
    subcadena_actual = ""
    indice_inicial = 1  # Inicializar en 1 en lugar de 0
    ignorar = False  # Bandera para indicar si se debe ignorar caracteres
    i = 0
    while i < len(cadena):
        if cadena[i] == '\n':
            i += 1
            ignorar = False  # Restablecer la bandera cuando se encuentra un salto de línea
            continue  # Salta al siguiente carácter sin procesar los siguientes pasos
        elif cadena[i] == '#':
            ignorar = True  # Establecer la bandera para ignorar caracteres
            i += 1
            continue
        elif ignorar:
            i += 1
            continue
        found_special = False
        if cadena[i] == '"':
            end_quote_index = cadena.find('"', i + 1)
            if end_quote_index != -1:  # Verificar si se encontró la comilla de cierre
                textoEscaneado.append([cadena[i:end_quote_index + 1], i + 1])
                i = end_quote_index + 1
                found_special = True
        if not found_special:
            if cadena[i].isdigit():
                k = i
                subcadena_siguiente = ""
                while k < len(cadena) and not 'j' in subcadena_siguiente:
                    k += 1
                    if (k < len(cadena)):
                        subcadena_siguiente += cadena[k]
                if (('+' or '-' in subcadena_siguiente) and 'j' in subcadena_siguiente):
                    subcadena_actual += cadena[i] + subcadena_siguiente
                    textoEscaneado.append([subcadena_actual, indice_inicial])
                    i += len(subcadena_actual)
                    subcadena_actual = ""
                    found_special = True
            for j in range(3, 0, -1):
                if i + j <= len(cadena) and cadena[i:i + j] in character_special:
                    if cadena[i:i + j] == '.':
                        if subcadena_actual.isdigit():
                            if cadena[i+1:i + j+1].isdigit():
                                subcadena_actual += cadena[i]
                                found_special = True
                                break
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                    textoEscaneado.append([cadena[i:i + j], i+1])
                    i += j - 1
                    found_special = True
                    break
            if not found_special:
                if cadena[i] == " ":
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                elif cadena[i:i + 3] in character_special:
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                    textoEscaneado.append((cadena[i:i + 3], i+1))
                    i += 2
                else:
                    if not subcadena_actual:
                        indice_inicial = i+1
                    subcadena_actual += cadena[i]
        i += 1
    # Agregar la última subcadena si existe
    if subcadena_actual:
        textoEscaneado.append([subcadena_actual, indice_inicial])
    return textoEscaneado
def generadorTokensSinProcesar(texto):
    tokensFinales=[]
    for i in range(len(texto)):
        tokensInperfectos=scannerFunction(texto[i])
        tokensFinales.append(tokensInperfectos)
    return tokensFinales
def clasificadorDeTokens(tokensFinales):
    tokenClasificado=[]
    for i in range(len(tokensFinales)):
        for j in range(len(tokensFinales[i])):

            if tokensFinales[i][j][0]in character_special:
                    objeto=Token(character_special[tokensFinales[i][j][0]],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0] in word_reserved:
                    objeto=Token(word_reserved[tokensFinales[i][j][0]],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0] in data_types:
                    objeto=Token(data_types[tokensFinales[i][j][0]],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0][-1] == 'j' and (sum(1 for char in tokensFinales[i][j][0] if char in ('+','-')) == 1) and (sum(1 for char in tokensFinales[i][j][0] if char == '.') == 0 or sum(1 for char in tokensFinales[i][j][0] if char == '.') == 1 or sum(1 for char in tokensFinales[i][j][0] if char == '.') == 2) and all(char.isdigit() or char in ('.', '+', '-', 'j', ' ') for char in tokensFinales[i][j][0]):
                objeto = Token('tk_complejo', i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif all(caracter.isdigit() for caracter in tokensFinales[i][j][0]):
                    objeto = Token('tk_entero', i + 1, tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif sum(1 for char in tokensFinales[i][j][0] if char == '.') == 1 and all(char.isdigit() or char == '.' for char in tokensFinales[i][j][0]):
                objeto = Token('tk_float', i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0][0]=='"'and tokensFinales[i][j][0][-1]=='"':
                    objeto = Token('tk_cadena,'+tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0].startswith("__") and tokensFinales[i][j][0].endswith("__"):
                    objeto=Token(tokensFinales[i][j][0],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif j!=0 and tokensFinales[i][j][0] in methods and tokensFinales[i][j-1][0]=='.':
                    objeto=Token(methods[tokensFinales[i][j][0]],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            elif any(caracter.isalpha() or (caracter.isdigit() and not caracter.isalnum())  for caracter in tokensFinales[i][j][0]):
                    objeto=Identifier(tokensFinales[i][j][0],i+1,tokensFinales[i][j][1])
                    tokenClasificado.append(objeto)
            else:
                objeto=Error(i+1,tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
                return tokenClasificado
    return tokenClasificado