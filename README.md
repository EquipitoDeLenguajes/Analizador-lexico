# Analizador_lexico
Este proyecto se trata de un analizador léxico para código de Python.

## Características
- __Soporte para operadores especiales__: El script reconoce operadores como +, -, *, /, entre otros.
- __Reconocimiento de palabras reservadas__: Detecta palabras reservadas de Python como if, else, for, while, entre otras.
- __Clasificación de tokens complejos__: Maneja números complejos, operadores de comparación, operadores de asignación, entre otros.
- __Soporte para comentarios__: Ignora los comentarios comenzados con #.
- __Detección de errores léxicos__: Proporciona mensajes de error cuando se detectan tokens no válidos.

## Cómo usar

### Paso 1: Ejecuta el script `AnalizadorLexico.py`:

```sh
$ python3 AnalizadorLexico.py
```

### Paso 2: Escribir el nombre del archivo que desea cargar:

Ejemplo:

```sh
$ python3 AnalizadorLexico.py
Ingrese el nombre del archivo: ejemplo_prueba_2.txt
```

### Paso 3: Interpretar la salida:

El script realizará el análisis léxico del archivo, clasificará los tokens y guardará el resultado en un archivo llamado `analisis_tokens.txt`.

__Ejemplo__ si el archivo contiene:

```py
for i in range(10):
    print(i)
```

La salida del escáner que se encontrará en `analisis_tokens.txt` será:

```
<for, 1, 1>
<id,i, 1, 5>
<in, 1, 7>
<range, 1, 10>
<tk_par_izq, 1, 15>
<tk_entero, 10, 1, 16>
<tk_par_der, 1, 18>
<tk_dos_puntos, 1, 19>
<print, 2, 5>
<tk_par_izq, 2, 10>
<id,i, 2, 11>
<tk_par_der, 2, 12>
```

### Autores
- Santiago Garzón
- Mateo Fonseca
- Karol Guerrero
- Sebastián Barros
