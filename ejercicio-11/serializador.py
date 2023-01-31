import pickle


class CombustibleInsuficienteError(Exception):
    pass


class DesperdicioCombustibleError(Exception):
    pass


class Vehiculo:
    def __init__(self, marca, modelo, patente, tamañoTanque, cantidadCombustible, rendimiento) -> None:
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.tamañoTanque = tamañoTanque  # En litros
        self.cantidadCombustible = tamañoTanque if cantidadCombustible > tamañoTanque else cantidadCombustible
        self.rendimiento = rendimiento  # Kilometros/litro

    def viajar(self, kilometros):
        """
            Devuelve la cantidad de combustible luego de realizar un viaje. En caso de no haber suficiente combustible para realizar dicho viaje, dispara una excepcion
        """
        if self.cantidadCombustible * self.rendimiento < kilometros:
            raise CombustibleInsuficienteError(
                "Debes cargar combustible en un punto intermedio")

        self.cantidadCombustible -= kilometros/self.rendimiento
        return self.cantidadCombustible

    def cargarCombustible(self, litros):
        """
            Devuelve la cantidad de combustible luego de cargar. En caso de que el combustible exceda el tamaño del tanque dispara una excepción
        """
        if self.cantidadCombustible+litros > self.tamañoTanque:
            raise DesperdicioCombustibleError(
                f'Rebalzara el tanque de combustible. Puede cargar hasta {self.tamañoTanque-self.cantidadCombustible} litros.')
        self.cantidadCombustible += litros
        return self.cantidadCombustible

    def __str__(self) -> str:
        return f'La marca del vehiculo es:{self.marca}.\nEl modelo del vehiculo es:{self.modelo}.\nLa patente es:{self.patente}.\nTiene un tanque de {self.tamañoTanque} litros.\nActualmente tiene {self.cantidadCombustible} litros de combustible.\nSu rendimiento es: {self.rendimiento} km/l'


class Serializador:
    def __init__(self, path) -> None:
        self.path = path

    def serializar(self, object) -> None:
        """
            Convierte un objeto en una secuencia de bytes para almacenarlo en un archivo.
        """
        f = open(self.path, 'wb')
        pickle.dump(object, f)
        f.close()

    def deserializar(self) -> object:
        """
            Convierte una representacion textual de un objeto (datos serializados) provenientes de un archivo  en un objeto.
        """
        f = open(self.path, 'rb')
        object = pickle.load(f)
        f.close()
        return object


class Test:
    def main():
        serializador = Serializador('vehiculo.bin')
        auto = Vehiculo('Volkswagen', 'Polo', 'AA123BB', 60, 30, 15)
        print("El vehiculo creado es:\n")
        print(auto)
        print('Serializado vehiculo en archivo vehiculo.bin')
        serializador.serializar(auto)
        vehiculo = serializador.deserializar()
        print("\nVehiculo deserializado:\n")
        print(vehiculo)
        print(
            f'Luego de un viaje de 200 km el vehiculo tiene {vehiculo.viajar(200)} litros de combustible.')
        print(
            f'Si cargamos 15 litros  vehiculo tiene {vehiculo.cargarCombustible(15)} litros de combustible.')
        print(vehiculo)


if __name__ == '__main__':
    Test.main()
