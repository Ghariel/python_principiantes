# Tarea:
# Pensar una manera mas eficiente de obtener alumnos en base a la matricula
# La matricula se debe poder ingresar por un input del programa pista: input()

# El usuario debe ingresar un numero de matricula, y una funciona tiene que responder
# con los datos de ese alumno

# Limitacion: No se puede usar for.
# Tiene que ser una funcion

# Lista de diccionarios
#alumnos = [
#    {"nombre": "Pepe", "apellido": "Perez", "matricula": 435},
#    {"nombre": "Julieta", "apellido": "Rodriguez", "matricula": 233},
#    {"nombre": "Maria", "apellido": "Rodriguez", "matricula": 123}
#]

#mi diccionario modificado
alumnos = {
    435:{"nombre": "Pepe", "apellido": "Perez"}, 
    233:{"nombre": "Julieta", "apellido": "Rodriguez"},
    123:{"nombre": "Maria", "apellido": "Rodriguez"}
}

#def listar_alumnos(lista_alumnos):
#    for a in lista_alumnos:
#        print(a["nombre"])

#def obtener_alumno(matricula, lista_alumnos):
#    for a in lista_alumnos:
#        if a['matricula'] == matricula:
#            return a

def buscar_matricula():
   #para evitar error al ingresar un dato que no sea entero
   while True:
       try: 
           matricula = int(input("Introduzca el numero de matricula: "))
            break
       except ValueError:
            print("El dato ingresado no es valido :c")
    print(alumnos.get(matricula, "No se encontro ningun alunmo que coincida con la matricula ingresada"))

buscar_matricula()    
#listar_alumnos(alumnos)
#print(alumnos)
#mi_alumno = obtener_alumno(435, alumnos)
#print(mi_alumno)
