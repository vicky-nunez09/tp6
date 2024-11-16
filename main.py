def modificar_dato(dato):
    if dato=="1":
        nuevoNombre=input("Ingrese el nuevo nombre: ")
        lista_alumnos[alumno-1]["Nombre"]=nuevoNombre
        print(lista_alumnos[alumno-1])
    elif dato=="2":
        nuevoApellido=input("Ingrese el nuevo apellido: ")
        lista_alumnos[alumno-1]["Apellido"]=nuevoApellido
        print(lista_alumnos[alumno-1])
    elif dato=="3":
        nuevoDNI=input("Ingrese el nuevo DNI: ")
        lista_alumnos[alumno-1]["DNI"]=nuevoDNI
        print(lista_alumnos[alumno-1])
    elif dato=="4":
        nuevaFechaNac=input("Ingrese la nueva fecha de nacimiento: ")
        lista_alumnos[alumno-1]["Fecha de nacimiento"]=nuevaFechaNac
        print(lista_alumnos[alumno-1])
    elif dato=="5":
        nuevoTutor=input("Ingrese el nuevo tutor: ")
        lista_alumnos[alumno-1]["Tutor"]=nuevoTutor
        print(lista_alumnos[alumno-1])
    elif  dato=="6":
        nota1=int(input("Ingrese la primer nota: "))
        nota2=int(input("Ingrese la segunda nota: "))
        nota3=int(input("Ingrese la tercera nota: "))
        nota4=int(input("Ingrese la cuarta nota: "))
        nota5=int(input("Ingrese la quinta nota: "))
        lista_alumnos[alumno-1]["Notas"]=(nota1,nota2,nota3,nota4,nota5)
        print(lista_alumnos[alumno-1])
    elif dato=="7":
        nuevasFaltas=int(input("Ingrese la cantidad de faltas: "))
        lista_alumnos[alumno-1]["Faltas"]=nuevasFaltas
        print(lista_alumnos[alumno-1])
    elif dato=="8":
        nuevasAmonestaciones=int(input("Ingrese la cantidad de amonestaciones: "))
        lista_alumnos[alumno-1]["Amonestaciones"]=nuevasAmonestaciones
        print(lista_alumnos[alumno-1])
    else:
        print("Por favor, ingrese una opción válida (1-8): ")

def agregarAlumno():
    nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    DNI=input("Ingrese el DNI: ")
    cumpleaños=input("Ingrese la fecha de nacimiento (formato dd-mm-aaaa): ")
    tutor=input("Ingrese el tutor: ")
    nota1=int(input("Ingrese la primer nota: "))
    nota2=int(input("Ingrese la segunda nota: "))
    nota3=int(input("Ingrese la tercera nota: "))
    nota4=int(input("Ingrese la cuarta nota: "))
    nota5=int(input("Ingrese la quinta nota: "))
    faltas=int(input("Ingrese la cantidad de faltas (x): "))
    amonestaciones=int(input("Ingrese la cantidad de amonestaciones (x): "))

    nuevo_alumno={"Nombre": nombre,
    "Apellido" : apellido,
    "DNI" : DNI,
    "Fecha de nacimiento" : cumpleaños,
    "Tutor" : tutor,
    "Notas" : (nota1,nota2,nota3,nota4,nota5),
    "Faltas" : faltas,
    "Amonestaciones" : amonestaciones}
    lista_alumnos.append(nuevo_alumno)
    print(nuevo_alumno)


alumno1={"Nombre": "Samanta",
"Apellido" : "Díaz",
"DNI" : 47623824,
"Fecha de nacimiento" : "25-11-2006",
"Tutor" : "Javier Ignacio Díaz",
"Notas" : (10,9,9,10,9),
"Faltas" : 5,
"Amonestaciones" : 0
}

alumno2={"Nombre": "Francesco",
"Apellido" : "Costansi",
"DNI" : 47619615,
"Fecha de nacimiento" : "11-10-2006",
"Tutor" : "Bernardo Costansi",
"Notas" : (8,7,10,6,9),
"Faltas" : 6,
"Amonestaciones" : 5}

alumno3={"Nombre": "Agustina",
"Apellido" : "Vilte",
"DNI" : 47644857,
"Fecha de nacimiento" : "31-9-2006",
"Tutor" : "Ernesto Vilte",
"Notas" : (5,3,6,4,6),
"Faltas" : 3,
"Amonestaciones" : 0}

alumno4={"Nombre": "Tomás David",
"Apellido" : "Hubaide",
"DNI" : 48083443,
"Fecha de nacimiento" : "24-5-2007",
"Tutor" : "Raul Alejandro Hubaide",
"Notas" : (10,8,9,10,9),
"Faltas" : 8,
"Amonestaciones" : 0}

lista_alumnos=[alumno1, alumno2, alumno3, alumno4]

while True:
    print("BIENVENIDO AL MENÚ\n1-Mostrar alumnos.\n2-Modificar alumno.\n3-Expulsar alumno.\n4-Agregar alumno.\n5-Salir del programa.")
    actividad=input("Qué actividad desea realizar?: ")
    if actividad=="1":
        for i in range(0,len(lista_alumnos)):
            print(lista_alumnos[i])
    elif actividad=="2":
        for i in range(0,len(lista_alumnos)):
            print(lista_alumnos[i])
        
        alumno=int(input("Qué alumno desea modificar?(1, 2, 3, etc.): "))
        print(lista_alumnos[alumno-1])
    
        print("Nombre: 1\nApellido: 2\nDNI: 3\nFecha de nacimiento: 4\nTutor: 5\nNotas: 6\nFaltas: 7\nAmonestaciones: 8")
        dato=input("Qué dato desea modificar?: ")
        modificar_dato(dato)
    elif actividad=="3":
        for i in range(0,len(lista_alumnos)):
            print(lista_alumnos[i])
        
        expulsión=int(input("Qué alumno desea expulsar? (1, 2, 3, etc): "))
        lista_alumnos.remove(lista_alumnos[expulsión-1])
        for i in range(0,len(lista_alumnos)):
            print(lista_alumnos[i])
    elif actividad=="4":
        agregarAlumno()
    elif actividad=="5":
        break
    else:
        print("Por favor, seleccione una opción válida (1-5): ")