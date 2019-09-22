class MyPet:

    def __init__(self, pet_name):
        self.name = pet_name

    def play_fetch(self):
        print("Your pet " + self.name + " seemed to be happy to play fetch!")

orange_cat = MyPet("Miles")
small_dog = MyPet("Fido")

print(orange_cat.name)
small_dog.play_fetch()
