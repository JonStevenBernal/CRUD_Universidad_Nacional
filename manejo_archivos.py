#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

# registro={} #inicializar el tipo de dato que se va a usar



# registro = {1:["AMANDA GIRALDO MUNEVAR",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
#             2:["JORGE RODRIGUEZ ALANIS",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
#             3:["JAVIER HERNANDEZ MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False],
#             4:["JUAN REYES MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False]
#             }

# Para subir datos, con indentacion y evitar que lo suba en ascii
# with open('alumnos.json', 'w') as file:
#     json.dump(registro, file, inden=4,ensure_ascii=False)

# with open('alumnos.json') as file:
#     datos = json.load(file)

# pprint(registro)

# with open("alumnos.json", "r") as f:
#     registro = json.loads(f)

def subir_data(registro):
    # Para guardar formato en JSON
    with open('alumnos.json', 'w') as file:
        json.dump(registro, file, ensure_ascii=False, indent=4)

    return registro

def leer_data():
    # convertir = json.loads(registro)
    with open("alumnos.json", "r") as file:
        registro = json.load(file)
    return registro


# print(leer_data())

# Convert a Python object containing all the legal data types:
# objetoJson = json.dumps(registro, indent=4)

# print(jso)

# Convertir y subir

# objectoJson = json.dumps(registro)

# with open('alumnos.json', 'w') as file:
#     json.dump(registro, file, ensure_ascii=False, indent=4)

# with io.open('filename', 'w', encoding='utf8') as json_file:


