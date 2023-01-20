class Pet:
    # implement __init__(name, type, tricks)
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
    
    # sleep() - increases the pet's energy by 25    
    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy is now {self.energy}.")
        return self
    
    # eat() - increases the pet's energy by 5 and health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy is now {self.energy} and health is now {self.health}.")
        return self
    
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name}'s health is now {self.health}.")
        return self
    
    # noise() - prints out the pet's sound
    def noise(self):
        print(self.sound)