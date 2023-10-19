"""
Ejemplo de manejo de archivos básico en Python
"""

import os

# Inicializar archivo ------------------
def inicializar_archivo():
    """
    Inicializar archivo
    """

    os.system("clear")
    print("Inicializando archivo ...")

# Abre archivo en modo escritura, borra todo su contenido ------------------
    with open('assignments/00Archivos/src/data/personas.csv', 'w') as f:
        f.write("NOMBRE,APELLIDO PATERNO,APELLIDO MATERNO\n")    

    print("Archivo inicializado correctamente!")
  
    input("Presione una tecla para continuar...")   

# Grabar datos ------------------------
def grabar_datos():
    """
    Grabar datos en un archivo
    """

    personas = []

    while True:
        os.system("clear")

        print("GRABAR DATOS")
        print("============")

        nombre = input("NOMBRE (FIN=0):")

        if nombre == "0":
            break

        ap_pat = input("APELLIDO PATERNO:")
        ap_mat = input("APELLIDO MATERNO:")

        personas.append([nombre, ap_pat, ap_mat])
    
    print("Grabando información ...")

# Abre archivo en modo escritura, agrega contenido ------------------
    with open('assignments/00Archivos/src/data/personas.csv', 'a') as f:
        for persona in personas:
            f.write(persona[0]+"," + persona[1] + "," + persona[2] + "\n")
    print("Información grabada correctamente!")
   
    input("Presione una tecla para continuar...")   

# Leer datos --------------------------
def leer_datos():
    """
    Leer datos de un archivo
    """
    os.system("clear")

    personas = []

# Abre archivo en modo lectura -------------------------------------
    with open('assignments/00Archivos/src/data/personas.csv', 'r') as f:
        for line in f:
            persona = line.split(",")
            personas.append([persona[0], persona[1], persona[2][:-1]])

    print("DATOS DEL ARCHIVO")

    print("-----------------")
    for persona in personas:
        print(persona[0] + " " + persona[1] + " " + persona[2])
    print("-----------------")

    input("Presione una tecla para continuar...")

# Menu principal ----------------------
def menu():
    """
    Menu principal de la aplicación
    """
    
    opcion=0

    while opcion != -1:
        os.system("clear")

        print("** INICIALIZAR EL ARCHIVO PRIMERO Y DESPUES GRABAR Y/O LEER DATOS **")
        print()

        print("MENU PRINCIPAL")
        print("===============")
        print("[0] - Inicializar archivo")
        print("[1] - Grabar datos en archivo")
        print("[2] - Leer datos de archivo")
        print()
        print("[-1] - Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 0:
            inicializar_archivo()
        elif opcion == 1:
            grabar_datos()
        elif opcion == 2:
            leer_datos()
        

def main():
    menu()
  
    os.system("clear")
    print("Fin del programa")

if __name__=='__main__':
    main()