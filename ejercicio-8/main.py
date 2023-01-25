from calculadora import dividir, multiplicar, restar, sumar
from random import randrange, random


def main():
    a = randrange(-1000000, 1000000)*random()
    b = randrange(-1000000, 1000000)*random()

    print(f'El valor de a es: {a}')
    print(f'El valor de b es: {b}')

    print(f'    a + b: {sumar(a,b)}')
    print(f'    a - b: {restar(a,b)}')
    print(f'    a * b: {multiplicar(a,b)}')
    print(f'    a / b: {dividir(a,b)}')


if __name__ == '__main__':
    main()
