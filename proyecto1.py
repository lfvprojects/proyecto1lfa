import re

# Definir las expresiones regulares para cada categoría léxica
regex_guion = re.compile(r'-')
regex_sexo = re.compile(r'[MF]')
regex_naturaleza = re.compile(r'[ONA]')
regex_provincia = re.compile(r'[0-9]')
regex_digitomen = re.compile(r'[1-9]')
regex_digitomay = re.compile(r'[0-4]')

# Inicializar tabla de símbolos y manejo de errores
tabla_simbolos = []
errores = []

# Función para agregar símbolos a la tabla de símbolos
def agregar_simbolo(lexema, categoria):
    tabla_simbolos.append((lexema, categoria))

# Función para manejar errores léxicos
def manejar_error(lexema, categoria):
    errores.append((lexema, categoria))
    print(f"Error léxico: {lexema} no es válido para la categoría {categoria}")

# Función principal para analizar la cadena de cédula
def analizador_lexico(cadena):
    tokens = re.findall(r'\S+|\s', cadena)

    for token in tokens:
        if regex_guion.match(token):
            agregar_simbolo(token, "<guion>")
        elif regex_sexo.match(token):
            agregar_simbolo(token, "<sexo>")
        elif regex_naturaleza.match(token):
            agregar_simbolo(token, "<naturaleza>")
        elif regex_provincia.match(token):
            agregar_simbolo(token, "Provincia")
        elif regex_digitomen.match(token):
            agregar_simbolo(token, "<dígitomen>")
        elif regex_digitomay.match(token):
            agregar_simbolo(token, "<dígitomay>")
        elif token.isspace():
            continue  # Ignorar espacios en blanco
        else:
            manejar_error(token, "Desconocido")

# Ejemplo de uso
cedula = "M-ONA1-12345"
analizador_lexico(cedula)

# Imprimir resultados
print("\nTabla de Símbolos:")
for lexema, categoria in tabla_simbolos:
    print(f"{lexema}: {categoria}")

print("\nErrores:")
for lexema, categoria in errores:
    print(f"{lexema}: {categoria}")
