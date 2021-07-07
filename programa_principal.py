#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess as sp
from modulos import *
from manejo_archivos import *
"""
Este programa invoca diferentes módulos que se encagan de manejar la
funcionalidad del aplicativo
"""
# registro_alumnos = {} #inicializa el diccionario
# registro_alumnos = {1:["AMANDA GIRALDO MUNEVAR",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
#                     2:["JORGE RODRIGUEZ ALANIS",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
#                     3:["JAVIER HERNANDEZ MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False]
#                   }
registro = leer_data()

while True:
   # tmp = sp.call('clear',shell=True) # borrarPantalla()
   opcion = menu()
   if opcion == 0: #Opción para salir del programa
      break
   if opcion == 1: #Opción para ingresar datos
      registro_alumnos = subir_data(registro)
      ingresar = ingresar(registro_alumnos)
      subir_data(ingresar)
   elif opcion == 2:  #Opción para modificar datos existentes
      registro_alumnos = subir_data(registro)
      modificar = modificar(registro_alumnos)
      subir_data(modificar)
   elif opcion == 3:  #Opción para consultar la información
      consultar_alumnos = leer_data()
      consultar(consultar_alumnos)
   elif opcion == 4:  #Opción para eliminar registros
      registro_alumnos = subir_data(registro)
      delete = eliminar(registro_alumnos)
      subir_data(delete)
   else:
      print(" .. Opción inválida ..")
      input("<Cualquier tecla para continuar>")

print("\n\n    . . !!!!  Programa terminó Ok  !!!! . .\n")

