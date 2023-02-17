from models.alumno import ModelAlumno


def main():
    # Cantidad de alumnos
    cantidad = ModelAlumno.cantidad()
    # Si la tabla esta vacia insertar 8 alumnos
    if cantidad == 0:
        ModelAlumno.crear(cantidad+1, 'Juan', 'Perez')
        ModelAlumno.crear(cantidad+2, 'Daniel', 'Garcia')
        ModelAlumno.crear(cantidad+3, 'Juan', 'Denardi')
        ModelAlumno.crear(cantidad+4, 'Miguel', 'Ramirez')
        ModelAlumno.crear(cantidad+5, 'Fernando', 'Gomez')
        ModelAlumno.crear(cantidad+6, 'Marcelo', 'Hernandez')
        ModelAlumno.crear(cantidad+7, 'Daniel', 'Giri')
        ModelAlumno.crear(cantidad+8, 'Hugo', 'Maldonado')

    # Menu
    opcion = ""
    while opcion != "q":
        print("---------------------------------------")
        print("Menu:")
        print("\t1- Ver alumnos")
        print("\t2- Registrar alumno")
        print("\t3- Buscar alumno por nombre")
        print("\t4- Borrar alumno por id")
        print("\tq- Salir")
        print("---------------------------------------")
        opcion = input("Elija una opción:")

        # Ver alumnos
        if opcion == "1":
            alumnos = ModelAlumno.obtenerTodos()
            print("ALUMNOS")
            for alumno in alumnos:
                print(alumno)
            continue

        # Registrar alumno
        if opcion == "2":
            alumno = {'id': 0, 'nombre': "", 'apellido': ""}

            while alumno["id"] == 0 or alumno['nombre'] == "" or alumno["apellido"] == "":
                if alumno["id"] == 0:
                    id = input("Ingrese el id: ")
                    if not id.isdecimal():
                        print("El id debe ser un nro mayor que cero")
                        continue
                    alumno["id"] = int(id)
                if alumno["nombre"] == "":
                    nombre = input("Ingrese el nombre: ")
                    if nombre == "":
                        print("El nombre debe no puede ser una cadena vacia")
                        continue
                    alumno["nombre"] = nombre.capitalize()
                if alumno["apellido"] == "":
                    apellido = input("Ingrese el apellido: ")
                    if apellido == "":
                        print("El apellido debe no puede ser una cadena vacia")
                        continue
                    alumno["apellido"] = apellido.capitalize()
            try:
                ModelAlumno.crear(
                    alumno["id"], alumno["nombre"], alumno["apellido"])
            except Exception as e:
                print(e)
            continue

        # Buscar alumno por nombre
        if opcion == "3":
            nombre = ""
            while nombre == "":
                nombre = input("Ingrese el nombre: ").capitalize()
                if nombre == "":
                    print("El nombre debe no puede ser una cadena vacia")
            alumnos = ModelAlumno.buscar({'nombre': nombre})
            if len(alumnos) == 0:
                print(f"\nNingun alumno tiene el nombre: {nombre}\n")
            for alumno in alumnos:
                print(alumno)
            continue

        # Borrar alumno
        if opcion == "4":
            id = 0
            while id == 0:
                id = input("Ingrese el id: ")
                if not id.isdecimal():
                    print("El id debe ser un nro mayor que cero")
                    id = 0
            filas_afectadas = ModelAlumno.eliminar(int(id))
            if filas_afectadas > 0:
                print(f"Se borro correctamente el alumno con id: {id}")
            else:
                print(f'No hay ningun alumno con el id:{id}')
            continue

        # Ingreso de opción invalida
        if opcion != "q":
            print(f'\nEl valor "{opcion}" no es una opción valida...\n')


if __name__ == '__main__':
    main()
