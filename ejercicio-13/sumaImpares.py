# Importación de funcion para generar valores enteros pertenecientes a un intervalo
from random import randrange
# Importación de la funcion reduce
from functools import reduce


class GeneradorListaValores:
    @staticmethod
    def generar(cantidad, min, max):
        valores = set()
        if cantidad < 1:
            raise ValueError("cantidad tiene que ser mayor que 1")
        if max <= min:
            raise ValueError("min tiene que ser mayor o igual a max")
        while len(valores) < cantidad:
            valor = randrange(min, max+1)
            valores.add(valor)

        return sorted(valores)


class Test:
    def main():
        valores = GeneradorListaValores.generar(20, 10, 150)
        print(f'Lista de valores:\n{valores}')
        valores = list(filter(lambda x: x % 2 != 0, valores))
        valores.sort()
        print(f'Valores impares:\n{valores}')
        print(f'Suma:{reduce(lambda a,b:a+b,valores)}')


if __name__ == "__main__":
    Test.main()
