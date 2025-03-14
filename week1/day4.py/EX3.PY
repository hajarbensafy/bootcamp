from random import choice

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ', '.join([dog.name for dog in args])
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(choice(tricks))
        else:
            print(f"{self.name} is not trained yet")

# Create an instance of PetDog
pet_dog = PetDog("Rex", 4, 35)

# Test the methods
pet_dog.train()
pet_dog.play(dog1, dog2, dog3)
pet_dog.do_a_trick()