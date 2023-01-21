class Alumno:
    # Constructor por defecto
    def __init__(self):
        self.__nombre = ""
        self.__nota = 0

    # get nombre
    def get_nombre(self):
        return self.__nombre

    # get nota
    def get_nota(self):
        return self.__nota

    # set nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # set nota
    def set_nota(self, nota):
        self.__nota = nota

    # Mostar alumno
    def toString(self):
        return f'Alumno:{self.__nombre}\nNota:{self.__nota}\nResultado:{"Aprobo" if self.__nota >= 6 else "Reprobo"}'


def main():
    alumno = Alumno()
    print(alumno.toString())
    alumno.set_nombre("Lucas")
    alumno.set_nota(7)
    print(alumno.toString())


if __name__ == "__main__":
    main()
