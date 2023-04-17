# Modulos instalados (en este caso funciones de sistema operativo)
import os

# Variables vacias
x = 0
y = 0
selector = int()
selectorReset = int()


# Lista para la creacion de campus
campus = ["Zona-Core", "Campus-Uno", "Campus-Matriz", "Sector-Outsourcing"]


# Bucle While para re-usar la aplicacion
while True:
    selectorReset = int()
    os.system("clear")

    
    # Visualizador de menu
    print("Bienvenido! \n¿Qué desea hacer? ")
    print("1. Visualizar dispositivos. \n2. Visualizar campus. \n3. Agregar dispositivos. \n4. Agregar campus. \n5. Salir.")
    selector = int()
    selector = input("Elija una opcion: ")

    
    # Visualizar los dispositivos
    if int(selector) == 1:
        os.system("clear")
        y = 1
        selector = int()
        print("Por favor elija un Campus \n")
        while len(campus)>=y:
            for item in campus:
                print(str(y)+".", item)
                y=y+1
        selector = input("\nElija una opcion: ")
        x = int()
        x = int(selector)-1
        if int(x) >= 0:
            os.system("clear")
            file=open(campus[int(x)]+".txt", 'r')
            for item in file:
                item=item.strip ()
                print(item)
            file.close()
        selectorReset = input("Presione enter para volver al menu")
    

    # Visualizador de campus
    elif int(selector) == 2:
        os.system("clear")
        y = 1
        selector = int()
        while len(campus)>=y:
            for item in campus:
                print(str(y)+".", item)
                y=y+1
        selectorReset = input("Presione enter para volver al menu")
    

    # Creador de dispositivos (para cada campus)
    elif int(selector) == 3:
        os.system("clear")
        y = 1
        selector = int()
        servicios = []
        print("¿Donde desea colocar su dispositivo nuevo? \n")
        while len(campus)>=y:
            for item in campus:
                print(str(y)+".", item)
                y=y+1
        selector = input("\nElija una opcion: ")
        x = int()
        x = int(selector)-1
        if int(x) >= 0:
            os.system("clear")
            file=open(campus[int(x)]+".txt", 'a')
            print("Elija un dispositivo: \n \n1. Switch. \n2. Switch Multicapa. \n3. Router. \n")
            variable1 = input("Elija su opcion: ")
            os.system("clear")
            print("Introduzca el nombre de su dispositivo")
            variable2 = input("Coloque su nombre aqui: ")
            while True:
                os.system("clear")
                print("¿Desea confirmar este nombre? \n \n1. Si \n2. No \n")
                variable3 = input("Introduzca su respuesta: ")
                if variable3 == "1":
                    break
                else:
                    os.system("clear")
                    print("Introduzca el nombre de su dispositivo")
                    variable2 = input("Coloque su nombre aqui: ")
            print("Elija una jerarquia: \n \n1. Nucleo. \n2. Distribucion. \n3. Acceso. \n")
            variable3 = input("Elija su opcion: ")
            os.system("clear")
            if int(variable1) == 1:
                print("Elija un servicio de red para su switch: \n1. Datos \n2. VLAN \n3. Trunking \n4. Salir \n")
                variable4 = int()
                while variable4 != 4:
                    variable4 = int(input("Introduzca una opcion: "))
                    if variable4 == 1:
                        servicios.append("Datos")
                    elif variable4 == 2:
                        servicios.append("VLAN")
                    elif variable4 == 3:
                        servicios.append("Trunking")
                file.write("Switch: " + variable2)
                if int(variable3) == 1:
                    file.write("\nJerarquia: Nucleo")
                elif int(variable3) == 2:
                    file.write("\nJerarquia: Distribucion")
                elif int(variable3) == 3:
                    file.write("\nJerarquia: Acceso")
                file.write("\nServicio: "+ str(servicios))
            elif int(variable1) == 2:
                print("Elija un servicio de red para su switch multicapa: \n1. Datos \n2. VLAN \n3. Trunking  \n4. Enrutamiento \n5. Salir")
                variable4 = int()
                while variable4 != 5:
                    variable4 = int(input("Introduzca una opcion: "))
                    if variable4 == 1:
                        servicios.append("Datos")
                    elif variable4 == 2:
                        servicios.append("VLAN")
                    elif variable4 == 3:
                        servicios.append("Trunking")
                    elif variable4 == 4:
                        servicios.append("Enrutamiento")
                file.write("Switch Multicapa: " + variable2)
                if int(variable3) == 1:
                    file.write("\nJerarquia: Nucleo")
                elif int(variable3) == 2:
                    file.write("\nJerarquia: Distribucion")
                elif int(variable3) == 3:
                    file.write("\nJerarquia: Acceso")
                file.write("\nServicio: "+ str(servicios))
            elif int(variable1) == 3:
                variable4 = int()
                print("Elija un servicio de red para su router: \n1. Enrutamiento \n2. Salir")
                while variable4 != 2:
                    variable4 = int(input("Introduzca una opcion: "))
                    if variable4 == 1:
                        servicios.append("Datos")
                file.write("Router: " + variable2)
                if int(variable3) == 1:
                    file.write("\nJerarquia: Nucleo")
                elif int(variable3) == 2:
                    file.write("\nJerarquia: Distribucion")
                elif int(variable3) == 3:
                    file.write("\nJerarquia: Acceso")
                file.write("\nServicio: "+ str(servicios))
            file.write("\n----------------------------------\n")
            file.close()
        selectorReset = input("Presione enter para volver al menu")
    

    # Creador de campus a base de una lista
    elif int(selector) == 4:
        os.system("clear")
        print("\n \nElija el nombre de el campus que desea agregar: \n")
        campusNombre = input()
        campus.append(campusNombre)
        with open(campusNombre+".txt", "w") as fp:
            pass
        file=open(campusNombre+".txt", 'a')
        file.write("----------------------------------\n")
        file.close()
        selectorReset = input("Presione enter para volver al menu")
    elif int(selector) == 5:
        os.system("clear")
        print("Gracias por usar la aplicacion!")
        break
