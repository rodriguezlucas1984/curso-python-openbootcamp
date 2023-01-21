from enum import Enum


class Color (Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3
    BLANCO = 4
    NEGRO = 5
    PLATA = 6


CANTIDAD_PUERTAS_COCHE = [2, 3, 4, 5]


class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self) -> str:
        return f'El {self.__class__.__name__} es de color {Color(self.color).name}, tiene {self.ruedas} ruedas y {self.puertas} puertas'


class Coche(Vehiculo):
    def __init__(self, color, puertas, velocidad, cilindrada):
        if puertas not in CANTIDAD_PUERTAS_COCHE:
            raise ValueError("La cantidad de puertas no es valida")
        super().__init__(color, 4, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return f'{super().__str__()}. Corre a {self.velocidad} Km/h y tiene una cilindrada de {self.cilindrada}cc '


def main():
    coche = Coche(Color.ROJO, 2, 350, 6262)
    print(coche.__str__())


if __name__ == "__main__":
    main()
