character_special = {
    ")": "tk_par_der",
    "(": "tk_par_izq",
    "]": "tk_sqb_der",
    "[": "tk_sqb_izq",
    ":": "tk_dos_puntos",
    ",": "tk_comma",
    ";": "tk_punto_comma",
    "+": "tk_plus",
    "-": "tk_minus",
    "*": "tk_star",
    "/": "tk_slash",
    "|": "tk_vbar",
    "&": "tk_amper",
    "<": "tk_less",
    ">": "tk_greater",
    "=": "tk_assign",
    ".": "tk_punto",
    "%": "tk_percent",
    "}": "tk_brace_der",
    "{": "tk_brace_izq",
    "==": "tk_equal",
    "!=": "tk_no_equal",
    "<=": "tk_less_equal",
    ">=": "tk_greate_equal",
    "^": "tk_circumflex",
    "<<": "tk_shift_izq",
    ">>": "tk_shift_der",
    "**": "tk_double_star",
    "+=": "tk_plus_equal",
    "-=": "tk_mine_equal",
    "*=": "tk_star_equal",
    "/=": "tk_slash_equal",
    "%=": "tk_percent_equal",
    "&=": "tk_amper_equal",
    "|=": "tk_vabar_equal",
    "^=": "tk_circum_flex_equal",
    "<<=": "tk_shift_equal_izq",
    ">>=": "tk_shift_equal_der",
    "**=": "tk_double_start_equal",
    "//": "tk_double_slash",
    "//=": "tk_double_slash_equal",
    "@": "tk_at",
    "@=": "tk_at_equal",
    "->": "tk_ejecuta",
    "...": "tk_ellipsis",
    ":=": "tk_dos_puntos_equal",
}
# reserved words
word_reserved = {
    "open": "open",
    "False": "False",
    "None": "None",
    "True": "True",
    "and": "and",
    "as": "as",
    "assert": "assert",
    "async": "async",
    "await": "await",
    "break": "break",
    "class": "class",
    "continue": "continue",
    "def": "def",
    "del": "del",
    "elif": "elif",
    "else": "else",
    "except": "except",
    "finally": "finally",
    "for": "for",
    "from": "from",
    "global": "global",
    "if": "if",
    "import": "import",
    "in": "in",
    "is": "is",
    "lambda": "lambda",
    "nonlocal": "nonlocal",
    "not": "not",
    "or": "or",
    "pass": "pass",
    "raise": "raise",
    "return": "return",
    "try": "try",
    "while": "while",
    "with": "with",
    "yield": "yield",
    "object": "object",
    "self": "self",
    "print": "print",
    "input": "input",
}
# metodos
methods = {
    "append": "append",
    "extend": "extend",
    "insert": "insert",
    "reverse": "reverse",
    "sort": "sort",
    "fromkeys": "fromkeys",
    "get": "get",
    "items": "items",
    "keys": "keys",
    "popitem": "popitem",
    "setdefault": "setdefault",
    "values": "values",
    "add": "add",
    "clear": "clear",
    "copy": "copy",
    "difference": "difference",
    "difference_update": "difference_update",
    "discard": "discard",
    "intersection": "intersection",
    "intersection_update": "intersection_update",
    "isdisjoint": "isdisjoint",
    "issubset": "issubset",
    "issuperset": "issuperset",
    "pop": "pop",
    "remove": "remove",
    "symmetric_difference": "symmetric_difference",
    "symmetric_difference_update": "symmetric_difference_update",
    "union": "union",
    "update": "update",
    "capitalize": "capitalize",
    "casefold": "casefold",
    "center": "center",
    "count": "count",
    "encode": "encode",
    "endswith": "endswith",
    "expandtabs": "expandtabs",
    "find": "find",
    "format": "format",
    "format_map": "format_map",
    "index": "index",
    "isalnum": "isalnum",
    "isalpha": "isalpha",
    "isascii": "isascii",
    "isdecimal": "isdecimal",
    "isdigit": "isdigit",
    "isidentifier": "isidentifier",
    "islower": "islower",
    "isnumeric": "isnumeric",
    "isprintable": "isprintable",
    "isspace": "isspace",
    "istitle": "istitle",
    "isupper": "isupper",
    "join": "join",
    "ljust": "ljust",
    "lower": "lower",
    "lstrip": "lstrip",
    "maketrans": "maketrans",
    "partition": "partition",
    "replace": "replace",
    "rfind": "rfind",
    "rindex": "rindex",
    "rjust": "rjust",
    "rpartition": "rpartition",
    "rsplit": "rsplit",
    "rstrip": "rstrip",
    "split": "split",
    "splitlines": "splitlines",
    "startswith": "startswith",
    "strip": "strip",
    "swapcase": "swapcase",
    "title": "title",
    "translate": "translate",
    "upper": "upper",
    "zfill": "zfill",
    "bit_length": "bit_length",
    "to_bytes": "to_bytes",
    "from_bytes": "from_bytes",
    "is_integer": "is_integer",
    "hex": "hex",
    "conjugate": "conjugate",
    "real": "real",
    "imag": "imag",
}
# Tipos de datos
data_types = {
    "int": "int",
    "float": "float",
    "complex": "complex",
    "bool": "bool",
    "str": "str",
    "list": "list",
    "tuple": "tuple",
    "set": "set",
    "dict": "dict",
    "NoneT": "None",
    "bytes": "bytes",
    "bytearray": "bytearray",
    "range": "range",
    "frozenset": "frozenset",
}


class Token:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f"<{self.nombre}, {self.fila}, {self.columna}>"


class Identifier:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f"<id,{self.nombre}, {self.fila}, {self.columna}>"


class Error:
    def __init__(self, nombre, fila, columna, mensaje=">>>Error léxico"):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.mensaje} (línea: {self.fila}, posición: {self.columna}, token: {self.nombre})"


def read_file(file_name):
    lines = []
    with open(file_name, "r", encoding="UTF-8") as file:
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
        if cadena[i] == "\n":
            i += 1
            ignorar = (
                False  # Restablecer la bandera cuando se encuentra un salto de línea
            )
            continue  # Salta al siguiente carácter sin procesar los siguientes pasos
        elif cadena[i] == "#":
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
                textoEscaneado.append([cadena[i : end_quote_index + 1], i + 1])
                i = end_quote_index + 1
                found_special = True
        if cadena[i] == "'":
            end_quote_index = cadena.find("'", i + 1)
            if end_quote_index != -1:  # Verificar si se encontró la comilla de cierre
                textoEscaneado.append([cadena[i : end_quote_index + 1], i + 1])
                i = end_quote_index + 1
                found_special = True
        if not found_special:
            if cadena[i].isdigit():
                k = i
                subcadena_siguiente = ""
                while (k < len(cadena) - 1 and " " not in subcadena_siguiente
                       and sum(1 for key in character_special if key in subcadena_siguiente) == 0):
                    k += 1
                    if k < len(cadena) - 1:
                        subcadena_siguiente += cadena[k]
                        if cadena[k] == 'j' and cadena[k + 1] == " ":
                            break
                if "j" in subcadena_siguiente:
                    subcadena_actual += cadena[i] + subcadena_siguiente
                    textoEscaneado.append([subcadena_actual, indice_inicial])
                    i += len(subcadena_actual)
                    subcadena_actual = ""
                    found_special = True
            for j in range(3, 0, -1):
                if i + j <= len(cadena) and cadena[i : i + j] in character_special:
                    if cadena[i : i + j] == ".":
                        if subcadena_actual.isdigit():
                            if cadena[i + 1 : i + j + 1].isdigit():
                                subcadena_actual += cadena[i]
                                found_special = True
                                break
                    if subcadena_actual:
                        textoEscaneado.append(
                            [subcadena_actual, indice_inicial]
                        )  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                    textoEscaneado.append([cadena[i : i + j], i + 1])
                    i += j - 1
                    found_special = True
                    break
            if not found_special:
                if cadena[i] == " ":
                    if subcadena_actual:
                        textoEscaneado.append(
                            [subcadena_actual, indice_inicial]
                        )  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                elif cadena[i : i + 3] in character_special:
                    if subcadena_actual:
                        textoEscaneado.append(
                            [subcadena_actual, indice_inicial]
                        )  # Se cambia subcadenas por textoEscaneado
                        subcadena_actual = ""
                    textoEscaneado.append((cadena[i : i + 3], i + 1))
                    i += 2
                else:
                    if not subcadena_actual:
                        indice_inicial = i + 1
                    subcadena_actual += cadena[i]
        i += 1
    # Agregar la última subcadena si existe
    if subcadena_actual:
        textoEscaneado.append([subcadena_actual, indice_inicial])
    return textoEscaneado


def generadorTokensSinProcesar(texto):
    tokensFinales = []
    for i in range(len(texto)):
        tokensImperfectos = scannerFunction(texto[i])
        tokensFinales.append(tokensImperfectos)
    return tokensFinales


def clasificadorDeTokens(tokensFinales):
    tokenClasificado = []
    for i in range(len(tokensFinales)):
        for j in range(len(tokensFinales[i])):

            if tokensFinales[i][j][0] in character_special:
                objeto = Token(
                    character_special[tokensFinales[i][j][0]],
                    i + 1,
                    tokensFinales[i][j][1],
                )
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0] in word_reserved:
                objeto = Token(
                    word_reserved[tokensFinales[i][j][0]], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0] in data_types:
                objeto = Token(
                    data_types[tokensFinales[i][j][0]], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            elif (
                tokensFinales[i][j][0][-1] == "j"
                and (
                    sum(1 for char in tokensFinales[i][j][0] if char == ".") == 0
                    or sum(1 for char in tokensFinales[i][j][0] if char == ".") == 1
                )
                and all(
                    char.isdigit() or char in (".", "j")
                    for char in tokensFinales[i][j][0]
                )
                and len(tokensFinales[i][j][0]) > 1
            ):
                objeto = Token("tk_complejo", i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif all(caracter.isdigit() for caracter in tokensFinales[i][j][0]):
                objeto = Token("tk_entero", i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif sum(1 for char in tokensFinales[i][j][0] if char == ".") == 1 and all(
                char.isdigit() or char == "." for char in tokensFinales[i][j][0]
            ):
                objeto = Token("tk_float", i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0][0] == '"' and tokensFinales[i][j][0][-1] == '"':
                objeto = Token(
                    "tk_cadena," + tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0][0] == "'" and tokensFinales[i][j][0][-1] == "'":
                objeto = Token(
                    "tk_cadena," + tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            elif tokensFinales[i][j][0].startswith("__") and tokensFinales[i][j][
                0
            ].endswith("__"):
                objeto = Token(tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1])
                tokenClasificado.append(objeto)
            elif (
                j != 0
                and tokensFinales[i][j][0] in methods
                and tokensFinales[i][j - 1][0] == "."
            ):
                objeto = Token(
                    methods[tokensFinales[i][j][0]], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            elif any(
                caracter.isalpha() or (caracter.isdigit() and not caracter.isalnum())
                for caracter in tokensFinales[i][j][0]
            ) and tokensFinales[i][j][0][0].isalpha():
                objeto = Identifier(
                    tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
            else:
                objeto = Error(
                    tokensFinales[i][j][0], i + 1, tokensFinales[i][j][1]
                )
                tokenClasificado.append(objeto)
                return tokenClasificado
    return tokenClasificado


def main():
    path = "ejemplo_prueba_2.txt"  # input("Ingrese el nombre del archivo: ")
    texto = read_file(path)
    tokens = generadorTokensSinProcesar(texto)
    salida = clasificadorDeTokens(tokens)

    output_file = "analisis_tokens.txt"

    with open(output_file, "w", encoding="UTF-8") as file:
        for token in salida:
            file.write(str(token) + "\n")


if __name__ == "__main__":
    main()
