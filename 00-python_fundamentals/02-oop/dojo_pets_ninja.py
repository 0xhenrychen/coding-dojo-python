import dojo_pets_pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    
    # feed() - feeds the ninka's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
        

# Create a pet   
everest = dojo_pets_pet.Pet("Everest", "Golden Retriever", "Jump", 100, 50, "Bark Bark!")

# Create a ninja
henry = Ninja("Henry", "Chen", everest, "Cookies", "Chow-Time")

henry.feed()
henry.walk()
henry.bathe()