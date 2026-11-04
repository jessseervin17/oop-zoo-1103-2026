class Animal:
    def __init__(self, name:str, species:str):
        self.name=name
        self.species=species
    
    def speak(self):
        return "Animal sound"

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"
    
class Bird(Animal):
    def __init__(self, name, species, wingspan=2.5):
        super().__init__(name, species)
        self.wingspan=wingspan
    
class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

