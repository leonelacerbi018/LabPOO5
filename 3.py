class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Coche(Vehiculo):
    def mover(self):
        return "manejando por la calle."

class Bicicleta(Vehiculo):
    def mover(self):
        return "andando por la ciclovía."


def hacer_mover_vehiculos(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print(f"El {vehiculo.__class__.__name__} se está {vehiculo.mover()}")


def main():
    mis_vehiculos = [
        Coche(),
        Bicicleta()
    ]
    
    hacer_mover_vehiculos(mis_vehiculos)

if __name__ == "__main__":
    main()
