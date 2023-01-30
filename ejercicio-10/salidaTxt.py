class SalidaTxt:
    def __init__(self, path) -> None:
        self.__path = path

    def escribir(self, texto):
        f = open(self.__path, 'wt')
        f.write(texto)
        f.close()

    def leer(selft):
        f = open(selft.__path, 'rt')
        texto = f.read()
        f.close()
        return texto


class Escritor:

    def main():
        libro = SalidaTxt('libro.txt')
        oracion = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
        print(f'Texto a escribir "{oracion}"\n')
        libro.escribir(oracion)
        print(f'Texto leido: "{libro.leer()}"\n')
        print(
            f'Ambos textos son: {"IGUALES" if oracion==libro.leer() else "DIFERENTES"}')


if __name__ == '__main__':
    Escritor.main()
