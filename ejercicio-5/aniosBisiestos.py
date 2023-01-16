import re


def esBisiesto(anio):
    if (anio < 1582):
        raise ValueError(
            "El calendario gregoriano se utiliza a partir del año 1582")
    if anio % 4 != 0:
        return False
    if anio % 100 == 0 and anio % 400:
        return False
    return True


def main():
    while True:
        try:
            anio = input("Ingrese el año: ")
            if re.match("[-+]?\d+$", anio) is None:
                raise ValueError("Ingrese un valor entero")
            if esBisiesto(int(anio)):
                print("Es año", anio, "es bisisesto")
            else:
                print("Es año", anio, "no es bisisesto")
            c = input("Ingrese 'q' para finalizar: ")
            if c == 'q':
                break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
