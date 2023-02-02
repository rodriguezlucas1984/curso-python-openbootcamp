# modulo para determinar si una cadena de texto es un nombre de un pais existente
from paisesExistentes import Paises


class Test():
    def main():
        setPaises = set()
        while len(setPaises) == 0:
            lista = input(
                "Ingrese una lista de paises, separada por comas:\n").split(",")
            paises = set(map(lambda x: x.strip(), lista))
            paises_aceptados = filter(lambda x: Paises.existe(x), paises)
            paises_rechazados = list(filter(lambda x: not Paises.existe(
                x), paises))
            setPaises = sorted(set(paises_aceptados))
            print(
                f'Los paises considerados validos(ordenados alfabeticamente) son:\n{setPaises if len(setPaises)>0 else ""}')
            print(f'Los paises invalidos son:\n{paises_rechazados}')


if __name__ == '__main__':
    Test.main()
