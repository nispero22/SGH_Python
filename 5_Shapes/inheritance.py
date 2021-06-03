class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old and his breed is {self.breed}"


    def is_majeur(self):
        if self.age>= 2:
            return True
        else:
            return False

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")


# create a child class
class JackRussellTerrier(Dog):

    def __init__(self, name, age, sound):
        super().__init__(name, age,"Jack Russell Terrier")
        self.sound=sound
        # equivalent à Dog()
        print(self.age)

    def speak(self):
        print(f"{self.name} says {self.sound}")


miles = JackRussellTerrier("Miles", 6, "tttttt")

