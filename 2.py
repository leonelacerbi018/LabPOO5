class Animal:
    def hacerSonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):
    def hacerSonido(self):
        return "Guau"

class Gato(Animal):
    def hacerSonido(self):
        return "Miau"

def main():
    animales = [
        Perro(),
        Gato(),
        Perro(),
        Gato()
    ]
    
    for animal in animales:
        print(f"El {animal.__class__.__name__} hace: {animal.hacerSonido()}")

if __name__ == "__main__":
    main()
