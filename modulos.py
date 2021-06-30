#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Módulo de opciones del sistema
"""
import os
# from manejo_archivos import *

def borrarPantalla(): #
   if os.name == "posix":
      os.system("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
      os.system("clear")
      # os.system("cls")

def menu():
   print("*"*80)
   print(" "*17,"Programa para el manejo de Estudiante del Curso")
   print("*"*80)
   print("""
                  1. Crear registros
                  2. Modificar registro
                  3. Consultar registros
                  4. Eliminar registro
                  0. <Terminar>
                  """)
   while True:
      try:     # Controla las fallas al ingresar una opción inválida
         op = int(input("\t\t\tDigite una Opción: "))
         break
      except ValueError:
         print("Error de selección .. Intente de nuevo")
   return op

def ingresar(registro):
   #  registro = grabar_datos(registro)
   borrarPantalla()
   while True:
      try:
         print("-------------------")
         print("Ingreso de Registro")
         print("-------------------")
         while True:
            numero_registro = int(input("Numero de registro: "))
            if numero_registro in registro:
               print("-------------------")
               print(f"Ingrese otro Numero de registro, {numero_registro} ya existe ")
               print("-------------------")
            else:
               break
         print(numero_registro)
         nombre = input("Nombre(s) y Apellido(s): ")
         datos = [nombre.upper()]
         materias = []
         for i in range(3):
            materia = input("Ingrese la materia: ")
            materias.append(materia.upper())
         datos.append(materias)
            # while True:
            #     materia = input("Ingrese las materias, C para continuar: ")
            #     materias.append(materia.upper())
            #     if materia.upper() == "C":
            #        break
            # datos.append(materias)
         while True:
            esta_activo = input("Esta Activo (S/N): ")
            if esta_activo.upper() == "S":
               datos.append(True)
               break
            elif esta_activo.upper() == "N":
               datos.append(False)
               break
            else:
               print("Ingrese una opcion correcta")
         registro[numero_registro] = datos
         print("Registro completado")
         break
      except ValueError:
         print("Error de selección .. Intente de nuevo")
   return registro


def modificar(registro):
   borrarPantalla()
   print("-------------------")
   print("Modificar Registro")
   print("-------------------")
   while True:
      try:
         while True:
            numero_modificar = int(input("Ingrese el numero de registro que desea modificar: "))
            if numero_modificar in registro:
               break
            else:
               print(f"Ingrese otro Numero de registro, {numero_modificar} no existe ")
         print(f"Vas a modificar el siguiente registro con el numero asignado {numero_modificar}")
         print(registro[numero_modificar])
         while True:
            try:
               valor_estudiante = int(input("Ingrese 1 si quiere modificar el nombre, 2 si quiere modificar materias y 3 el estado, 0 <Salir>: "))
               if valor_estudiante == 1:
                  nombre = input("Ingrese el nombre: ")
                  registro[numero_modificar][0] = nombre.upper()
                  print("Modificacion Exitosa!")
               elif valor_estudiante == 2:
                  materias = []
                  for i in range(3):
                     materia = input("Ingrese la materia: ")
                     materias.append(materia.upper())
                  registro[numero_modificar][1] = materias
                  print("Modificacion Exitosa!")
               elif valor_estudiante == 3:
                  while True:
                     estado = input("Ingrese el estado S/N: ")
                     if estado.upper() == "S":
                        registro[numero_modificar][2] = True
                        break
                     elif estado.upper() == "N":
                        registro[numero_modificar][2] = False
                        break
                     else:
                        print("Ingrese una opción correcta S o N")
                  print("Modificacion Exitosa!")
               elif valor_estudiante == 0:
                  break
            except ValueError:
               print("Error de selección .. Intente de nuevo")
         break
      except ValueError:
         print("Error de selección .. Intente de nuevo")
   return registro

def consultar(registro):
   borrarPantalla()
   print("-------------------")
   print("Consultar Registro")
   print("-------------------")
   while True:
      try:
         numero_consulta = int(input("Ingrese el numero que desea consultar 0 para <Salir>: "))
         if numero_consulta in registro:
            print(f"Nombre: {registro[numero_consulta][0]} ")
            print(f"Clases asignadas: {registro[numero_consulta][1]}")
            if registro[numero_consulta][2] == True:
               print("Activo SI")
            else:
               print("Activo No")
         elif numero_consulta == 0:
            break
         else:
            print("El registro no esta en la base de datos")
      except ValueError:
         print("Ingrese un valor correcto")

def eliminar(registro):
   borrarPantalla()
   print("-------------------")
   print("Eliminar Registro")
   print("-------------------")
   while True:
      try:
         while True:
            try:
               borrar_registro = int(input("Ingrese el numero de registro que desea eliminar: "))
               if borrar_registro in registro:
                  break
               else:
                  print(f"El registro {borrar_registro} no esta en la base de datos")
            except ValueError:
               print("Ingrese un valor valido")
         print("Esta a punto de eliminar el siguiente registro")
         print(registro[borrar_registro])
         while True:
            try:
               eleccion = input("Ingrese S si quiere elimarlo, N si no quiere eliminarlo: ")
               if eleccion.upper() == "S":
                  del registro[borrar_registro]
                  print("Eliminacion exitosa")
                  break
               elif eleccion.upper() == "N":
                  break
               else:
                  print("Ingresa un valor correcto S o N")
            except ValueError:
               print("Ingrese un valor valido")
      except ValueError:
         print("Ingrese un valor valido")
      break
   return registro
