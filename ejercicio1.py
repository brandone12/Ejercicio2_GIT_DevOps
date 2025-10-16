class Animal:
    def hablar(self):
        return "El animal hace un sonido"


class Perro(Animal):
    def hablar(self):
        return "El perro hace guau y woof"


class Gato(Animal):
    def hablar(self):
        return "El gato hace miau y purr"


class Vaca(Animal):
    def hablar(self):
        return "La vaca hace muu"


# Polimorfismo en acción.
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    print(animal.hablar())
